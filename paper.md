---
title: "Copernicus Forecast Module: Bridging Seasonal Climate Predictions and Impact-Based Forecasting for Operational Risk Assessment"

tags:
  - Python
  - Seasonal forecasts
  - Copernicus Climate Data Store
  - Climate hazard modeling
  - Impact-based forecasting
  - Climate risk assessment
  - Climate adaptation
  - Open-source software
authors:
  - name: Dahyann Araya
    affiliation: "1,2"
  - name: Valentin Gebhart
    affiliation: "1,2"
  - name: David N. Bresch
    affiliation: "1,2"
  - name: Tobias Geiger
    affiliation: "3,4"
affiliations:
  - name: Institute for Environmental Decisions, ETH Zurich, Universitätstr. 22, 8092 Zurich, Switzerland
    index: 1
  - name: Federal Office of Meteorology and Climatology MeteoSwiss, Operation Center 1, P.O. Box 257, 8058 Zurich-Airport, Switzerland
    index: 2
  - name: Potsdam Institute for Climate Impact Research (PIK), Member of the Leibniz Association, Potsdam, Germany
    index: 3
  - name: Regional Climate Office Potsdam, Deutscher Wetterdienst, Potsdam, Germany
    index: 4
date: 2025-04-28
bibliography: paper.bib
---

# Summary

Disaster risk management is being revolutionized by two complementary approaches: impact-based forecasting (IBF) and seasonal forecast data. While traditional forecasting focuses solely on weather predictions, IBF integrates hazard information—such as extreme temperature patterns—with socioeconomic vulnerability factors, enabling quantitative risk assessments from public health to infrastructure resilience. Seasonal forecasts extend this capacity by providing probabilistic predictions months ahead, offering opportunities for proactive adaptation strategies.

However, a critical gap remains: the absence of operational systems that systematically link seasonal forecasts with impact-based models.  This work helps to address the strategic gap in moving from weather-centric forecasts to impact-oriented services, contributing to the development of operational, reproducible pipelines that connect probabilistic climate forecasts to warning chain. To address this, we introduce the **Copernicus Forecast Module**, a foundational tool to integrate seasonal climate predictions into the CLIMADA platform. It automates the workflow from data retrieval via the Copernicus Climate Data Store (CDS), through preprocessing and climate index calculation, to the generation of CLIMADA-compatible hazard objects. This enables streamlined, actionable risk assessments months in advance into concrete impact assessments.

The module automates the entire pipeline—from data retrieval and preprocessing, to climate index computation and hazard object generation—enabling seamless and timely impact assessments that support proactive risk management months ahead of potential events.

# Statement of need

Despite the growing interest in both seasonal prediction and impact-based modelling—aiming to shift from describing what the hazard will look like to how the hazard will affect, and moving from weather-centric forecasts to impact-oriented services—there is still a lack of operational and reproducible tools to link probabilistic seasonal climate predictions with quantitative impact assessment frameworks [@Geiger:2024]. Current workflows are often fragmented and require manual intervention at multiple stages—from handling unstructured data sources and access, to preprocessing and hazard transformation—which can delay critical risk assessments and limit reproducibility [@Potter:2025, @Wyatt:2023]. 

The Copernicus Forecast Module addresses this gap by providing an automated, flexible, and modular solution. It connects seasonal forecast data from the Copernicus Climate Data Store (CDS) with the hazard and impact modeling capabilities of the CLIMADA platform [@aznar-siguan_climada_2019], an open-source platform for climate risk analysis and the evaluation of adaptation benefits [@bresch_climada_2021]. This integration allows users to efficiently transform raw seasonal predictions into actionable climate risk insights. The module supports the definition of custom climate indices, the integration of data from multiple providers, and adaptation to emerging hazard types and regional contexts. Thereby strengthening the operational implementation of impact forecasting and facilitating downstream components of the warning value chain or operational pipeline [@Golding:2019] bridging the gap between probabilistic seasonal forecasts and concrete impact assessments. 

# Implementation and functionality

The Copernicus Climate Data Store currently offers one of the most comprehensive and globally accessible repositories of seasonal forecast data [@Buontempo:2022]. It aggregates hourly-resolution outputs from around eight major meteorological centers, covering more than 50 climate variables. These datasets span both hindcast and forecast periods, starting from around 1996 to the present, with up to 6-month lead times and multiple ensemble members per forecasting provider [@cds_documentation]. While the richness of this dataset enables advanced climate research, its size and complexity can make direct use challenging.

To address this issue, the Copernicus Forecast Module provides streamlined tools to access data via cdsapi, filter, and aggregate raw GRIB/netCDF files into daily netCDF outputs, facilitating their downstream use in climate index calculation and risk modeling. The module checks whether the raw data has already been downloaded. Once retrieved, it processes the raw files into gridded daily netCDF datasets, structured by forecast step, ensemble member, latitude, and longitude. Each file includes multi-ensemble data for daily mean, maximum, and minimum values.

Once daily data is calculated, users can select from twelve available heat indices, including temperature-based indices (Tmean, Tmin, Tmax), heat stress indicators (HIA—Heat Index Adjusted, HIS—Heat Index Simplified, HUM—Humidex, AT—Apparent Temperature, WBGT—Wet Bulb Globe Temperature), and extreme event indices (HW—Heat Wave, TR—Tropical Nights, TX30—Hot Days).

Calculated index data is saved in netCDF format and organized by index and time period, with file paths printed during processing. Statistical summaries of the index across ensemble members are computed and saved simultaneously, providing insight into forecast behavior. Users can then transform the index into a CLIMADA-compatible hazard object, enabling integration into impact-based forecasting workflows.

# Status

The current version of the Copernicus Forecast Module supports:

- Automated download of seasonal forecasts via the Copernicus API
- Preprocessing of sub-daily forecast data into daily formats
- Calculation of heat-related climate indices (e.g., heatwave days, tropical nights)
- Conversion of processed indices into CLIMADA hazard objects for impact modeling
- Flexible modular architecture to accommodate additional indices or datasets

The module has been tested within CLIMADA workflows and demonstrated in example notebooks. Planned future developments include integrating skill metrics from Copernicus, when available, across ensemble members to improve transparency in the impact-based forecasting chain. Further enhancements will support adaptation to new forecast data versions from Copernicus as they become available, including those with improved spatial resolution.

# Acknowledgements

The development of the Copernicus Forecast Module was supported by the U-CLIMADAPT project, which aims to enhance the usability of Copernicus data products for climate adaptation planning. We also acknowledge the CLIMADA development team at ETH Zurich for providing the risk modeling framework that this module integrates with.

# References
