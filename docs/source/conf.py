# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Copernicus Seasonal Forecast Tools'
#copyright = '2025, Dahyann Araya'
author = 'Dahyann Araya'
release = '0.1.1'

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "myst_nb",
]
nb_execution_excludepatterns = [
    "source/climada_hazard_copernicus_forecast.ipynb",
]

autoapi_type = "python"
autoapi_dirs = ["../../seasonal_forecast_tools"]  # relative to conf.py


autoapi_keep_files = True
autoapi_add_toctree_entry = True

templates_path = ['_templates']

exclude_patterns = []

# Suppress substitution warnings like "T - 95"
suppress_warnings = ["substitution"]

autoapi_options = ["members", "undoc-members", "show-inheritance", "no-index"]


# Add project root directory to sys.path so autodoc can find modules
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]







