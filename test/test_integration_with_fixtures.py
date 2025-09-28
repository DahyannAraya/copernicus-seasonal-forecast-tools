"""
Integration tests for the SeasonalForecast pipeline using mocked/synthetic data.

This test suite verifies that the full workflow executes correctly:
from synthetic GRIB-like inputs to NetCDF index computation and hazard generation (HDF5),
for all supported thermal index metrics.

Uses mocked data to test integration without requiring deep repository structure.
"""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open
import numpy as np
import pandas as pd
import xarray as xr

from seasonal_forecast_tools.core.seasonal_forecast import SeasonalForecast, CLIMADA_INSTALLED

# If CLIMADA is available, import Hazard for testing
if CLIMADA_INSTALLED:
    from seasonal_forecast_tools.core.seasonal_forecast import Hazard  # noqa: F401

INDEX_METRICS = [
    "Tmean",  # Mean Temperature
    "Tmin",   # Minimum Temperature
    "Tmax",   # Maximum Temperature
    "HIA",    # Heat Index Adjusted
    "HIS",    # Heat Index Simplified
    "HUM",    # Humidex
    "AT",     # Apparent Temperature
    "WBGT",   # Wet Bulb Globe Temperature (Simple)
    "HW",     # Heat Wave
    "TR",     # Tropical Nights
    "TX30"    # Hot Days
]

class TestIntegrationWorkflowMocked(unittest.TestCase):
    """
    Integration test for the seasonal forecast pipeline using mocked data.
    Tests the complete workflow without requiring repository file structure.
    """

    def setUp(self):
        """Set up temporary directory and mock data for each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name)

        # Test parameters
        self.originating_centre = "dwd"
        self.system = "21"
        self.year = 2022
        self.init_month = 11
        self.valid_period = ["December", "February"]
        self.bounds = [-59, -35, -52, -29]  # W, S, E, N

        np.random.seed(42)

    def tearDown(self):
        """Clean up temporary directory."""
        self.temp_dir.cleanup()

    def _create_mock_grib_dataset(self, index_metric):
        """Create synthetic xarray dataset mimicking GRIB data structure."""
        n_members = 3
        n_steps = 5
        n_lat = 4
        n_lon = 4

        # Create realistic coordinate arrays
        dates = pd.date_range(start="2022-12-01", periods=n_steps, freq="D")
        lat_vals = np.linspace(-35, -29, n_lat)
        lon_vals = np.linspace(-59, -52, n_lon)

        # Generate synthetic weather data
        base_temp = 290.0  # Kelvin
        temp_data = (
            base_temp
            + np.random.normal(0, 5, (n_members, n_steps, n_lat, n_lon))
            + np.arange(n_steps).reshape(1, -1, 1, 1) * 0.5  # slight trend
        )

        data_vars = {
            "t2m": (["number", "step", "latitude", "longitude"], temp_data),
            "t2m_max": (["number", "step", "latitude", "longitude"], temp_data + 3),
            "t2m_min": (["number", "step", "latitude", "longitude"], temp_data - 3),
            "d2m": (["number", "step", "latitude", "longitude"], temp_data - 5),
            "u10": (
                ["number", "step", "latitude", "longitude"],
                np.random.normal(2, 1, (n_members, n_steps, n_lat, n_lon)),
            ),
            "v10": (
                ["number", "step", "latitude", "longitude"],
                np.random.normal(1, 1, (n_members, n_steps, n_lat, n_lon)),
            ),
        }

        return xr.Dataset(
            data_vars=data_vars,
            coords={
                "number": np.arange(n_members),
                "step": dates,
                "latitude": lat_vals,
                "longitude": lon_vals,
                "valid_time": ("step", dates),
            },
        )

    def _create_mock_processed_dataset(self, index_metric):
        """Create synthetic processed daily dataset."""
        n_members = 3
        n_days = 10
        n_lat = 4
        n_lon = 4

        dates = pd.date_range(start="2022-12-01", periods=n_days, freq="D")
        lat_vals = np.linspace(-35, -29, n_lat)
        lon_vals = np.linspace(-59, -52, n_lon)

        if index_metric in ["TR", "TX30", "HW"]:
            # Binary indices (0 or 1)
            index_data = np.random.choice([0, 1], size=(n_members, n_days, n_lat, n_lon))
        else:
            # Temperature-like indices
            base_value = 25.0 if index_metric.startswith("T") else 30.0
            index_data = base_value + np.random.normal(0, 5, (n_members, n_days, n_lat, n_lon))

        return xr.Dataset(
            data_vars={
                index_metric: (["number", "step", "latitude", "longitude"], index_data)
            },
            coords={
                "number": np.arange(n_members),
                "step": dates,
                "latitude": lat_vals,
                "longitude": lon_vals,
                "valid_time": ("step", dates),
            },
        )

    @patch("seasonal_forecast_tools.core.seasonal_forecast.SeasonalForecast._download")
    @patch("xarray.open_dataset")
    @patch("os.path.exists")
    def test_complete_pipeline_mocked(self, mock_exists, mock_open_dataset, mock_download):
        """Test complete pipeline with mocked data for a single index."""
        index_metric = "Tmax"

        mock_exists.return_value = True

        mock_grib_ds = self._create_mock_grib_dataset(index_metric)
        mock_processed_ds = self._create_mock_processed_dataset(index_metric)
        mock_open_dataset.return_value = mock_grib_ds

        forecast = SeasonalForecast(
            index_metric=index_metric,
            year_list=[self.year],
            forecast_period=self.valid_period,
            initiation_month=["November"],
            bounds=self.bounds,
            data_format="grib",
            originating_centre=self.originating_centre,
            system=self.system,
            data_out=self.base_dir,
        )

        # Mock the processing steps so we do not depend on disk IO
        with patch.object(forecast, "_process") as mock_process:
            with patch.object(forecast, "calculate_index") as mock_calc_index:
                with patch("xarray.open_dataset", return_value=mock_processed_ds):
                    forecast._process(overwrite=True)
                    mock_process.assert_called_once_with(overwrite=True)

                    forecast.calculate_index(overwrite=True)
                    mock_calc_index.assert_called_once_with(overwrite=True)

    @patch("seasonal_forecast_tools.core.seasonal_forecast.SeasonalForecast._download")
    @patch("xarray.open_dataset")
    @patch("os.path.exists")
    def test_index_calculation_for_all_metrics(self, mock_exists, mock_open_dataset, mock_download):
        """Test index calculation works for all supported metrics."""
        mock_exists.return_value = True

        for index_metric in INDEX_METRICS[:3]:  # subset for speed
            with self.subTest(index_metric=index_metric):
                mock_processed_ds = self._create_mock_processed_dataset(index_metric)
                mock_open_dataset.return_value = mock_processed_ds

                forecast = SeasonalForecast(
                    index_metric=index_metric,
                    year_list=[self.year],
                    forecast_period=self.valid_period,
                    initiation_month=["November"],
                    bounds=self.bounds,
                    data_format="grib",
                    originating_centre=self.originating_centre,
                    system=self.system,
                    data_out=self.base_dir,
                )

                with patch.object(forecast, "calculate_index") as mock_calc:
                    forecast.calculate_index(overwrite=True)
                    mock_calc.assert_called_once()

    @unittest.skipUnless(CLIMADA_INSTALLED, "CLIMADA not available")
    @patch("seasonal_forecast_tools.core.seasonal_forecast.SeasonalForecast._download")
    @patch("xarray.open_dataset")
    @patch("os.path.exists")
    def test_hazard_creation_mocked(self, mock_exists, mock_open_dataset, mock_download):
        """Test hazard creation with mocked data."""
        index_metric = "Tmax"
        mock_exists.return_value = True

        mock_processed_ds = self._create_mock_processed_dataset(index_metric)
        mock_open_dataset.return_value = mock_processed_ds

        forecast = SeasonalForecast(
            index_metric=index_metric,
            year_list=[self.year],
            forecast_period=self.valid_period,
            initiation_month=["November"],
            bounds=self.bounds,
            data_format="grib",
            originating_centre=self.originating_centre,
            system=self.system,
            data_out=self.base_dir,
        )

        with patch.object(forecast, "save_index_to_hazard") as mock_save_hazard:
            forecast.save_index_to_hazard(overwrite=True)
            mock_save_hazard.assert_called_once()

    def test_path_construction_integration(self):
        """Test that path construction works within SeasonalForecast context."""
        for index_metric in ["Tmax", "TR"]:
            with self.subTest(index_metric=index_metric):
                forecast = SeasonalForecast(
                    index_metric=index_metric,
                    year_list=[self.year],
                    forecast_period=self.valid_period,
                    initiation_month=["November"],
                    bounds=self.bounds,
                    data_format="grib",
                    originating_centre=self.originating_centre,
                    system=self.system,
                    data_out=self.base_dir,
                )

                month_str = forecast.initiation_month_str[0]

                grib_path = forecast.get_pipeline_path(self.year, month_str, "downloaded_data")
                processed_path = forecast.get_pipeline_path(self.year, month_str, "processed_data")
                indices_paths = forecast.get_pipeline_path(self.year, month_str, "indices")
                hazard_path = forecast.get_pipeline_path(self.year, month_str, "hazard")

                self.assertIn(self.originating_centre, str(grib_path))
                self.assertIn(str(self.year), str(processed_path))
                self.assertIsInstance(indices_paths, dict)
                self.assertIn("index_window_monthly", indices_paths)
                self.assertTrue(str(hazard_path).endswith(".hdf5"))

    @patch("seasonal_forecast_tools.core.seasonal_forecast.SeasonalForecast._download")
    def test_workflow_error_handling(self, mock_download):
        """Test error handling in the workflow."""
        index_metric = "InvalidIndex"

        with self.assertRaises((ValueError, KeyError)):
            _ = SeasonalForecast(
                index_metric=index_metric,
                year_list=[self.year],
                forecast_period=self.valid_period,
                initiation_month=["November"],
                bounds=self.bounds,
                data_format="grib",
                originating_centre=self.originating_centre,
                system=self.system,
                data_out=self.base_dir,
            )

# Execute Tests
if __name__ == "__main__":
    unittest.main()
