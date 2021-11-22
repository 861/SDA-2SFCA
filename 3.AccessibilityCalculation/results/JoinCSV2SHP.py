'''
Description: 
Version: 1.0
Autor: 
Date: 2020-09-02 09:43:16
LastEditors: 
LastEditTime: 2021-11-22 14:01:27
'''
from fiona import drivers
import pandas as pd
import geopandas as gpd

filename_gpkg = "/Users/yaxiongshao/Desktop/PaperDataV2/4AccessibilityCalculation/results/access_results"
filename = "/Users/yaxiongshao/Desktop/PaperDataV2/4AccessibilityCalculation/results/access_results_30"

shp = gpd.read_file("Blocks.shp")
print(shp.head())
print(shp.dtypes)
shp["GEOID10"] = shp["GEOID10"].astype("int64")
print(shp.head())

csv = pd.read_csv(filename+".csv")
print(csv.head())
print(csv.dtypes)
csv["geoid"] = csv["geoid"].astype("int64")
print(csv.head())
gdf = shp.merge(csv, left_on='GEOID10', right_on="geoid", how='left')
gdf["GEOID10"] = gdf["GEOID10"].astype("str")
# gdf.to_file(filename+".shp")
gdf.to_file(filename_gpkg+".gpkg", layer="access30", driver="GPKG")
gdf.to_file(filename_gpkg+".gpkg", layer="access30_n", driver="GPKG")
