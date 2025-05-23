seasonal_forecast_tools.core.index_definitions
==============================================

.. py:module:: seasonal_forecast_tools.core.index_definitions

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

   Climate Index Definitions Module (seasonal_forecast_tools.index_definitions)

   Defines specifications and variable mappings for climate indices used in the seasonal_forecast_tools workflow.
   Centralizes metadata to ensure consistent index naming, descriptions, and variable handling across forecasting steps.

   Key Components
   --------------
   - IndexSpec : dataclass with units, names, explanations, and required input variables.
   - IndexSpecEnum : enumerates supported indices (e.g., Tmean, TR, HW) mapped to IndexSpec definitions.
   - get_info(index_name) : fetches metadata for a given climate index.
   - get_short_name_from_variable(variable) : maps standard CDS variable names (e.g. "2m_temperature") to short forms ("t2m").

   .. rubric:: Example

   IndexSpecEnum.get_info("TR").variables
   ['2m_temperature']

   get_short_name_from_variable("2m_temperature")
   't2m'



Classes
-------

.. autoapisummary::

   seasonal_forecast_tools.core.index_definitions.IndexSpec
   seasonal_forecast_tools.core.index_definitions.ClimateIndex


Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.core.index_definitions.get_short_name_from_variable


Module Contents
---------------

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


