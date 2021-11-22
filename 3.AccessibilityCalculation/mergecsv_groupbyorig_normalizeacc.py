'''
Description: 
Version: 1.0
Autor: 
Date: 2021-11-15 09:53:15
LastEditors: 
LastEditTime: 2021-11-22 14:00:19
'''
import pandas as pd
import numpy as np
import glob

csv_list = glob.glob('resuls/access30*.csv')
df_list = []
for csv in csv_list:
    df = pd.read_csv(csv)
    df_list.append(df)
merge_df = pd.concat(df_list)

print(merge_df.head())
print(merge_df.shape)

grouped_df = merge_df.groupby(['orig'])['R_sum'].reset_index()
grouped_df.columns = ['geoid', 'acc30']
Max = np.max(grouped_df['acc30'])
Min = np.min(grouped_df['acc30'])
grouped_df['acc30_n'] = (grouped_df['acc30'] - Min)/(Max - Min)
grouped_df.to_csv('results/access30.csv', index=False)
