seasonal_forecast_tools.heat_index
==================================

.. py:module:: seasonal_forecast_tools.heat_index

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

   ---

   Module for calculating various indices, including:
   - Relative Humidity
   - Humidex
   - Heat Index (Simplified & Adjusted)
   - Wind Speed
   - Apparent Temperature
   - Wet Bulb Globe Temperature (WBGT)
   - Tropical Nights (TR)
   - TX30 (Days above 30°C)
   - Heatwaves (HW)



Attributes
----------

.. autoapisummary::

   seasonal_forecast_tools.heat_index.LOGGER
   seasonal_forecast_tools.heat_index.HI_COEFFS
   seasonal_forecast_tools.heat_index.HI_ADJUSTED_COEFFS


Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.heat_index.kelvin_to_fahrenheit
   seasonal_forecast_tools.heat_index.fahrenheit_to_kelvin
   seasonal_forecast_tools.heat_index.fahrenheit_to_celsius
   seasonal_forecast_tools.heat_index.celsius_to_kelvin
   seasonal_forecast_tools.heat_index.kelvin_to_celsius
   seasonal_forecast_tools.heat_index.calculate_relative_humidity
   seasonal_forecast_tools.heat_index.calculate_humidex
   seasonal_forecast_tools.heat_index.calculate_heat_index_simplified
   seasonal_forecast_tools.heat_index.calculate_heat_index_adjusted
   seasonal_forecast_tools.heat_index.calculate_wind_speed
   seasonal_forecast_tools.heat_index.calculate_apparent_temperature
   seasonal_forecast_tools.heat_index.calculate_nonsaturation_vapour_pressure
   seasonal_forecast_tools.heat_index.calculate_wbgt_simple
   seasonal_forecast_tools.heat_index.calculate_heat_index
   seasonal_forecast_tools.heat_index.calculate_tr
   seasonal_forecast_tools.heat_index.calculate_tx30
   seasonal_forecast_tools.heat_index.calculate_hw_1D
   seasonal_forecast_tools.heat_index.calculate_hw


Module Contents
---------------

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


