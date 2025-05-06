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
Time utility functions for seasonal forecast pipelines.
Provides helpers to convert month names to numbers and calculate lead times
based on forecast configuration.
"""

import calendar
from datetime import date
import numpy as np

##########  Utility Functions  ##########


def month_name_to_number(month):
    """
    Convert a month name or number to its corresponding integer value.

    Accepts either an integer (1-12), full month name (e.g., 'March'),
    or abbreviated month name (e.g., 'Mar') and returns the corresponding
    month number (1-12).

    Parameters
    ----------
    month : int or str
        Month as an integer (1-12) or as a string (full or abbreviated month name).

    Returns
    -------
    int
        Month as an integer in the range 1-12.

    Raises
    ------
    ValueError
        If the input month is invalid, empty, or outside the valid range.
    """
    if isinstance(month, int):  # Already a number
        if 1 <= month <= 12:
            return month
        else:
            raise ValueError("Month number must be between 1 and 12.")
    if isinstance(month, str):
        if not month.strip():
            raise ValueError("Month cannot be empty.")  # e.g. "" or "   "
        month = month.capitalize()  # Ensure consistent capitalization
        if month in calendar.month_name:
            return list(calendar.month_name).index(month)
        elif month in calendar.month_abbr:
            return list(calendar.month_abbr).index(month)
    raise ValueError(f"Invalid month input: {month}")


def calculate_leadtimes(year, initiation_month, valid_period):
    """
    Calculate forecast lead times (in hours) between initiation and valid period.

    Parameters
    ----------
    year : int
        Forecast initiation year.
    initiation_month : int or str
        Month when the forecast starts, as integer (1–12) or full month name.
    valid_period : list of int or str
        Two-element list specifying the start and end months of the forecast period,
        either as integers or full month names (e.g., ['December', 'February']).

    Returns
    -------
    list of int
        List of lead times in hours (spaced every 6 hours) from initiation date
        to the end of the valid period.

    Raises
    ------
    ValueError
        If input months are invalid or misordered.

    Notes
    -----
    - If the valid period crosses a calendar year (e.g., Dec–Feb), it is handled correctly.
    - Lead times are counted from the first day of the initiation month.
    - The list includes all time steps in 6-hour intervals until the end of the valid period.

    Examples
    --------
    calculate_leadtimes(2022, "November", ["December", "February"])
    [720, 726, 732, ..., 2184]
    """
    # Convert initiation month to numeric if it is a string
    if isinstance(initiation_month, str):
        initiation_month = month_name_to_number(initiation_month)

    # Convert valid_period to numeric
    valid_period = [
        month_name_to_number(month) if isinstance(month, str) else month
        for month in valid_period
    ]
    start_month, end_month = valid_period

    # Determine if the valid period spans into the next calendar year
    spans_two_years = end_month < start_month

    # Determine valid year range for start and end of forecast period
    valid_years = np.array([year, year])

    if initiation_month > start_month:
        valid_years += 1
    if spans_two_years:
        valid_years[1] += 1

    # Reference starting date for initiation
    initiation_date = date(year, initiation_month, 1)
    valid_period_start = date(valid_years[0], start_month, 1)
    valid_period_end = date(
        valid_years[1],
        end_month,
        calendar.monthrange(valid_years[1], end_month)[1],
    )

    return list(
        range(
            (valid_period_start - initiation_date).days * 24,
            (valid_period_end - initiation_date).days * 24 + 24,
            6,
        )
    )
