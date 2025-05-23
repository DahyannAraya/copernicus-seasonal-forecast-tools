"""
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
"""

from typing import List, Tuple

import geopandas as gpd
from cartopy.io import shapereader


def bounding_box_from_cardinal_bounds(north: float, south: float, east: float, west: float) -> Tuple[float, float, float, float]:
    """
    Return a bounding box tuple from cardinal directions.

    Parameters
    ----------
    north, south, east, west : float
        Geographic bounds.

    Returns
    -------
    tuple
        (lon_min, lat_min, lon_max, lat_max)
    """
    return (west, south, east, north)

def bounding_box_global() -> Tuple[float, float, float, float]:
    """
    Return a bounding box covering the entire globe.

    Returns
    -------
    tuple
        (-180.0, -90.0, 180.0, 90.0)
    """
    return (-180.0, -90.0, 180.0, 90.0)


def bounding_box_from_countries(countries: List[str], buffer: float = 1.0) -> Tuple[float, float, float, float]:
    """
    Return bounding box for a list of countries using Natural Earth data via Cartopy, with optional buffer.

    Parameters
    ----------
    countries : list of str
        List of ISO-3 country codes (e.g., ['CHE', 'FRA']).
    buffer : float, optional
        Buffer to add to all sides of the bounding box (in degrees). Default is 1.0.

    Returns
    -------
    tuple
        (lon_min, lat_min, lon_max, lat_max)

    Raises
    ------
    ValueError
        If no matching countries are found.
    """
    shp_path = shapereader.natural_earth(resolution="110m", category="cultural", name="admin_0_countries")
    gdf = gpd.read_file(shp_path)

    gdf["iso_lower"] = gdf["ADM0_A3"].str.lower()
    countries_lower = [c.lower() for c in countries]
    selection = gdf[gdf["iso_lower"].isin(countries_lower)]

    if selection.empty:
        raise ValueError(f"No countries found for input: {countries}")

    bounds = selection.total_bounds  # [minx, miny, maxx, maxy]
    lon_min, lat_min, lon_max, lat_max = bounds
    return (
        lon_min - buffer,
        lat_min - buffer,
        lon_max + buffer,
        lat_max + buffer
    )
