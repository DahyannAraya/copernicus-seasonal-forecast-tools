seasonal_forecast_tools.utils.path_utils
========================================

.. py:module:: seasonal_forecast_tools.utils.path_utils

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
   Path utility functions for seasonal forecast pipelines.
   Provides helpers to generate and check file paths used across the seasonal
   forecast download, processing, and hazard generation modules.



Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.utils.path_utils.get_file_path
   seasonal_forecast_tools.utils.path_utils.check_existing_files


Module Contents
---------------

.. py:function:: get_file_path(base_dir: Union[str, pathlib.Path], originating_centre: str, year: Union[int, str], initiation_month_str: str, valid_period_str: str, data_type: str, index_metric: str, bounds_str: str, system: str, data_format: str = 'grib') -> Union[pathlib.Path, dict]

   Construct the file path or path dictionary for a given forecast dataset.

   Based on forecast metadata (provider, date, system, index, format, etc.), this
   function builds the expected path or dictionary of paths (for indices) that follow
   CLIMADA's seasonal forecast directory structure.

   :param base_dir: Base directory where Copernicus seasonal data is stored.
   :type base_dir: str or Path
   :param originating_centre: Data provider (e.g., 'dwd').
   :type originating_centre: str
   :param year: Forecast initiation year.
   :type year: int or str
   :param initiation_month_str: Forecast initiation month in two-digit string format (e.g., '03').
   :type initiation_month_str: str
   :param valid_period_str: Valid period formatted as '<start>_<end>' (e.g., '06_08').
   :type valid_period_str: str
   :param data_type: Type of data, one of: 'downloaded_data', 'processed_data', 'indices', 'hazard'.
   :type data_type: str
   :param index_metric: Name of the climate index (e.g., 'HW', 'TR', 'Tmax').
   :type index_metric: str
   :param bounds_str: Bounding box string (e.g., 'W4_S44_E11_N48').
   :type bounds_str: str
   :param system: Forecast system (e.g., '21').
   :type system: str
   :param data_format: File format: 'grib', 'netcdf', or 'hdf5' (autodetected by data_type if not provided).
   :type data_format: str, optional

   :returns: A single file path (for non-index types) or a dictionary of paths (for 'indices').
   :rtype: pathlib.Path or dict

   :raises ValueError: If an unknown data_type is provided.

   .. rubric:: Notes

   - The returned path follows the CLIMADA forecast folder structure.
   - Index files return a dict with 'daily', 'monthly', and 'stats' keys.


.. py:function:: check_existing_files(base_dir: Union[str, pathlib.Path], originating_centre: str, index_metric: str, year: int, initiation_month: str, valid_period: List[str], bounds_str: str, system: str, download_format: str = 'grib', print_flag: bool = False) -> str

   Inspect the existence of forecast data files for a given configuration.

   A manual debugging utility, this function checks whether the expected
   files (downloaded, processed, index, hazard) exist in the configured directory tree.

   :param base_dir: Base directory where Copernicus seasonal data is stored.
   :type base_dir: str or Path
   :param originating_centre: Forecast data provider (e.g., 'dwd').
   :type originating_centre: str
   :param index_metric: Climate index to check (e.g., 'HW', 'TR', 'Tmax').
   :type index_metric: str
   :param year: Forecast initiation year.
   :type year: int
   :param initiation_month: Initiation month as string (e.g., 'March').
   :type initiation_month: str
   :param valid_period: Valid forecast months, exactly two (e.g., ['June', 'August']).
   :type valid_period: list of str
   :param bounds_str: Spatial bounds string used in filenames.
   :type bounds_str: str
   :param system: Forecast system version (e.g., '21').
   :type system: str
   :param download_format: Format of the downloaded data. Default is 'grib'.
   :type download_format: str, optional
   :param print_flag: Whether to print the existence check report.
   :type print_flag: bool, optional

   :returns: Summary report indicating which files exist.
   :rtype: str

   :raises ValueError: If valid_period is not exactly two months long.

   .. rubric:: Notes

   - This is a utility function for developers and users to validate pipeline outputs.
   - It is not called by the main forecast processing pipeline.


