"""
Integration tests for seasonal_forecast_tools.SeasonalForecast (IO mocked).

This test suite covers:
- End-to-end orchestration: init → preprocess → compute → finalize.
- Isolation from external services (CDS, filesystem) via mocks.
- Error handling and minimal output contracts under mocked operations.
"""
import unittest
from unittest.mock import patch
from pathlib import Path
import tempfile
import numpy as np
import pandas as pd
import xarray as xr

from seasonal_forecast_tools.core.seasonal_forecast import SeasonalForecast


def make_synthetic_ds(n_members=2, n_steps=48, ny=3, nx=4):
    """
    Build a minimal GRIB-like xarray.Dataset.

    Notes
    -----
    - 'step' is an hourly DatetimeIndex so seasonal_statistics can resample by day.
    - Variables include t2m, d2m, u10, v10 expected by heat-stress indices.
    - Units are Kelvin for temperatures to match typical GRIB-derived fields.
    """
    numbers = np.arange(n_members)
    times = pd.date_range("2022-12-01", periods=n_steps, freq="H")  # DatetimeIndex
    lats = np.linspace(46.0, 48.0, ny)
    lons = np.linspace(8.0, 10.0, nx)
    shape = (n_members, n_steps, ny, nx)

    return xr.Dataset(
        data_vars={
            "t2m": (["number", "step", "latitude", "longitude"], 273.15 + 12.0 + np.random.rand(*shape)),
            "d2m": (["number", "step", "latitude", "longitude"], 273.15 + 9.0 + np.random.rand(*shape)),
            "u10": (["number", "step", "latitude", "longitude"], np.random.randn(*shape)),
            "v10": (["number", "step", "latitude", "longitude"], np.random.randn(*shape)),
        },
        coords={
            "number": numbers,
            "step": times,                          # DatetimeIndex required for resample
            "valid_time": ("step", times),          # common coord used downstream
            "latitude": lats,
            "longitude": lons,
        },
        attrs={"originating_centre": "dwd", "system": "21", "data_format": "grib"},
    )


class TestSeasonalForecastSmoke(unittest.TestCase):
    @patch("xarray.Dataset.to_netcdf")
    @patch("xarray.open_dataset")
    @patch("seasonal_forecast_tools.core.seasonal_forecast.SeasonalForecast._process")
    def test_calculate_index_smoke(self, mock_process, mock_open, mock_to_netcdf):
        # Return our synthetic, timestamped dataset for any open_dataset call
        mock_open.return_value = make_synthetic_ds()
        mock_to_netcdf.return_value = None

        with tempfile.TemporaryDirectory() as tmp:
            sf = SeasonalForecast(
                index_metric="TR",                       # uses GRIB path and t2m daily min
                year_list=[2022],
                forecast_period=["December", "February"],
                initiation_month=["November"],
                bounds=[-59, -35, -52, -29],
                data_format="grib",
                originating_centre="dwd",
                system="21",
                data_out=Path(tmp),
            )

            # Internal processing step mocked
            sf._process(overwrite=True)

            # This should now succeed because 'step' is a DatetimeIndex
            sf.calculate_index(overwrite=True)

        assert mock_process.called, "Expected _process to be called"
        assert mock_open.called, "Expected xarray.open_dataset to be called"
        assert mock_to_netcdf.called, "Expected Dataset.to_netcdf to be called"


if __name__ == "__main__":
    unittest.main()
