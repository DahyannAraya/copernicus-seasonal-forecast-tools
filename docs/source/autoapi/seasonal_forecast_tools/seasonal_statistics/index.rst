seasonal_forecast_tools.seasonal_statistics
===========================================

.. py:module:: seasonal_forecast_tools.seasonal_statistics

.. autoapi-nested-parse::

   This script is part of the seasonal forecast module developed within the U-CLIMADAPT project.
   It provides functionality for accessing, processing, and analyzing seasonal forecast data
   from the Copernicus Climate Data Store (CDS), with an emphasis on computing heat-related
   climate indices and supporting impact-based forecasting.

   The module is designed to interface with CLIMADA but can also be used independently.
   The design is modular and flexible, allowing it to be easily adapted to support
   new climate indices or to serve individual steps in the workflow — such as data download,
   index calculation, or hazard generation — depending on the user's needs.

   This module is distributed under the terms of the GNU General Public License version 3 (GPLv3).
   It is provided without any warranty — not even the implied warranty of merchantability
   or fitness for a particular purpose. For more details, see the GNU General Public License.
   A copy of the GNU General Public License should have been provided with this module.
   If not, it is available at https://www.gnu.org/licenses/.

   ---

   File to calculate different seasonal forecast indices.



Attributes
----------

.. autoapisummary::

   seasonal_forecast_tools.seasonal_statistics.LOGGER


Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.seasonal_statistics.calculate_heat_indices_metrics
   seasonal_forecast_tools.seasonal_statistics.monthly_periods_from_valid_times
   seasonal_forecast_tools.seasonal_statistics.calculate_monthly_dataset
   seasonal_forecast_tools.seasonal_statistics.calculate_statistics_from_index


Module Contents
---------------

.. py:data:: LOGGER

.. py:function:: calculate_heat_indices_metrics(input_file_name, index_metric, tr_threshold=20, hw_threshold=27, hw_min_duration=3, hw_max_gap=0)

   Computes heat indices or temperature-related metrics based on the specified climate index.

   :param input_file_name: Path to the input data file containing the variables required for the computation of the selected index.
                           The file should be in NetCDF (.nc) or GRIB format and contain relevant atmospheric data such as temperature,
                           dewpoint temperature, humidity, or wind speed. Information on the required variables for each index
                           can be found in the `index_definitions` class.
   :type input_file_name: str
   :param index_metric: The climate index to be processed. Supported indices include:
                        - "Tmean" : Mean daily temperature
                        - "Tmax" : Maximum daily temperature
                        - "Tmin" : Minimum daily temperature
                        - "HIS" : Simplified Heat Index
                        - "HIA" : Adjusted Heat Index
                        - "RH"  : Relative Humidity
                        - "HUM" : Humidex
                        - "AT"  : Apparent Temperature
                        - "WBGT": Wet Bulb Globe Temperature (Simple)
   :type index_metric: str
   :param tr_threshold: Temperature threshold (°C) for computing tropical nights (TR).
                        Default is 20°C, meaning nights with Tmin > 20°C are considered tropical.
   :type tr_threshold: float, optional
   :param hw_threshold: Temperature threshold (°C) for detecting a heatwave (HW).
                        Default is 27°C, meaning a heatwave occurs if the temperature remains above this threshold for multiple days.
   :type hw_threshold: float, optional
   :param hw_min_duration: Minimum consecutive days for a heatwave event to be detected.
                           Default is 3 days.
   :type hw_min_duration: int, optional
   :param hw_max_gap: Maximum allowable gap (in days) between heatwave days for them to still be considered part of the same event.
                      Default is 0 days, meaning no gaps are allowed.
   :type hw_max_gap: int, optional

   :returns: A tuple containing three `xarray.Dataset` objects:
             - `daily index` : The calculated daily index values.
             - `monthly index` : Monthly mean values of the index.
             - `index statistics` : Ensemble statistics calculated from the index.
   :rtype: tuple

   :raises ValueError: If an unsupported index is provided.
   :raises FileNotFoundError: If the specified input file does not exist.


.. py:function:: monthly_periods_from_valid_times(ds)

   Create monthly labels from valid times of a dataframe

   :param ds: Dataset of daily values
   :type ds: xr.DataSet

   :returns: DataArray with monthly labels
   :rtype: xr.DataArray


.. py:function:: calculate_monthly_dataset(da_index, index_metric, method)

   Calculate monthly means from daily data

   :param da_index: Dataset containing daily data
   :type da_index: xr.Dataset
   :param index_metric: index to be computed
   :type index_metric: str
   :param method: method to combine daily data to monthly data. Available are "mean" and "count".
   :type method: str

   :returns: Dataset of monthly averages
   :rtype: xr.DataSet


.. py:function:: calculate_statistics_from_index(dataarray)

   Calculates a set of ensemble statistics for the given data array, including mean, median, standard deviation, and selected percentiles.

   :param dataarray: Input data array representing climate index values across multiple ensemble members.
                     It should have a dimension named "number" corresponding to the different ensemble members.
   :type dataarray: xarray.DataArray

   :returns: A dataset containing the calculated statistics:
             - `ensemble_mean`: The mean value across the ensemble members.
             - `ensemble_median`: The median value across the ensemble members.
             - `ensemble_max`: The maximum value across the ensemble members.
             - `ensemble_min`: The minimum value across the ensemble members.
             - `ensemble_std`: The standard deviation across the ensemble members.
             - `ensemble_p05`, `ensemble_p25`, `ensemble_p50`, `ensemble_p75`, `ensemble_p95`: Percentile values (5th, 25th, 50th, 75th, and 95th) across the ensemble members.
   :rtype: xarray.Dataset


