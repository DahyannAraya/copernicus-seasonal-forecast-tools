seasonal_forecast_tools
=======================

.. py:module:: seasonal_forecast_tools

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

   init Copernicus seasonal forecast tools



Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/seasonal_forecast_tools/core/index
   /autoapi/seasonal_forecast_tools/data/index
   /autoapi/seasonal_forecast_tools/utils/index


Attributes
----------

.. autoapisummary::

   seasonal_forecast_tools.CLIMADA_INSTALLED
   seasonal_forecast_tools.DATA_OUT
   seasonal_forecast_tools.LOGGER
   seasonal_forecast_tools.LOGGER
   seasonal_forecast_tools.HI_COEFFS
   seasonal_forecast_tools.HI_ADJUSTED_COEFFS
   seasonal_forecast_tools.LOGGER
   seasonal_forecast_tools.BASE_DATA_DIR
   seasonal_forecast_tools.SEASONAL_FORECAST_DIR


Classes
-------

.. autoapisummary::

   seasonal_forecast_tools.ClimateIndex
   seasonal_forecast_tools.SeasonalForecast
   seasonal_forecast_tools.IndexSpec
   seasonal_forecast_tools.ClimateIndex


Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.download_data
   seasonal_forecast_tools.get_short_name_from_variable
   seasonal_forecast_tools.get_file_path
   seasonal_forecast_tools.calculate_leadtimes
   seasonal_forecast_tools.month_name_to_number
   seasonal_forecast_tools.handle_overwriting
   seasonal_forecast_tools._download_data
   seasonal_forecast_tools._process_data
   seasonal_forecast_tools._calculate_index
   seasonal_forecast_tools._convert_to_hazard
   seasonal_forecast_tools.kelvin_to_fahrenheit
   seasonal_forecast_tools.fahrenheit_to_kelvin
   seasonal_forecast_tools.fahrenheit_to_celsius
   seasonal_forecast_tools.celsius_to_kelvin
   seasonal_forecast_tools.kelvin_to_celsius
   seasonal_forecast_tools.calculate_relative_humidity
   seasonal_forecast_tools.calculate_humidex
   seasonal_forecast_tools.calculate_heat_index_simplified
   seasonal_forecast_tools.calculate_heat_index_adjusted
   seasonal_forecast_tools.calculate_wind_speed
   seasonal_forecast_tools.calculate_apparent_temperature
   seasonal_forecast_tools.calculate_nonsaturation_vapour_pressure
   seasonal_forecast_tools.calculate_wbgt_simple
   seasonal_forecast_tools.calculate_heat_index
   seasonal_forecast_tools.calculate_tr
   seasonal_forecast_tools.calculate_tx30
   seasonal_forecast_tools.calculate_hw_1D
   seasonal_forecast_tools.calculate_hw
   seasonal_forecast_tools.get_short_name_from_variable
   seasonal_forecast_tools.kelvin_to_celsius
   seasonal_forecast_tools.calculate_heat_indices_metrics
   seasonal_forecast_tools._monthly_periods_from_valid_times
   seasonal_forecast_tools.calculate_monthly_dataset
   seasonal_forecast_tools.calculate_statistics_from_index
   seasonal_forecast_tools.download_data
   seasonal_forecast_tools.month_name_to_number
   seasonal_forecast_tools.calculate_leadtimes
   seasonal_forecast_tools.month_name_to_number
   seasonal_forecast_tools.get_file_path
   seasonal_forecast_tools.check_existing_files
   seasonal_forecast_tools.bounding_box_from_cardinal_bounds
   seasonal_forecast_tools.bounding_box_global
   seasonal_forecast_tools.bounding_box_from_countries


Package Contents
----------------

.. py:data:: CLIMADA_INSTALLED
   :value: True


.. py:function:: download_data(dataset, params, filename=None, datastore_url=None, overwrite=False)

   Download data from Copernicus Data Stores (e.g., cds.climate.copernicus.eu,
   ads.atmosphere.copernicus.eu and ewds.climate.copernicus.eu) using specified dataset type and parameters.

   :param dataset: The dataset to retrieve (e.g., 'seasonal-original-single-levels', 'sis-heat-and-cold-spells').
   :type dataset: str
   :param params: Dictionary containing the parameters for the CDS API call (e.g., variables, time range, area).
                  To see which parameters are requested for the given dataset, go to the copernicus website of the dataset in the "download" tab,
                  tick all required parameter choices. You find the params dicts as "request" dict in the "API request" section.
   :type params: dict
   :param filename: Full path and filename where the downloaded data will be stored. If None, data will be saved with the filename as suggested by the data store. Defaults to None.
   :type filename: pathlib.Path or str
   :param datastore_url: Url of the Copernicus data store to be accessed. If None, the url of the .cdsapirc file is used. Defaults to None.
   :type datastore_url: str
   :param overwrite: If True, overwrite the file if it already exists. If False, skip downloading
                     if the file is already present. The default is False.
   :type overwrite: bool, optional

   :returns: Path to the downloaded file if the download was successfull.
   :rtype: Path

   :raises FileNotFoundError: Raised if the download attempt fails and the file is not found at the specified location.
   :raises Exception: Raised for any other error during the download process, with further details corresponding to typical errors.


.. py:class:: ClimateIndex

   Bases: :py:obj:`enum.Enum`


   Generic enumeration.

   Derive from this class to define new enumerations.


   .. py:attribute:: HIA


   .. py:attribute:: HIS


   .. py:attribute:: Tmean


   .. py:attribute:: Tmin


   .. py:attribute:: Tmax


   .. py:attribute:: HW


   .. py:attribute:: TR


   .. py:attribute:: TX30


   .. py:attribute:: RH


   .. py:attribute:: HUM


   .. py:attribute:: AT


   .. py:attribute:: WBGT


   .. py:method:: by_name(index_name: str)
      :classmethod:


      Retrieve the complete information for a specified index.

      :param index_name: The name of the index (e.g., "HIA", "HIS", "Tmean").
      :type index_name: str

      :returns: Returns an instance of IndexSpec containing all relevant information.
                Raises a ValueError if the index is not found.
      :rtype: IndexSpec



   .. py:method:: from_input(arg)
      :staticmethod:


      Returns proper IndexSpec object from whatever input is valid



.. py:function:: get_short_name_from_variable(variable)

   Retrieve the short name of a variable within an index based on its standard name.

   :param variable: The standard name of the climate variable (e.g., "2m_temperature",
                    "10m_u_component_of_wind").
   :type variable: str

   :returns: The short name corresponding to the specified climate variable (e.g., "t2m" for
             "2m_temperature").
             Returns None if the variable is not recognized.
   :rtype: str or None

   .. rubric:: Notes

   This function maps specific variable names to their short names, which are used across
   climate index definitions. These mappings are independent of the indices themselves
   but provide consistent naming conventions for variable processing and file management.

   .. rubric:: Examples

   >>> get_short_name_from_variable("2m_temperature")
   't2m'

   >>> get_short_name_from_variable("10m_u_component_of_wind")
   'u10'

   >>> get_short_name_from_variable("unknown_variable")
   None


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


.. py:function:: calculate_leadtimes(year, initiation_month, valid_period)

   Calculate forecast lead times (in hours) between initiation and valid period.

   :param year: Forecast initiation year.
   :type year: int
   :param initiation_month: Month when the forecast starts, as integer (1–12) or full month name.
   :type initiation_month: int or str
   :param valid_period: Two-element list specifying the start and end months of the forecast period,
                        either as integers or full month names (e.g., ['December', 'February']).
   :type valid_period: list of int or str

   :returns: List of lead times in hours (spaced every 6 hours) from initiation date
             to the end of the valid period.
   :rtype: list of int

   :raises ValueError: If input months are invalid or misordered.

   .. rubric:: Notes

   - If the valid period crosses a calendar year (e.g., Dec–Feb), it is handled correctly.
   - Lead times are counted from the first day of the initiation month.
   - The list includes all time steps in 6-hour intervals until the end of the valid period.

   .. rubric:: Examples

   calculate_leadtimes(2022, "November", ["December", "February"])
   [720, 726, 732, ..., 2184]


.. py:function:: month_name_to_number(month)

   Convert a month name or number to its corresponding integer value.

   Accepts either an integer (1-12), full month name (e.g., 'March'),
   or abbreviated month name (e.g., 'Mar') and returns the corresponding
   month number (1-12).

   :param month: Month as an integer (1-12) or as a string (full or abbreviated month name).
   :type month: int or str

   :returns: Month as an integer in the range 1-12.
   :rtype: int

   :raises ValueError: If the input month is invalid, empty, or outside the valid range.


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



   .. py:method:: _download(overwrite=False)

      Download seasonal forecast data for the specified years and initiation months.

      This function downloads the raw forecast data files for each year and initiation month
      defined in the instance configuration. The data is downloaded in the specified format
      ('grib' or 'netcdf') and stored in the configured directory structure.

      :param overwrite: If True, existing downloaded files will be overwritten. Default is False.
      :type overwrite: bool, optional

      :returns: Dictionary with keys of the form "<year>_init<month>_valid<valid_period>"
                and values corresponding to the downloaded data file paths.
      :rtype: dict

      .. rubric:: Notes

      The data is downloaded using the `_download_data` function and follows the directory
      structure defined in `get_pipeline_path`. The bounding box is automatically converted
      to CDS (Climate Data Store) format before download.



   .. py:method:: _process(overwrite=False)

      Process the downloaded forecast data into daily NetCDF format.

      This function processes the raw downloaded data files into a standardized
      daily NetCDF format, applying basic aggregation operations (mean, max, min).
      The processed files are saved in the configured output directory.

      :param overwrite: If True, existing processed files will be overwritten. Default is False.
      :type overwrite: bool, optional

      :returns: Dictionary with keys of the form "<year>_init<month>_valid<valid_period>"
                and values corresponding to the processed NetCDF file paths.
      :rtype: dict

      .. rubric:: Notes

      The processing applies a daily coarsening operation and aggregates the data.
      The processed data is saved in NetCDF format in the directory defined by
      `get_pipeline_path`. Processing is performed using the `_process_data` function.



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


.. py:function:: _download_data(output_file_name, overwrite, variables, year, initiation_month, data_format, originating_centre, system, bounds_cds_order, leadtimes)

   Download seasonal forecast data for a specific year and initiation month.

   This function downloads raw seasonal forecast data from the Copernicus
   Climate Data Store (CDS) based on the specified forecast configuration
   and geographical domain. The data is saved in the specified format and
   location.

   :param output_file_name: Path to save the downloaded data file.
   :type output_file_name: Path
   :param overwrite: If True, existing files will be overwritten. If False and the file exists,
                     the download is skipped.
   :type overwrite: bool
   :param variables: List of variable names to download (e.g., ['tasmax', 'tasmin']).
   :type variables: list of str
   :param year: Year of the forecast initiation.
   :type year: int
   :param initiation_month: Month of the forecast initiation (1-12).
   :type initiation_month: int
   :param data_format: File format for the downloaded data ('grib' or 'netcdf').
   :type data_format: str
   :param originating_centre: Forecast data provider (e.g., 'dwd' for German Weather Service).
   :type originating_centre: str
   :param system: Model system identifier (e.g., '21').
   :type system: str
   :param bounds_cds_order: Geographical bounding box in CDS order: [north, west, south, east].
   :type bounds_cds_order: list of float
   :param leadtimes: List of forecast lead times in hours.
   :type leadtimes: list of int

   :returns: Path to the downloaded data file.
   :rtype: Path

   .. rubric:: Notes

   The function uses the `download_data` method from the Copernicus interface module.
   The downloaded data is stored following the directory structure defined by the pipeline.


.. py:function:: _process_data(output_file_name, overwrite, input_file_name, variables, data_format)

   Process a downloaded forecast data file into daily NetCDF format.

   This function reads the downloaded forecast data (in GRIB or NetCDF format),
   applies a temporal coarsening operation (aggregation over 4 time steps),
   and saves the resulting daily data as a NetCDF file. For each variable,
   daily mean, maximum, and minimum values are computed.

   If data_format == "netcdf", any existing “forecast_period” dimension
   is first renamed to “step” so that the Xarray coarsen( step=… ) call works.
   Note that NetCDF format is still experimental; see the CDS documentation
   for details. In contrast, GRIB files (opened with engine="cfgrib") already
   include a step dimension, so no renaming is required.

   :param output_file_name: Path to save the processed NetCDF file.
   :type output_file_name: Path
   :param overwrite: If True, existing processed files will be overwritten. If False and the file exists,
                     the processing is skipped.
   :type overwrite: bool
   :param input_file_name: Path to the input downloaded data file.
   :type input_file_name: Path
   :param variables: List of short variable names to process (e.g., ['tasmax', 'tasmin']).
   :type variables: list of str
   :param data_format: Format of the input file ('grib' or 'netcdf').
   :type data_format: str

   :returns: Path to the saved processed NetCDF file.
   :rtype: Path

   :raises FileNotFoundError: If the input file does not exist.
   :raises Exception: If an error occurs during data processing.

   .. rubric:: Notes

   The function performs a temporal aggregation by coarsening the data over 4 time steps,
   resulting in daily mean, maximum, and minimum values for each variable.
   The processed data is saved in NetCDF format and can be used for index calculation.


.. py:function:: _calculate_index(output_file_names, overwrite, input_file_name, index_metric, tr_threshold=20, hw_threshold=27, hw_min_duration=3, hw_max_gap=0)

   Calculate and save climate indices based on the input data.

   :param output_file_names: Dictionary containing paths for daily, monthly, and stats output files.
   :type output_file_names: dict
   :param overwrite: Whether to overwrite existing files.
   :type overwrite: bool
   :param input_file_name: Path to the input file.
   :type input_file_name: Path
   :param index_metric: Climate index to calculate (e.g., 'HW', 'TR').
   :type index_metric: str
   :param threshold: Threshold for the index calculation (specific to the index type).
   :type threshold: float, optional
   :param min_duration: Minimum duration for events (specific to the index type).
   :type min_duration: int, optional
   :param max_gap: Maximum gap allowed between events (specific to the index type).
   :type max_gap: int, optional
   :param tr_threshold: Threshold for tropical nights (specific to the 'TR' index).
   :type tr_threshold: float, optional

   :returns: Paths to the saved index files.
   :rtype: dict


.. py:function:: _convert_to_hazard(output_file_name, overwrite, input_file_name, index_metric)

   Convert a climate index file to a CLIMADA Hazard object and save it as HDF5.

   This function reads a processed climate index NetCDF file, converts it to a
   CLIMADA Hazard object, and saves it in HDF5 format. The function supports
   ensemble members and concatenates them into a single Hazard object.

   :param output_file_name: Path to save the generated Hazard HDF5 file.
   :type output_file_name: Path
   :param overwrite: If True, existing hazard files will be overwritten. If False and the file exists,
                     the conversion is skipped.
   :type overwrite: bool
   :param input_file_name: Path to the input NetCDF file containing the calculated climate index.
   :type input_file_name: Path
   :param index_metric: Climate index metric used for hazard creation (e.g., 'HW', 'TR', 'Tmax').
   :type index_metric: str

   :returns: Path to the saved Hazard HDF5 file.
   :rtype: Path

   :raises KeyError: If required variables (e.g., 'step' or index variable) are missing in the dataset.
   :raises Exception: If the hazard conversion process fails.

   .. rubric:: Notes

   - The function uses `Hazard.from_xarray_raster()` to create Hazard objects
     from the input dataset.
   - If multiple ensemble members are present, individual Hazard objects are
     created for each member and concatenated.
   - The function determines the intensity unit based on the selected index:
       - '%' for relative humidity (RH)
       - 'days' for duration indices (e.g., 'HW', 'TR', 'TX30')
       - '°C' for temperature indices


.. py:data:: LOGGER

.. py:function:: kelvin_to_fahrenheit(kelvin)

.. py:function:: fahrenheit_to_kelvin(fahrenheit)

.. py:function:: fahrenheit_to_celsius(fahrenheit)

.. py:function:: celsius_to_kelvin(temp_c)

.. py:function:: kelvin_to_celsius(temp_k)

.. py:function:: calculate_relative_humidity(t2k, tdk, as_percentage=True)

   Calculates the relative humidity with the option to return it either as a decimal value (0-1) or as a percentage (0-100).

   :param t2k: 2-meter air temperature in Kelvin.
   :type t2k: float or array-like
   :param tdk: 2-meter dew point temperature in Kelvin.
   :type tdk: float or array-like
   :param as_percentage: If True, returns relative humidity as a percentage (0-100). If False, returns it as a fraction (0-1).
                         Default is True.
   :type as_percentage: bool, optional

   :returns: Relative humidity as a percentage (0-100) or as a decimal value (0-1), depending on the `as_percentage` setting.
   :rtype: float or array-like


.. py:function:: calculate_humidex(t2_k, td_k)

   Calculate Humidex (°C)
   The Humidex is a thermal comfort index that represents the perceived temperature
   by incorporating both air temperature and humidity. It is commonly used in
   meteorology to assess heat stress and human discomfort in warm and humid conditions.
   The higher the Humidex value, the greater the level of discomfort.

   :param t2_k: 2m temperature in Kelvin.
   :type t2_k: float or np.array
   :param td_k: Dew point temperature in Kelvin.
   :type td_k: float or np.array

   :returns: * *float or np.array* -- Humidex in Celsius.
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices library. *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005*)


.. py:data:: HI_COEFFS

.. py:data:: HI_ADJUSTED_COEFFS

.. py:function:: calculate_heat_index_simplified(t2k, tdk)

   Calculates the simplified heat index (HIS) based on temperature and dewpoint temperature.

   The simplified heat index formula is **only valid for temperatures above 20°C**,
   as the heat index is specifically designed for **warm to hot conditions** where
   humidity significantly influences perceived temperature. Below 20°C, the function
   returns the actual air temperature instead of applying the heat index formula.

   The heat index is an empirical measure that estimates the **perceived temperature**
   by incorporating the effects of both temperature and humidity. It is commonly used
   in meteorology and climate studies to assess heat stress.

   :param t2k: 2-meter air temperature in Kelvin. This is used for consistency with
               climate datasets and numerical weather models.
   :type t2k: float or array-like
   :param tdk: 2-meter dewpoint temperature in Kelvin.
   :type tdk: float or array-like

   :returns: * *float or array-like* -- Simplified heat index in degrees Celsius, representing how hot it feels
               to the human body by accounting for both temperature and relative humidity.
             * *Formula*
             * *-------*
             * *If T > 20°C* -- HI = c1 + c2*T + c3*RH + c4*T*RH + c5*T² + c6*RH² + c7*T²*RH + c8*T*RH² + c9*T²*RH²
             * *Otherwise* -- HI = T (air temperature in °C)
             * *where* --

               - T = air temperature in °C
               - RH = relative humidity in %
               - c1, c2, ..., c9 are empirical coefficients (Rothfusz regression).
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology*
             * *can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices*)
             * **library. *SoftwareX*, 17, 101005. DOI** (*https://doi.org/10.1016/j.softx.2022.101005*)


.. py:function:: calculate_heat_index_adjusted(t2k, tdk)

   Calculates the adjusted heat index based on temperature and dewpoint temperature.

   This function refines the standard heat index calculation by incorporating adjustments
   for extreme values of temperature and relative humidity. The adjustments improve accuracy
   in conditions where the simplified formula may not be sufficient, particularly for
   high temperatures (> 80°F / ~27°C) and very low or high humidity levels.

   :param t2k: 2-meter air temperature in Kelvin. This is used for consistency with
               climate datasets and numerical weather models.
   :type t2k: float or array-like
   :param tdk: 2-meter dewpoint temperature in Kelvin.
   :type tdk: float or array-like

   :returns: * *float or array-like* -- Adjusted heat index in degrees Celsius, representing how hot it feels
               to the human body by accounting for both temperature and relative humidity.
             * *Formula*
             * *-------*
             * *If T > 80°F (~27°C)* -- HI = c1 + c2*T + c3*RH + c4*T*RH + c5*T² + c6*RH² + c7*T²*RH + c8*T*RH² + c9*T²*RH²
               + adjustments based on extreme humidity conditions.
             * *Otherwise* -- HI = 0.5 * (T + 61 + ((T - 68) * 1.2) + (RH * 0.094))
             * *where* --

               - T = air temperature in °F
               - RH = relative humidity in %
               - c1, c2, ..., c9 are empirical coefficients (Rothfusz regression).
             * *Adjustments* --

               - If RH ≤ 13% and 80°F < T < 112°F:
                   Adjustment = (13 - RH) / 4 * sqrt((17 - |T - 95|) / 17)
               - If RH > 85% and T < 87°F:
                   Adjustment = (RH - 85) / 10 * ((87 - T) / 5)

   .. rubric:: Notes

   - If T ≤ 26.7°C (80°F), the function returns a simplified index.
   - If T > 26.7°C (80°F), additional corrections are applied to refine the heat index value.
   - **Very low humidity** is defined as RH ≤ 13%, where a correction is subtracted if 80°F < T < 112°F.
   - **Very high humidity** is defined as RH > 85%, where a correction is added if T < 87°F.

   .. rubric:: References

   Brimicombe, C., Bröde, P., & Calvi, P. (2022). Thermofeel: A python thermal comfort indices library.
   *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005


.. py:function:: calculate_wind_speed(u10, v10)

   Calculate wind speed (m/s) from the u and v components of the wind.

   :param u10: 10m eastward wind component in m/s.
   :type u10: float or np.array
   :param v10: 10m northward wind component in m/s.
   :type v10: float or np.array

   :returns: * *float or np.array* -- Wind speed in m/s.
             * *Acknowledgment*
             * *--------------*
             * **This function is based on ECMWF (European Centre for Medium-Range Weather Forecasts) documentation for wind calculations https** (*//confluence.ecmwf.int/pages/viewpage.action?pageId=133262398*)


.. py:function:: calculate_apparent_temperature(t2_k, u10, v10, tdk)

   Calculate Apparent Temperature (°C)

   :param t2_k: 2m temperature in Kelvin. Represents the air temperature measured at a height of 2 meters.
   :type t2_k: float or np.array
   :param u10: 10m eastward wind component in m/s. Indicates the wind speed in the eastward direction at a height of 10 meters.
   :type u10: float or np.array
   :param v10: 10m northward wind component in m/s. Indicates the wind speed in the northward direction at a height of 10 meters.
   :type v10: float or np.array
   :param tdk: 2m dewpoint temperature in Kelvin. Dew point temperature at which air becomes saturated and condensation begins.
   :type tdk: float or np.array

   :returns: * *float or np.array* -- Apparent temperature in Celsius. This metric represents the perceived temperature considering both wind speed and humidity, accounting for heat loss or gain due to environmental factors.
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices library. *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005*)


.. py:function:: calculate_nonsaturation_vapour_pressure(t2_k, rh)

   Calculate Non-Saturated Vapour Pressure (hPa)

   :param t2_k: 2m temperature in Kelvin. Represents the temperature measured at 2 meters above ground level.
   :type t2_k: float or np.array
   :param rh: Relative humidity as a percentage. Indicates the amount of moisture present in the air relative to the maximum it can hold.
   :type rh: float or np.array

   :returns: * *float or np.array* -- Non-saturated vapour pressure in hPa (equivalent to mBar). This pressure reflects the partial pressure of water vapor in air under non-saturated conditions.
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices library. *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005*)


.. py:function:: calculate_wbgt_simple(t2_k, tdk)

   Calculate Wet Bulb Globe Temperature (Simple)

   :param t2_k: 2m temperature in Kelvin. This is the standard air temperature measured at a height of 2 meters.
   :type t2_k: float or np.array
   :param tdk: Dew point temperature in Kelvin. Used to calculate relative humidity and overall heat stress.
   :type tdk: float or np.array

   :returns: * *float or np.array* -- Wet Bulb Globe Temperature in Celsius. This index is used for heat stress assessments, combining temperature, humidity, and other factors to determine the perceived heat risk.
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices library. *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005*)


.. py:function:: calculate_heat_index(da_t2k, da_tdk, index)

   Calculates the heat index based on temperature and dewpoint temperature using
   either the simplified or adjusted formula as implemented in the Thermofeel library.

   :param da_t2k: 2-meter air temperature in Kelvin. This value represents the air temperature measured at a height of 2 meters above ground level.
   :type da_t2k: xarray.DataArray
   :param da_tdk: 2-meter dewpoint temperature in Kelvin. The dewpoint temperature is the temperature at which the air becomes saturated and condensation begins.
   :type da_tdk: xarray.DataArray
   :param index: Identifier for the type of heat index to calculate. Options are:
                 - "HIS": Heat Index Simplified.
                 - "HIA": Heat Index Adjusted.
   :type index: str

   :returns: * *xarray.DataArray* -- The calculated heat index in degrees Celsius, represented as an `xarray.DataArray` with the same dimensions and coordinates as the input data. It includes the heat index values along with relevant metadata, such as units and a description.
             * *Acknowledgment*
             * *--------------*
             * *This function is based on the Thermofeel library. The original implementation and methodology can be found in*
             * **Brimicombe, C., Bröde, P., and Calvi, P. (2022). Thermofeel** (*A python thermal comfort indices library. *SoftwareX*, 17, 101005. DOI: https://doi.org/10.1016/j.softx.2022.101005*)


.. py:function:: calculate_tr(temperature_data, tr_threshold=20)

   Calculate the Tropical Nights index, defined as the number of nights with minimum temperature above a given threshold.

   :param temperature_data: DataArray containing daily minimum temperatures in Celsius.
   :type temperature_data: xarray.DataArray
   :param tr_threshold: Temperature threshold in Celsius for a tropical night. Default is 20°C.
   :type tr_threshold: float, optional

   :returns: Boolean DataArray where True indicates nights with Tmin > threshold.
   :rtype: xarray.DataArray


.. py:function:: calculate_tx30(temperature_data, threshold=30)

   Calculate TX30, the number of days with maximum temperature above the given threshold (default is 30°C).

   :param temperature_data: DataArray containing daily maximum temperatures in Celsius. Can be from any dataset, not specific to seasonal forecasts.
   :type temperature_data: xarray.DataArray
   :param threshold: Temperature threshold in Celsius for a TX30 day. Default is 30°C.
   :type threshold: float, optional

   :returns: Boolean DataArray where True indicates days where Tmax > threshold.
   :rtype: xarray.DataArray


.. py:function:: calculate_hw_1D(temperatures: numpy.ndarray, threshold: float = 27, min_duration: int = 3, max_gap: int = 0) -> list

   Identify and define heatwave events based on a sequence of daily temperatures.

   This function scans an array of temperature data to detect periods of heatwaves,
   defined as consecutive days where temperatures exceed a given threshold for a minimum duration.
   If two such periods are separated by days with temperatures below the threshold but within a specified maximum gap,
   they are merged into one continuous heatwave event.

   :param temperatures: Array of daily temperatures.
   :type temperatures: np.ndarray
   :param threshold: Temperature threshold above which days are considered part of a heatwave. Default is 27°C.
   :type threshold: float, optional
   :param min_duration: Minimum number of consecutive days required to define a heatwave event. Default is 3 days.
   :type min_duration: int, optional
   :param max_gap: Maximum allowed gap (in days) of below-threshold temperatures to merge two consecutive heatwave events into one. Default is 0 days.
   :type max_gap: int, optional

   :returns: * *np.ndarray*
             * A binary mask (1D array) of the same length as `temperatures`, where
             * - `1` indicates a heatwave day.
             * - `0` indicates a non-heatwave day.

   Acknowledgment
   --------------
   Adapted from Modelling marine heatwaves impact on shallow and upper mesophotic tropical coral reefs DOI:10.1088/1748-9326/ad89df


.. py:function:: calculate_hw(daily_mean_temp, threshold: float = 27, min_duration: int = 3, max_gap: int = 0, label_time_step='step')

   Identify and define heatwave events based on a sequence of daily mean temperatures.

   This function detects heatwave events by applying a threshold-based approach to
   an xarray DataArray of daily mean temperatures. A heatwave is defined as a period
   where temperatures exceed a specified threshold for a minimum number of consecutive days.
   If two such periods are separated by a gap of below-threshold temperatures within
   a given maximum gap length, they are merged into a single heatwave event.

   :param daily_mean_temp: An xarray DataArray containing daily mean temperatures. The time dimension should be labeled
                           according to `label_time_step`.
   :type daily_mean_temp: xarray.DataArray
   :param threshold: Temperature threshold above which days are considered part of a heatwave. Default is 27°C.
   :type threshold: float, optional
   :param min_duration: Minimum number of consecutive days required to define a heatwave event. Default is 3 days.
   :type min_duration: int, optional
   :param max_gap: Maximum allowed gap (in days) of below-threshold temperatures to merge two consecutive
                   heatwave events into one. Default is 0 days.
   :type max_gap: int, optional
   :param label_time_step: Name of the time dimension in `daily_mean_temp`. Default is "step".
   :type label_time_step: str, optional

   :returns: A DataArray of the same shape as `daily_mean_temp`, where heatwave periods
             are labeled with 1 (heatwave) and 0 (non-heatwave).
   :rtype: xarray.DataArray

   .. rubric:: Notes

   This function leverages `xarray.apply_ufunc` to apply the `calculate_hw_1D` function
   efficiently across all grid points, supporting vectorized operations and parallelized
   computation with Dask.


.. py:class:: IndexSpec

   .. py:attribute:: unit
      :type:  str


   .. py:attribute:: full_name
      :type:  str


   .. py:attribute:: explanation
      :type:  str


   .. py:attribute:: variables
      :type:  list


.. py:class:: ClimateIndex

   Bases: :py:obj:`enum.Enum`


   Generic enumeration.

   Derive from this class to define new enumerations.


   .. py:attribute:: HIA


   .. py:attribute:: HIS


   .. py:attribute:: Tmean


   .. py:attribute:: Tmin


   .. py:attribute:: Tmax


   .. py:attribute:: HW


   .. py:attribute:: TR


   .. py:attribute:: TX30


   .. py:attribute:: RH


   .. py:attribute:: HUM


   .. py:attribute:: AT


   .. py:attribute:: WBGT


   .. py:method:: by_name(index_name: str)
      :classmethod:


      Retrieve the complete information for a specified index.

      :param index_name: The name of the index (e.g., "HIA", "HIS", "Tmean").
      :type index_name: str

      :returns: Returns an instance of IndexSpec containing all relevant information.
                Raises a ValueError if the index is not found.
      :rtype: IndexSpec



   .. py:method:: from_input(arg)
      :staticmethod:


      Returns proper IndexSpec object from whatever input is valid



.. py:function:: get_short_name_from_variable(variable)

   Retrieve the short name of a variable within an index based on its standard name.

   :param variable: The standard name of the climate variable (e.g., "2m_temperature",
                    "10m_u_component_of_wind").
   :type variable: str

   :returns: The short name corresponding to the specified climate variable (e.g., "t2m" for
             "2m_temperature").
             Returns None if the variable is not recognized.
   :rtype: str or None

   .. rubric:: Notes

   This function maps specific variable names to their short names, which are used across
   climate index definitions. These mappings are independent of the indices themselves
   but provide consistent naming conventions for variable processing and file management.

   .. rubric:: Examples

   >>> get_short_name_from_variable("2m_temperature")
   't2m'

   >>> get_short_name_from_variable("10m_u_component_of_wind")
   'u10'

   >>> get_short_name_from_variable("unknown_variable")
   None


.. py:function:: kelvin_to_celsius(temp_k)

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


.. py:function:: _monthly_periods_from_valid_times(ds)

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


.. py:function:: download_data(dataset, params, filename=None, datastore_url=None, overwrite=False)

   Download data from Copernicus Data Stores (e.g., cds.climate.copernicus.eu,
   ads.atmosphere.copernicus.eu and ewds.climate.copernicus.eu) using specified dataset type and parameters.

   :param dataset: The dataset to retrieve (e.g., 'seasonal-original-single-levels', 'sis-heat-and-cold-spells').
   :type dataset: str
   :param params: Dictionary containing the parameters for the CDS API call (e.g., variables, time range, area).
                  To see which parameters are requested for the given dataset, go to the copernicus website of the dataset in the "download" tab,
                  tick all required parameter choices. You find the params dicts as "request" dict in the "API request" section.
   :type params: dict
   :param filename: Full path and filename where the downloaded data will be stored. If None, data will be saved with the filename as suggested by the data store. Defaults to None.
   :type filename: pathlib.Path or str
   :param datastore_url: Url of the Copernicus data store to be accessed. If None, the url of the .cdsapirc file is used. Defaults to None.
   :type datastore_url: str
   :param overwrite: If True, overwrite the file if it already exists. If False, skip downloading
                     if the file is already present. The default is False.
   :type overwrite: bool, optional

   :returns: Path to the downloaded file if the download was successfull.
   :rtype: Path

   :raises FileNotFoundError: Raised if the download attempt fails and the file is not found at the specified location.
   :raises Exception: Raised for any other error during the download process, with further details corresponding to typical errors.


.. py:function:: month_name_to_number(month)

   Convert a month name or number to its corresponding integer value.

   Accepts either an integer (1-12), full month name (e.g., 'March'),
   or abbreviated month name (e.g., 'Mar') and returns the corresponding
   month number (1-12).

   :param month: Month as an integer (1-12) or as a string (full or abbreviated month name).
   :type month: int or str

   :returns: Month as an integer in the range 1-12.
   :rtype: int

   :raises ValueError: If the input month is invalid, empty, or outside the valid range.


.. py:function:: calculate_leadtimes(year, initiation_month, valid_period)

   Calculate forecast lead times (in hours) between initiation and valid period.

   :param year: Forecast initiation year.
   :type year: int
   :param initiation_month: Month when the forecast starts, as integer (1–12) or full month name.
   :type initiation_month: int or str
   :param valid_period: Two-element list specifying the start and end months of the forecast period,
                        either as integers or full month names (e.g., ['December', 'February']).
   :type valid_period: list of int or str

   :returns: List of lead times in hours (spaced every 6 hours) from initiation date
             to the end of the valid period.
   :rtype: list of int

   :raises ValueError: If input months are invalid or misordered.

   .. rubric:: Notes

   - If the valid period crosses a calendar year (e.g., Dec–Feb), it is handled correctly.
   - Lead times are counted from the first day of the initiation month.
   - The list includes all time steps in 6-hour intervals until the end of the valid period.

   .. rubric:: Examples

   calculate_leadtimes(2022, "November", ["December", "February"])
   [720, 726, 732, ..., 2184]


.. py:function:: month_name_to_number(month)

   Convert a month name or number to its corresponding integer value.

   Accepts either an integer (1-12), full month name (e.g., 'March'),
   or abbreviated month name (e.g., 'Mar') and returns the corresponding
   month number (1-12).

   :param month: Month as an integer (1-12) or as a string (full or abbreviated month name).
   :type month: int or str

   :returns: Month as an integer in the range 1-12.
   :rtype: int

   :raises ValueError: If the input month is invalid, empty, or outside the valid range.


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


.. py:function:: bounding_box_from_cardinal_bounds(north: float, south: float, east: float, west: float) -> Tuple[float, float, float, float]

   Return a bounding box tuple from cardinal directions.

   :param north: Geographic bounds.
   :type north: float
   :param south: Geographic bounds.
   :type south: float
   :param east: Geographic bounds.
   :type east: float
   :param west: Geographic bounds.
   :type west: float

   :returns: (lon_min, lat_min, lon_max, lat_max)
   :rtype: tuple


.. py:function:: bounding_box_global() -> Tuple[float, float, float, float]

   Return a bounding box covering the entire globe.

   :returns: (-180.0, -90.0, 180.0, 90.0)
   :rtype: tuple


.. py:function:: bounding_box_from_countries(countries: List[str], buffer: float = 1.0) -> Tuple[float, float, float, float]

   Return bounding box for a list of countries using Natural Earth data via Cartopy, with optional buffer.

   :param countries: List of ISO-3 country codes (e.g., ['CHE', 'FRA']).
   :type countries: list of str
   :param buffer: Buffer to add to all sides of the bounding box (in degrees). Default is 1.0.
   :type buffer: float, optional

   :returns: (lon_min, lat_min, lon_max, lat_max)
   :rtype: tuple

   :raises ValueError: If no matching countries are found.


.. py:data:: BASE_DATA_DIR

.. py:data:: SEASONAL_FORECAST_DIR

