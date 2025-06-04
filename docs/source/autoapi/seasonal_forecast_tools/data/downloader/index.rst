seasonal_forecast_tools.data.downloader
=======================================

.. py:module:: seasonal_forecast_tools.data.downloader

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

   Functionality to download data from the Copernicus Data Stores.

   ---

   Prerequisites:
   1. CDS API client installation:
      pip install cdsapi

   2. CDS account and API key:
      Register at https://cds.climate.copernicus.eu

   3. CDS API configuration:
      Create a .cdsapirc file in your home directory with your API key and URL of the CDS you want to access.
      For instance, if you want to access the Climate Data Store, see here for instructions:
      https://cds.climate.copernicus.eu/how-to-api#install-the-cds-api-client

   4. Dataset Terms and Conditions: After selecting the dataset to download, make
      sure to accept the terms and conditions on the corresponding dataset webpage (under the "download" tab)
      in the CDS portal before running the script.


Module Contents
---------------

.. py:data:: DATA_DIR

.. py:data:: LOGGER

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


