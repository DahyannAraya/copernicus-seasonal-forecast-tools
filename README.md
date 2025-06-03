<img src="https://raw.githubusercontent.com/DahyannAraya/copernicus-seasonal-forecast-tools/refs/heads/main/images/Logos.png" alt="Project Logos" width="70%"/>


# **Copernicus Seasonal Forecast Tools**
[![GitHub repo](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools)
[![License](https://img.shields.io/github/license/DahyannAraya/copernicus-seasonal-forecast-tools)](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/copernicus-seasonal-forecast-tools.svg)](https://badge.fury.io/py/copernicus-seasonal-forecast-tools)
[![Downloads](https://img.shields.io/pypi/dm/copernicus-seasonal-forecast-tools?color=yellow&label=Downloads)](https://pypistats.org/packages/copernicus-seasonal-forecast-tools)
[![Documentation Status](https://readthedocs.org/projects/copernicus-seasonal-forecast-tools/badge/?version=latest)](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest)



<img src="https://raw.githubusercontent.com/DahyannAraya/copernicus-seasonal-forecast-tools/refs/heads/main/images/copernicus_forecast_qr.png" alt="Repository QR Code" width="150"/>

This repository hosts the **copernicus-seasonal-forecast-tools** package, a Python module developed as part of the [U-CLIMADAPT project](https://www.copernicus-user-uptake.eu/user-uptake/details/responding-to-the-impact-of-climate-change-u-climadapt-488).

The module bridges **seasonal forecast data** from the [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu) with flexible data processing and climate impact modeling workflows. It supports downloading [sub-daily Copernicus forecasts](https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=overview) and **aggregating them to daily resolution**, enabling analysis of climate indices for impact forecasting.

Users can:
- Convert raw Copernicus seasonal forecasts into usable daily datasets.
- Compute **heat-related climate indices** (e.g., Heatwaves, Tropical Nights).
- Generate **CLIMADA-compatible hazard objects** from processed forecasts.

While not part of the core [CLIMADA](https://climada.ethz.ch/) platform, it is designed for **seamless integration** with CLIMADA for climate impact and risk workflows.



## **Documentation**
For full documentation of all features and functions, please refer to the [Copernicus Seasonal Forecast Tools documentation on ReadTheDocs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/?badge=latest).


## **Getting Started**

To use this package, you must first configure access to the [Copernicus Climate Data Store (CDS)](https://cds.climate.copernicus.eu), which provides the seasonal forecast datasets.

We've prepared a comprehensive [CDS API setup guide](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/cds_api.html) to walk you through each step of the process. Once configured, you'll be ready to explore and analyze seasonal forecast data.


## **Installation**

You can install **`copernicus-seasonal-forecast-tools`** in three ways, depending on your setup and preferences.

> **Note:** If you want to generate CLIMADA hazard objects, you must install the **optional CLIMADA dependency**.  
> For full installation instructions, see the [online documentation](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/index.html).


### 1. Install via pip (recommended for most users)

```bash
pip install copernicus-seasonal-forecast-tools
git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git (optional)
pip install -r docs/requirements.txt (optional)
```
### 2. Install via environment.yml (Conda or Mamba):
```bash
git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
conda env create -f environment.yml
conda activate venv_forecast
```
### 3. Install directly from GitHub 
```bash
git clone https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools.git
cd copernicus-seasonal-forecast-tools
pip install .
pip install -r docs/requirements.txt (optional)
```


### **CLIMADA Installation**

CLIMADA is required to generate hazard layers.

- If you installed via `environment.yml`, CLIMADA is already included.
- If you installed from PyPI and then ran `pip install -r docs/requirements.txt`, CLIMADA is also installed.

> **Note**  
> If you want to have all the functionalities of **CLIMADA**, you must install the full version.  
> 👉 For detailed instructions, follow the official CLIMADA installation guide:  
> [CLIMADA Installation Guide](https://climada-python.readthedocs.io/en/stable/guide/install.html)


## **Example of use**

This section provides practical example to help users understand how to work with the copernicus-seasonal-forecast-tools package. The notebooks demonstrate key steps including downloading data, computing climate indices, and generating CLIMADA hazard objects.

- **`DEMO_copernicus_forecast_seasonal.ipynb`**: This is the first notebook to run. It demonstrates how to install and use the `seasonal_forecast_tools` to download, process, and convert seasonal forecast data into a CLIMADA hazard object.


### Notebooks

| Notebook | Open in Colab | GitHub (Documentation) |
|----------|----------------|-----------------|
| DEMO Copernicus Seasonal Forecast | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb) | [View on GitHub](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html) |
| Download and Process Data | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Download_and_Process_Data) | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#download-and-process-data) |
| Calculate Climate Indices | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Calculate_Climate_Indices)  | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#calculate-climate-indices) |
| Calculate a Hazard Object | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Calculate_a_Hazard_Object)  | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#calculate-a-hazard-object) |
| Example for Reading and Plotting Hazard | [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/Modul_climada_copernicus_seasonal_forecast_workshop.ipynb#scrollTo=Example_for_reading_and_plotting_hazard) | [View in Docs](https://copernicus-seasonal-forecast-tools.readthedocs.io/en/latest/climada_hazard_copernicus_forecast.html#example-for-reading-and-plotting-hazard) |

You can find further material in [<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="20">](https://colab.research.google.com/github/DahyannAraya/copernicus_climada_seasonal_forecast_workshop/blob/main/DEMO_Modul_climada_copernicus_seasonal_forecast_workshop.ipynb), where we provide an extended demonstration.



## **License**

[GPL-3.0 license](https://github.com/DahyannAraya/copernicus-seasonal-forecast-tools/blob/main/LICENSE)


## **Resources**
- [U-CLIMADAPT Project](https://www.copernicus-user-uptake.eu/user-uptake/details/responding-to-the-impact-of-climate-change-u-climadapt-488)
- [Copernicus Seasonal Forecast on CLIMADA](to do)
- [Copernicus Seasonal Forecast Module extended demostration](https://colab.research.google.com/github/DahyannAraya/climada_copernicus_seasonal_forecast_workshop/blob/main/DEMO_Modul_climada_copernicus_seasonal_forecast_workshop.ipynb)
- [Seasonal forecast daily and subdaily data on single levels](https://cds.climate.copernicus.eu/datasets/seasonal-original-single-levels?tab=overview)
- [Copernicus Climate Data Store](https://cds.climate.copernicus.eu)
- [CLIMADA Documentation](https://climada.ethz.ch/)

