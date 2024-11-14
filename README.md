# Introduction

This document provides a step-by-step guide to install the GeographicLib Python package, download the Geoid data (EGM2008), and calculate the ellipsoidal height of WGS84 from (latitude, longitude, mean-sea level).

## Step 1: Install GeographicLib Python Package

To install the GeographicLib Python package, use the following command:

```bash
pip install geographiclib
```

## Step 2: Download the Geoid Data (EGM2008)

To download the EGM2008 geoid data, you can use the GeographicLib datasets. Run the following command:

```bash
geographiclib-get-geoids egm2008-1
```

## Step 3: Calculate Geoid Height in Python

Calculate the ellipsoidal height using the python script msl2hae.py by editing the (latitude, longitude, msl).:

```bash
python msl2hae.py
```
The script will call the GeoidEval command in shell and get the result for potential calculation. Please visit [geographiclib documentation](https://geographiclib.sourceforge.io/1.52/GeoidEval.1.html) for details of the command.
