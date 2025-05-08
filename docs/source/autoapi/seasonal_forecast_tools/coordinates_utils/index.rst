seasonal_forecast_tools.coordinates_utils
=========================================

.. py:module:: seasonal_forecast_tools.coordinates_utils

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

   Coordinate utilities for the Copernicus seasonal forecast module.

   Provides helper functions to construct bounding boxes from global, cardinal, or country-level input.



Functions
---------

.. autoapisummary::

   seasonal_forecast_tools.coordinates_utils.bounding_box_from_cardinal_bounds
   seasonal_forecast_tools.coordinates_utils.bounding_box_global
   seasonal_forecast_tools.coordinates_utils.bounding_box_from_countries


Module Contents
---------------

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


