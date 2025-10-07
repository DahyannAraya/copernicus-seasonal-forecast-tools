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


Installation
============

The package requires **Python 3.10**, but versions 3.11 and 3.12 are also supported. Make sure your environment is using a compatible Python version before installation.

You can install **copernicus-seasonal-forecast-tools** in different ways, depending on your setup and preferences.

.. note::

   If you want to generate CLIMADA hazard objects, you must install the optional CLIMADA dependency.

Install from PyPI:

.. code-block:: bash

   pip install copernicus-seasonal-forecast-tools
   # optional (including CLIMADA installation):
   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   pip install -r docs/requirements.txt

Install via environment.yml (Conda or Mamba):

.. code-block:: bash

   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   conda env create -f environment.yml
   conda activate venv_forecast

Install from GitHub:

.. code-block:: bash

   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   pip install .
   pip install -r docs/requirements.txt  # optional (including CLIMADA installation)

To install the package **in developer (editable) mode on macOS/Linux**, and run the documentation and tests:

.. code-block:: bash

   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   python3.10 -m venv .venv_forecast
   source .venv_forecast/bin/activate
   pip install -e .
   pip install -r docs/requirements.txt # optional (including CLIMADA installation)

To install the package **in developer (editable) mode on Windows (PowerShell)**, and run the documentation and tests:

.. code-block:: powershell

   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   py -3.10 -m venv .venv_forecast
   .venv_forecast\Scripts\Activate.ps1
   pip install -e .
   pip install -r docs/requirements.txt # optional (including CLIMADA installation)


CLIMADA Installation
--------------------

CLIMADA is required to generate hazard layers.

- If you installed via `environment.yml`, CLIMADA is already included.
- If you installed from PyPI and then ran `pip install -r docs/requirements.txt`, CLIMADA is also installed.
- ⚠️ Only install CLIMADA manually if you skipped `requirements.txt` or want to customize its installation:

.. code-block:: bash

   git clone https://github.com/CLIMADA-project/climada_python.git
   cd climada_python
   pip install -e .

.. note::

   If you want to have all the functionalities of **CLIMADA**, you must install the full version. For detailed instructions, follow the official CLIMADA installation guide: `CLIMADA Installation Guide <https://climada-python.readthedocs.io/en/stable/guide/install.html>`_

.. _cds-api-setup:
How to Set Up the Copernicus API?
---------------------------------

This page guides you through setting up the Copernicus Climate Data Store (CDS) API so you can access and download climate datasets directly from your Python scripts.

.. note::
   **Quick Tip for Successful Data Access**
   
   To ensure smooth access to the climate datasets:
   
   * Remember to accept the Terms and Conditions for each dataset you're interested in
   * You'll find these terms at the bottom of each dataset's download page
   * This simple step enables your API requests to work correctly
   * For reference, the general data usage guidelines are available at: `CDS Term of Use <https://cds.climate.copernicus.eu/disclaimer-privacy>`_


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
  https://cds.climate.copernicus.eu/how-to-api

- Copy your personal API key and create a file named **`.cdsapirc`** in your home directory with the following format:

  .. code-block:: text

     url: https://cds.climate.copernicus.eu/api
     key: <your-uid>:<your-api-key>

  For full instructions, see:  
  https://cds.climate.copernicus.eu/how-to-api#install-the-cds-api-client

**4. Accept Dataset Terms and Conditions**

- Navigate to the dataset you want, for example:  
  https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=download

- Scroll to the bottom and **accept the terms**.






