seasonal_forecast_tools.utils.time_utils
========================================

.. py:module:: seasonal_forecast_tools.utils.time_utils

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
   Time utility functions for seasonal forecast pipelines.
   Provides helpers to convert month names to numbers and calculate lead times
   based on forecast configuration.





Module Contents
---------------

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


