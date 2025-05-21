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

Climate Index Definitions Module (seasonal_forecast_tools.index_definitions)

Defines specifications and variable mappings for climate indices used in the seasonal_forecast_tools workflow.
Centralizes metadata to ensure consistent index naming, descriptions, and variable handling across forecasting steps.

Key Components
--------------
- IndexSpec : dataclass with units, names, explanations, and required input variables.
- IndexSpecEnum : enumerates supported indices (e.g., Tmean, TR, HW) mapped to IndexSpec definitions.
- get_info(index_name) : fetches metadata for a given climate index.
- get_short_name_from_variable(variable) : maps standard CDS variable names (e.g. "2m_temperature") to short forms ("t2m").

Example
-------
IndexSpecEnum.get_info("TR").variables
['2m_temperature']

get_short_name_from_variable("2m_temperature")
't2m'

"""

from dataclasses import dataclass
from enum import Enum


@dataclass
class IndexSpec:
    unit: str
    full_name: str
    explanation: str
    variables: list


class ClimateIndex(Enum):
    HIA = IndexSpec(
        unit="C",
        full_name="Heat Index Adjusted",
        explanation="Heat Index Adjusted: A refined measure of apparent temperature that accounts"
        " for both air temperature and humidity. This index improves upon the simplified heat"
        " index by incorporating empirical corrections for extreme temperature and humidity"
        " conditions, ensuring a more accurate representation of perceived heat stress. If the"
        " temperature is ≤ 26.7°C (80°F), the index returns a simplified estimate.",
        variables=["2m_temperature", "2m_dewpoint_temperature"],
    )
    HIS = IndexSpec(
        unit="C",
        full_name="Heat Index Simplified",
        explanation="Heat Index Simplified: A quick estimate of perceived heat based on"
        " temperature and humidity, using an empirical formula designed for warm conditions"
        " (T > 20°C). If the temperature is ≤ 20°C, the heat index is set to the air temperature.",
        variables=["2m_temperature", "2m_dewpoint_temperature"],
    )
    Tmean = IndexSpec(
        unit="C",
        full_name="Mean Temperature",
        explanation="Mean Temperature: Calculates the average temperature over a specified period.",
        variables=["2m_temperature"],
    )
    Tmin = IndexSpec(
        unit="C",
        full_name="Minimum Temperature",
        explanation="Minimum Temperature: Tracks the lowest temperature recorded over a specified"
        " period.",
        variables=["2m_temperature"],
    )
    Tmax = IndexSpec(
        unit="C",
        full_name="Maximum Temperature",
        explanation="Maximum Temperature: Tracks the highest temperature recorded over a specified"
        " period.",
        variables=["2m_temperature"],
    )
    HW = IndexSpec(
        unit="Days",
        full_name="Heat Wave",
        explanation="Heat Wave: Identifies heat waves as periods with temperatures above a"
        " threshold. Default >= 27 °C for minimum 3 consecutive days.",
        variables=["2m_temperature"],
    )
    TR = IndexSpec(
        unit="Days",
        full_name="Tropical Nights",
        explanation="Tropical Nights: Counts nights with minimum temperatures above a certain"
        " threshold. Default threshold is 20°C.",
        variables=["2m_temperature"],
    )
    TX30 = IndexSpec(
        unit="Days",
        full_name="Hot Days (TX30)",
        explanation="Hot Days (TX30): Counts days with maximum temperature exceeding 30°C.",
        variables=["2m_temperature"],
    )
    RH = IndexSpec(
        unit="%",
        full_name="Relative Humidity",
        explanation="Relative Humidity: Measures humidity as a percentage.",
        variables=["2m_temperature", "2m_dewpoint_temperature"],
    )
    HUM = IndexSpec(
        unit="C",
        full_name="Humidex",
        explanation="Humidex: Perceived temperature combining temperature and humidity.",
        variables=["2m_temperature", "2m_dewpoint_temperature"],
    )
    AT = IndexSpec(
        unit="C",
        full_name="Apparent Temperature",
        explanation="Apparent Temperature: Perceived temperature considering wind and humidity.",
        variables=[
            "2m_temperature",
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
            "2m_dewpoint_temperature",
        ],
    )
    WBGT = IndexSpec(
        unit="C",
        full_name="Wet Bulb Globe Temperature",
        explanation="Wet Bulb Globe Temperature (Simple): Heat stress index combining temperature"
        " and humidity.",
        variables=["2m_temperature", "2m_dewpoint_temperature"],
    )

    @classmethod
    def by_name(cls, index_name: str):
        """
        Retrieve the complete information for a specified index.

        Parameters
        ----------
        index_name : str
            The name of the index (e.g., "HIA", "HIS", "Tmean").

        Returns
        -------
        IndexSpec
            Returns an instance of IndexSpec containing all relevant information.
            Raises a ValueError if the index is not found.
        """
        try:
            return cls[index_name].value
        except KeyError as kerr:
            indices = ', '.join(cls.__members__.keys())
            raise ValueError(
                f"Unknown index '{index_name}'. Available indices: {indices}"
            ) from kerr
        
    @staticmethod
    def from_input(arg):
        """Returns proper IndexSpec object from whatever input is valid"""
        if isinstance(arg, str):
            return ClimateIndex.by_name(arg)
        if isinstance(arg, IndexSpec):
            return arg
        raise ValueError("type of index_spec must be of IndexSpec or str")


def get_short_name_from_variable(variable):
    """
    Retrieve the short name of a variable within an index based on its standard name.

    Parameters
    ----------
    variable : str
        The standard name of the climate variable (e.g., "2m_temperature",
        "10m_u_component_of_wind").

    Returns
    -------
    str or None
        The short name corresponding to the specified climate variable (e.g., "t2m" for
        "2m_temperature").
        Returns None if the variable is not recognized.

    Notes
    -----
    This function maps specific variable names to their short names, which are used across
    climate index definitions. These mappings are independent of the indices themselves
    but provide consistent naming conventions for variable processing and file management.

    Examples
    --------
    >>> get_short_name_from_variable("2m_temperature")
    't2m'

    >>> get_short_name_from_variable("10m_u_component_of_wind")
    'u10'

    >>> get_short_name_from_variable("unknown_variable")
    None
    """
    return {
        "2m_temperature": "t2m",
        "2m_dewpoint_temperature": "d2m",
        "10m_u_component_of_wind": "u10",
        "10m_v_component_of_wind": "v10",
    }.get(variable)
