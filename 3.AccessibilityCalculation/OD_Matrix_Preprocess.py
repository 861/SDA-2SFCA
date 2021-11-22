'''
Description: E2SFCA 
Version: 1.0
Autor: 
Date: 2021-07-27 21:39:18
LastEditors: 
LastEditTime: 2021-11-22 13:59:49
'''


import pandas as pd
#import modin.pandas as pd
import numpy as np
import time

catchment_sizes = 2700  # units: seconds
travel_time = str(int(catchment_sizes/60))
# Gaussian decay function parrameters
sigma = catchment_sizes/3  # 3*sigma is enough to cover the most of the area


od_hdf = 'CookCounty_15miBuffer_Individuals_Blocks_OD_DOCV4_POPV5.HDF5_dask_merged.hdf5'
od_csv = 'results/od_30min.csv'


od_df = pd.read_hdf(od_hdf)
#dtype = {'orig': int, 'dest': int, 'duration': float, 'distance': float}
#od_df = pd.read_csv(od_csv, dtype=dtype)
od_df.drop(axis=1, columns=['distance'], inplace=True)
# selected data within the travel time range
od_df = od_df[od_df['duration'] <= catchment_sizes]

# compute weights using gaussian decay function and stored into od matrix to redue the computation time
od_df['w'] = od_df.apply(
    lambda x: np.exp(-x['duration']*x['duration'] / (2 * sigma**2)), axis=1)
print('od:\n', od_df.head())
od_df.to_csv('results/od_'+travel_time+'min_W.csv', index=False)


print("Finished!")
