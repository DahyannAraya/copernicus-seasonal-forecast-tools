from setuptools import setup, find_packages

setup(
    name="copernicus-seasonal-forecast-tools",
    version="0.1.0",
    description="CLIMADA-compatible module for generating and analyzing seasonal forecast hazards from Copernicus data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dahyann Araya",
    license="GPL-3.0-or-later",
    python_requires=">=3.10,<3.12",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "ipykernel",
        "xarray",
        "cfgrib",
        "cdsapi",
        "numpy",
        "pandas",
        "matplotlib",
        "netCDF4",
        "shapely",
        "geopandas",
        "cartopy",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Hydrology",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
