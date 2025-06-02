"""
Integration tests for the SeasonalForecast pipeline in seasonal_forecast_tools.

This test suite verifies that the full workflow executes correctly:
from local GRIB input to NetCDF index computation and hazard generation (HDF5),
for all supported thermal index metrics.

Each test checks file creation, dataset content, and hazard consistency.
"""

from pathlib import Path
import unittest

import xarray as xr

from seasonal_forecast_tools.core.seasonal_forecast import SeasonalForecast, Hazard, CLIMADA_INSTALLED

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

class TestIntegrationWorkflow(unittest.TestCase):
    """
    Integration test for the seasonal forecast pipeline:
    From local GRIB data to index NetCDF to Hazard HDF5.
    """

    @classmethod
    def setUpClass(cls):
        """
        Prepare the test environment and run the full seasonal forecast pipeline.

        This method initializes SeasonalForecast objects for each index metric using
        predefined parameters, skips downloading (GRIB files exist locally),
        processes the data, calculates the indices, saves hazards, and stores paths.
        """
        repo_root = Path(__file__).resolve().parents[1]
        cls.base_dir = repo_root / "test" / "climada_data_test" / "copernicus_data" / "seasonal_forecasts"

        cls.data_format = "grib"
        cls.originating_centre = "dwd"
        cls.system = "21"
        cls.year = 2022
        cls.init_month = 11
        cls.valid_period = ["December", "February"]
        cls.bounds = [-59, -35, -52, -29]  # W, S, E, N

        cls.forecasts = {}
        cls.hazard_paths = {}
        cls.nc_paths = {}

        for index_metric in INDEX_METRICS:
            forecast = SeasonalForecast(
                index_metric=index_metric,
                year_list=[cls.year],
                forecast_period=cls.valid_period,
                initiation_month=["November"],
                bounds=cls.bounds,
                data_format=cls.data_format,
                originating_centre=cls.originating_centre,
                system=cls.system,
                data_out=cls.base_dir
            )
            forecast._process(overwrite=True)
            forecast.calculate_index(overwrite=True)
            if CLIMADA_INSTALLED:
                forecast.save_index_to_hazard(overwrite=True)

            month_str = forecast.initiation_month_str[0]
            cls.forecasts[index_metric] = forecast
            cls.hazard_paths[index_metric] = forecast.get_pipeline_path(cls.year, month_str, "hazard")
            cls.nc_paths[index_metric] = forecast.get_pipeline_path(cls.year, month_str, "indices")["monthly"]

    def test_grib_input_exists(self):
        """
        Test if the expected GRIB input file exists at the correct path for each index.
        """
        for index_metric in INDEX_METRICS:
            with self.subTest(index_metric=index_metric):
                grib_path = (
                    self.base_dir / self.originating_centre / f"sys{self.system}" / str(self.year)
                    / f"init{self.init_month:02d}" / "valid12_02" / "downloaded_data" / "grib"
                    / f"{index_metric}_boundsN-59_S-35_E-52_W-29.grib"
                )
                self.assertTrue(grib_path.exists(), f"GRIB input file missing: {grib_path}")

    def test_nc_index_file_created(self):
        """
        Test if the NetCDF index file was created during processing for each index.
        """
        for index_metric in INDEX_METRICS:
            with self.subTest(index_metric=index_metric):
                self.assertTrue(self.nc_paths[index_metric].exists(),
                    f"NetCDF index file not found: {self.nc_paths[index_metric]}")

    def test_nc_index_content(self):
        """
        Validate the content of the NetCDF index file for each index.

        Checks that:
        - the expected index variable is present,
        - the 'step' dimension exists,
        - the variable has non-empty values.
        """
        for index_metric in INDEX_METRICS:
            with self.subTest(index_metric=index_metric):
                ds = xr.open_dataset(self.nc_paths[index_metric])
                self.assertIn(index_metric, ds.data_vars)
                self.assertIn("step", ds.dims)
                self.assertGreater(ds[index_metric].values.size, 0, "Index variable is empty.")

    def test_hazard_file_created(self):
        """
        Test if the hazard HDF5 file was created after index-to-hazard conversion.
        """
        for index_metric in INDEX_METRICS:
            with self.subTest(index_metric=index_metric):
                self.assertTrue(self.hazard_paths[index_metric].exists(),
                    f"Hazard file not found: {self.hazard_paths[index_metric]}")

    @unittest.skipUnless(CLIMADA_INSTALLED, "Without climada there is no functional Hazard class.")
    def test_hazard_content(self):
        """
        Validate the content of the hazard file for each index.

        Checks that:
        - the intensity array is not empty,
        - at least one date is present,
        - the hazard type matches the index metric.

        Note: If CLIMADA is not installed, this test is skipped.
        """
        for index_metric in INDEX_METRICS:
            with self.subTest(index_metric=index_metric):
                haz = Hazard.from_hdf5(self.hazard_paths[index_metric])
                self.assertGreater(haz.intensity.size, 0, "Hazard intensity is empty.")
                self.assertGreater(len(haz.date), 0, "Hazard has no dates.")
                self.assertEqual(haz.haz_type, index_metric)

if __name__ == "__main__":
    unittest.main()
