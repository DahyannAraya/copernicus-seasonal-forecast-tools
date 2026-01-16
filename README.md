<img src="https://raw.githubusercontent.com/DahyannAraya/copernicus-seasonal-forecast-tools/refs/heads/main/images/Logos.png" alt="Project Logos" width="70%"/>


# **Copernicus Seasonal Forecast Tools**
[![GitHub repo](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools)
[![License](https://img.shields.io/github/license/DahyannAraya/copernicus-seasonal-forecast-tools)](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/copernicus-seasonal-forecast-tools.svg)](https://badge.fury.io/py/copernicus-seasonal-forecast-tools)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.12-blue?logo=python&logoColor=white)](https://pypi.org/project/copernicus-seasonal-forecast-tools/)
[![Downloads](https://img.shields.io/pypi/dm/copernicus-seasonal-forecast-tools?color=yellow&label=Downloads)](https://pypistats.org/packages/copernicus-seasonal-forecast-tools)
[![Documentation Status](https://readthedocs.org/projects/copernicus-seasonal-forecast-tools/badge/?version=latest)](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest)



<img src="https://raw.githubusercontent.com/DahyannAraya/copernicus-seasonal-forecast-tools/refs/heads/main/images/copernicus_forecast_qr.png" alt="Repository QR Code" width="150"/>

This repository hosts the **copernicus-seasonal-forecast-tools**, a Python package developed to manage seasonal forecast data from the [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu/) as part of the [U-CLIMADAPT project](https://www.dwd.de/EN/research/projects/socioeconomics/fpcup_u_climadapt/fpcup_u_climadapt.html).

It offers comprehensive tools for downloading, processing, computing climate indices, and generating hazard objects based on seasonal forecast datasets, particularly [Seasonal forecast daily and subdaily data on single levels](https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=overview).
The package is tailored to integrate seamlessly with the [CLIMADA](https://climada.ethz.ch/) (CLIMate ADAptation) platform, supporting climate risk assessment and the development of effective adaptation strategies.

Users can:
- Automatically download of high-resolution seasonal forecast data via the CDS API
- Preprocess sub-daily fields into daily aggregates
- Compute heat-related indices (e.g., **heatwave days**, **tropical nights**, **TX30**)
- Generate **CLIMADA hazard objects**
- Benefit from the modular design for extending to new indices or forecast products


## **Documentation**
For full documentation of all features and functions, please refer to the [Copernicus Seasonal Forecast Tools documentation on ReadTheDocs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest).


## **Getting Started**

To use this package, you must first configure access to the [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu), which provides the seasonal forecast datasets.

We've prepared a comprehensive [CDS API setup guide](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/cds_api.html) to walk you through each step of the process. Once configured, you'll be ready to explore and analyze seasonal forecast data.


## **Installation**

The package requires Python 3.10, 3.11 or 3.12. Make sure your environment is using a compatible Python version before installation.

You can install **copernicus-seasonal-forecast-tools** in different ways, depending on your setup and preferences.
Below we describe the installation using the package manager and environment management system
[Conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html).

> **Note:** If you want to generate CLIMADA hazard objects, you must install the **optional CLIMADA dependency**.  
> For full installation instructions, see the [online documentation](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/index.html).


### 1. To install the package WITH the climate-risk assessment package CLIMADA:

```bash
conda create -n copernicus_with python=3.11 pip climada
conda activate copernicus_with
pip install copernicus-seasonal-forecast-tools
```
### 2. To install the package WITHOUT the climate-risk assessment package CLIMADA:
```bash
conda create -n copernicus_without python=3.11 pip geopandas
conda activate copernicus_without
pip install copernicus-seasonal-forecast-tools
```
### 3. To install the package in DEVELOPER (editable) mode, and run the documentation and tests:
```bash
conda create -n copernicus-dev-mode python=3.11 pip geopandas climada
conda activate copernicus-dev-mode
git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
cd copernicus-seasonal-forecast-tools
pip install -e .
```


### **CLIMADA Installation**

CLIMADA is required to generate hazard layers. If you installed the package without CLIMADA you can install CLIMADA later on with
```bash
conda install climada
```
If you want to customize the CLIMADA installation, follow the [Advanced Instructions](https://climada-python.readthedocs.io/en/stable/getting-started/install.html#advanced-instructions-installing-from-source) of the CLIMADA installation guide.


## **Example of use**

This section provides practical example to help users understand how to work with the copernicus-seasonal-forecast-tools package. The notebooks demonstrate key steps including downloading data, computing climate indices, and generating CLIMADA hazard objects.

- **DEMO_copernicus_forecast_seasonal.ipynb**: This is the first notebook to run. It demonstrates how to install and use the `seasonal_forecast_tools` to download, process, and convert seasonal forecast data into a CLIMADA hazard object.


### Notebooks

| Notebook | Open in Colab | GitHub (Documentation) |
|----------|----------------|-----------------|
| DEMO Copernicus Seasonal Forecast | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb) | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html) |
| Download and Process Data | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Download_and_Process_Data) | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#download-and-process-data) |
| Calculate Climate Indices | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Calculate_Climate_Indices)  | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#calculate-climate-indices) |
| Calculate a Hazard Object | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Calculate_a_Hazard_Object)  | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#calculate-a-hazard-object) |
| Example for Reading and Plotting Hazard | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Example_for_reading_and_plotting_hazard) | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#example-for-reading-and-plotting-hazard) |

You can find further material in [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/DEMO_Modul_climada_copernicus_seasonal_forecast_workshop.ipynb), where we provide an extended demonstration.


## Community guidelines and contributions

This section summarizes how to contribute and where to find more information. We follow the CLIMADA contribution workflow and conventions. See details in [CONTRIBUTING.md](CONTRIBUTING.md).


## **License**

[GPL-3.0 license](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools/blob/main/LICENSE)


## **Resources**
- [U-CLIMADAPT Project](https://www.dwd.de/EN/research/projects/socioeconomics/fpcup_u_climadapt/fpcup_u_climadapt.html)
- [Copernicus Seasonal Forecast Tools package on CLIMADA](https://climada-python.readthedocs.io/en/latest/user-guide/climada_hazard_copernicus_seasonal_forecast.html)
- [Copernicus Seasonal Forecast Tools Package — Extended Demonstration](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/DEMO_Modul_climada_copernicus_seasonal_forecast_workshop.ipynb)
- [Seasonal forecast daily and subdaily data on single levels](https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=overview)
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu)
- [CLIMADA Documentation](https://climada.ethz.ch/)

