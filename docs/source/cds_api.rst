.. raw:: html

   <p>
      <a href="https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools">
         <img src="https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue" alt="GitHub repo">
      </a>
      <a href="https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools/blob/main/LICENSE">
         <img src="https://img.shields.io/github/license/DahyannAraya/copernicus-seasonal-forecast-tools" alt="License">
      </a>
      <a href="https://badge.fury.io/py/copernicus-seasonal-forecast-tools">
         <img src="https://badge.fury.io/py/copernicus-seasonal-forecast-tools.svg" alt="PyPI version">
      </a>
      <a href="https://pypi.org/project/copernicus-seasonal-forecast-tools/">
         <img src="https://img.shields.io/badge/python-3.10–3.12-blue?logo=python&logoColor=white" alt="Supported Python versions">
      </a>
      <a href="https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest">
         <img src="https://readthedocs.org/projects/copernicus-seasonal-forecast-tools/badge/?version=latest" alt="Documentation Status">
      </a>
   </p>


How to Set Up the Copernicus API?
=================================

This page guides you through setting up the Copernicus Climate Data Store (CDS) API so you can access and download climate datasets directly from your Python scripts.

.. note::
   **Quick Tip for Successful Data Access**
   
   To ensure smooth access to the climate datasets:
   
   * Remember to accept the Terms and Conditions for each dataset you're interested in
   * You'll find these terms at the bottom of each dataset's download page
   * This simple step enables your API requests to work correctly
   * For reference, the general data usage guidelines are available at: https://cds.climate.copernicus.eu/terms

Step-by-Step Instructions
-------------------------

**1. Create a CDS Account**

- Register at the Copernicus Climate Data Store:  
  https://cds.climate.copernicus.eu

**2. Install the CDS API Client**

- In your terminal, run:

  .. code-block:: bash

     pip install cdsapi

**3. Configure Your API Key**

- After registration, go to your CDS account page:  
  https://cds.climate.copernicus.eu/api-how-to

- Copy your personal API key and create a file named **`.cdsapirc`** in your home directory with the following format:

  .. code-block:: text

     url: https://cds.climate.copernicus.eu/api/v2
     key: <your-uid>:<your-api-key>

  For full instructions, see:  
  https://cds.climate.copernicus.eu/how-to-api#install-the-cds-api-client

**4. Accept Dataset Terms and Conditions**

- Navigate to the dataset you want, for example:  
  https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=download

- Scroll to the bottom and **accept the terms**.






