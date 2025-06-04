seasonal_forecast_tools.core.seasonal_forecast
==============================================

.. py:module:: seasonal_forecast_tools.core.seasonal_forecast

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
   Core interface for managing seasonal climate forecasts in CLIMADA.

   This module provides the SeasonalForecast class, which enables:
   - Downloading Copernicus seasonal forecast data for selected years and months.
   - Processing raw GRIB or NetCDF data into standardized daily format.
   - Computing user-defined climate indices (e.g., Heatwaves, Tropical Nights, Tmax).
   - Converting the calculated indices into CLIMADA-compatible Hazard objects.
   - Organizing outputs by forecast system, initialization time, and spatial domain.

   The interface integrates several submodules under copernicus_interface:
   - seasonal_forecast.py: implements the core SeasonalForecast class
     that coordinates the entire workflow.
   - downloader.py: handles forecast data retrieval from the CDS API.
   - index_definitions.py: climate index definitions and variable handling.
   - heat_index.py: calculate different thermal indices.
   - seasonal_statistics.py: provides statistical postprocessing and index calculations.
   - path_utils.py: standardizes and validates file and folder structures.
   - time_utils.py: computes lead times and handles month name conversions.
   - forecast_skill.py: manages access and plotting of seasonal forecast skill scores from Zenodo.

   All inputs and outputs are consistently managed through a pipeline structure that ensures
   modularity, traceability, and ease of integration into CLIMADA workflows.









Module Contents
---------------

.. py:data:: CLIMADA_INSTALLED
   :value: True


.. py:data:: DATA_OUT

.. py:data:: LOGGER

.. py:class:: SeasonalForecast(index_metric, year_list, forecast_period, initiation_month, bounds, data_format, originating_centre, system, data_out=None)

   Class for managing the download, processing, and analysis of seasonal climate forecast data.


   .. py:attribute:: initiation_month_str


   .. py:attribute:: valid_period


   .. py:attribute:: valid_period_str
      :value: ''



   .. py:attribute:: index_metric


   .. py:attribute:: year_list


   .. py:attribute:: bounds


   .. py:attribute:: bounds_str
      :value: 'boundsNInstance of builtins.int_SInstance of builtins.int_EInstance of builtins.int_WInstance...



   .. py:attribute:: data_format


   .. py:attribute:: originating_centre


   .. py:attribute:: system


   .. py:attribute:: data_out


   .. py:attribute:: index_spec


   .. py:property:: variables


   .. py:property:: short_variables


   .. py:method:: explain_index(index_metric=None, print_flag=False)

      Retrieve and display information about a specific climate index.

      This function provides an explanation and the required input variables for
      the selected climate index. If no index is provided, the instance's
      `index_metric` is used.

      :param index_metric: Climate index to explain (e.g., 'HW', 'TR', 'Tmax'). If None, uses the
                           instance's index_metric.
      :type index_metric: str, optional
      :param print_flag: If True, prints the explanation. Default is False.
      :type print_flag: bool, optional

      :returns: Text description of the index explanation and required input variables.
      :rtype: str

      .. rubric:: Notes

      The index information is retrieved from `IndexSpecEnum.get_info`.



   .. py:method:: get_pipeline_path(year, initiation_month_str, data_type)

      Provide (and possibly create) file paths for forecast pipeline.

      :param year: Year of the forecast initiation.
      :type year: int
      :param init_month: Initiation month as two-digit string (e.g., '03' for March).
      :type init_month: str
      :param data_type: Type of data to access ('downloaded_data', 'processed_data', 'indices', 'hazard').
      :type data_type: str

      :returns: Path to the requested file(s). For 'indices', returns a dictionary with keys
                'daily', 'monthly', 'stats'.
      :rtype: Path or dict of Path

      :raises ValueError: If unknown data_type is provided.

      .. rubric:: Notes

      File structure:
      {base_dir}/{originating_centre}/sys{system}/{year}/init{init_month}/valid{valid_period}
      /{data_type}



   .. py:method:: download_and_process_data(overwrite=False)

      Download and process seasonal climate forecast data.

      This function performs the complete data pipeline by first downloading
      the raw forecast data for the specified years and initiation months,
      and then processing the downloaded data into a daily NetCDF format.

      :param overwrite: If True, existing downloaded and processed files will be overwritten. Default is False.
      :type overwrite: bool, optional

      :returns: Dictionary containing two keys:
                - "downloaded_data": dict with file paths to downloaded raw data.
                - "processed_data": dict with file paths to processed NetCDF data.
      :rtype: dict

      :raises Exception: If an error occurs during download or processing, such as invalid input parameters
          or file system issues.

      .. rubric:: Notes

      This is a high-level method that internally calls `_download()` and `_process()`.
      The file structure and naming follow the configuration defined in `get_pipeline_path`.



   .. py:method:: calculate_index(overwrite=False, hw_threshold=27, hw_min_duration=3, hw_max_gap=0, tr_threshold=20)

      Calculate the specified climate index based on the downloaded forecast data.

      This function processes the downloaded or processed forecast data to compute
      the selected climate index (e.g., Heatwave days, Tropical Nights) according
      to the parameters defined for the index.

      :param overwrite: If True, existing index files will be overwritten. Default is False.
      :type overwrite: bool, optional
      :param hw_threshold: Temperature threshold for heatwave days index calculation. Default is 27°C.
      :type hw_threshold: float, optional
      :param hw_min_duration: Minimum duration (in days) of consecutive conditions for a heatwave event. Default is 3.
      :type hw_min_duration: int, optional
      :param hw_max_gap: Maximum allowable gap (in days) between conditions to still
                         consider as a single heatwave event. Default is 0.
      :type hw_max_gap: int, optional
      :param tr_threshold: Temperature threshold for tropical nights index calculation. Default is 20°C.
      :type tr_threshold: float, optional

      :returns: Dictionary with keys of the form "<year>_init<month>_valid<valid_period>"
                and values corresponding to the output NetCDF index files (daily, monthly, stats).
      :rtype: dict

      :raises Exception: If index calculation fails due to missing files or processing errors.

      .. rubric:: Notes

      The input files used depend on the index:
      - For 'TX30', 'TR', and 'HW', the raw downloaded GRIB data is used.
      - For other indices, the processed NetCDF data is used.

      The calculation is performed using the `_calculate_index` function and results
      are saved in the configured output directory structure.



   .. py:method:: save_index_to_hazard(overwrite=False)

      Convert the calculated climate index to a CLIMADA Hazard object and save it as HDF5.

      This function reads the monthly aggregated index NetCDF files and converts them
      into a CLIMADA Hazard object. The resulting hazard files are saved in HDF5 format.

      :param overwrite: If True, existing hazard files will be overwritten. Default is False.
      :type overwrite: bool, optional

      :returns: Dictionary with keys of the form "<year>_init<month>_valid<valid_period>"
                and values corresponding to the saved Hazard HDF5 file paths.
      :rtype: dict

      :raises Exception: If the hazard conversion fails due to missing input files or processing errors.

      .. rubric:: Notes

      The hazard conversion is performed using the `_convert_to_hazard` function.
      The function expects that the index files (monthly NetCDF) have already been
      calculated and saved using `calculate_index()`.

      The resulting Hazard objects follow CLIMADA's internal structure and can be
      used for further risk assessment workflows.



.. py:function:: handle_overwriting(function)

   Decorator to handle file overwriting during data processing.

   This decorator checks if the target output file(s) already exist and
   whether overwriting is allowed. If the file(s) exist and overwriting
   is disabled, the existing file paths are returned without executing
   the decorated function.

   :param function: Function to be decorated. Must have the first two arguments:
                    - output_file_name : Path or dict of Path
                    - overwrite : bool
   :type function: callable

   :returns: Wrapped function with added file existence check logic.
   :rtype: callable

   .. rubric:: Notes

   - If `output_file_name` is a `Path`, its existence is checked.
   - If `output_file_name` is a `dict` of `Path`, the existence of any file is checked.
   - If `overwrite` is False and the file(s) exist, the function is skipped and the
     existing path(s) are returned.
   - The function must accept `overwrite` as the second argument.


