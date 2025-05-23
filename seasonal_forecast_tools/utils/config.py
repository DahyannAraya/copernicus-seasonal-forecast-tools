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
Default output path for seasonal forecast data.

"""
import os
from pathlib import Path

# Default base directory for all seasonal forecast outputs
BASE_DATA_DIR = Path.home() / "climada/data"

# Path to Copernicus seasonal forecasts
SEASONAL_FORECAST_DIR = Path(os.getenv(
    "CLIMADA_SEASONAL_FORECAST_DIR",
    str(BASE_DATA_DIR / "copernicus_data" / "seasonal_forecasts")
))
