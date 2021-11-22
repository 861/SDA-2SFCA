'''
Description: Join three results together
Version: 1.0
Autor: 
Date: 2021-11-17 09:03:33
LastEditors: 
LastEditTime: 2021-11-22 14:01:38
'''
import pandas as pd
import numpy as np


df_45 = pd.read_csv('access_results_45.csv')
print(df_45.shape)
df_30 = pd.read_csv('access_results_30.csv')
print(df_30.shape)
df_15 = pd.read_csv('access_results_15.csv')
print(df_15.shape)


temp_df = df_45.merge(df_30, on='geoid', how='left')
print(temp_df.shape)
temp_df2 = temp_df.merge(df_15, on='geoid', how='left')
print(temp_df2.shape)

temp_df2.fillna(0, inplace=True)


col_list = ['acc15', 'acc30', 'acc45']
for col in col_list:
    temp_df2[col] = temp_df2[col]*1000  # per 1000 population accessibility
temp_df2.head()

temp_df2.to_csv('access_results_merged_1000.csv', index=False)


df_45 = pd.read_csv('E2SFCA/access_e2sfca_jl_45.csv')
df_45.columns = ['geoid', 'acc45']
print(df_45.shape)
df_30 = pd.read_csv('E2SFCA/access_e2sfca_jl_30.csv')
df_30.columns = ['geoid', 'acc30']
print(df_30.shape)
df_15 = pd.read_csv('E2SFCA/access_e2sfca_jl_15.csv')
df_15.columns = ['geoid', 'acc15']
print(df_15.shape)


temp_df = df_45.merge(df_30, on='geoid', how='left')
print(temp_df.shape)
temp_df2 = temp_df.merge(df_15, on='geoid', how='left')
print(temp_df2.shape)

temp_df2.fillna(0, inplace=True)
print(temp_df2.head())

col_list = ['acc15', 'acc30', 'acc45']
for col in col_list:
    temp_df2[col+'_1000'] = temp_df2[col] * \
        1000  # per 1000 population accessibility
temp_df2.head()

temp_df2.to_csv('access_results_E2SFCA_merged_1000.csv', index=False)
