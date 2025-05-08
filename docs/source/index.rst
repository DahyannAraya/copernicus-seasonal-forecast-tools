.. Copernicus Seasonal Forecast Tools documentation master file, created by
   sphinx-quickstart on Wed May  7 16:11:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



.. Copernicus Seasonal Forecast Tools documentation master file


.. image:: _static/Logos.png
   :width: 50%
   :align: center

Copernicus Seasonal Forecast Tools
==================================

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
        <a href="https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest">
            <img src="https://readthedocs.org/projects/copernicus-seasonal-forecast-tools/badge/?version=latest" alt="Documentation Status">
        </a>
    </p>


Overview
--------

Welcome to the **Copernicus Seasonal Forecast Tools**! 

This Python package, developed under the `U-CLIMADAPT <https://www.copernicus-user-uptake.eu/user-uptake/details/responding-to-the-impact-of-climate-change-u-climadapt-488>`_ project, connects seasonal forecast data with climate impact modeling. We designed this module to make working with climate forecasts more accessible for researchers and practitioners.

The module bridges **seasonal forecast data** from the `Copernicus Climate Data Store (CDS) <https://cds.climate.copernicus.eu>`_ with flexible data processing and climate impact modeling workflows. It supports downloading `sub-daily Copernicus forecasts <https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=overview>`_ and **aggregating them to daily resolution**, enabling analysis of climate indices for impact forecasting.

Key features include:

- 📥 Download Copernicus CDS seasonal forecasts (subdaily)
- 🔁 Convert to daily resolution automatically
- 🌡️ Calculate heat-related climate indices (e.g., Heatwaves, Tropical Nights).
- 🧩 Integrate with CLIMADA hazard workflows

While not part of the core `CLIMADA <https://climada.ethz.ch/>`_ platform, it is designed for **seamless integration** with CLIMADA for climate impact and risk workflows



Getting Started
---------------

To use this package, you must first configure access to the `Copernicus Climate Data Store (CDS) <https://cds.climate.copernicus.eu>`_, which provides the seasonal forecast datasets.

**note:** You need a CDS account, API credentials, and to accept the dataset's terms and conditions.

We've prepared a comprehensive :doc:`CDS API setup guide <cds_api>` to walk you through each step of the process. Once configured, you'll be ready to explore and analyze seasonal forecast data with ease!

Installation
------------

Install from PyPI:

.. code-block:: bash

   pip install copernicus-seasonal-forecast-tools

Install via conda or mamba:

.. code-block:: bash

   conda install -c conda-forge copernicus-seasonal-forecast-tools

Install from GitHub:

.. code-block:: bash

   git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
   cd copernicus-seasonal-forecast-tools
   pip install .

CLIMADA Installation
--------------------

To generate hazard layers, install `CLIMADA <https://github.com/CLIMADA-project/climada_python>`_:

.. code-block:: bash

   git clone https://github.com/CLIMADA-project/climada_python.git
   cd climada_python
   pip install -e .

Examples
--------

Jupyter notebooks for full pipelines:

- `Workshop notebook on GitHub <https://github.com/DahyannAraya/climada_copernicus_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb>`_
- `Demo end-to-end pipeline <https://github.com/DahyannAraya/climada_copernicus_seasonal_forecast_workshop/blob/main/DEMO_Modul_climada_copernicus_seasonal_forecast_workshop.ipynb>`_



.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :titlesonly:

   Home <self>
   CDS API <cds_api>
   autoapi/index
   climada_hazard_copernicus_forecast.ipynb
   How to Cite <citing>
   Resources <modules>


