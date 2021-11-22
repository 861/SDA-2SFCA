'''
Description: 
Version: 1.0
Autor: 
Date: 2021-11-05 22:36:09
LastEditors: 
LastEditTime: 2021-11-22 13:59:32
'''

import pandas as pd
import numpy as np


pop_csv = 'data/cook_blocks_2020_15mibuffer_pop_demandscore_V9_166980_byInsurances.csv'
doc_csv = 'data/cookcounty_15mi_indivuals_doc_latlon_byInsuraces_161717_V18.csv'

dtype = {'orig': int, 'ds': float, 'groupcode': int}
pop_df = pd.read_csv(pop_csv, dtype=dtype)

print('pop:\n', pop_df.head())

dtype = {'docid': int, 'groupcode': int, 'as': float, 'dest': int, 'uid': int}
doc_df = pd.read_csv(doc_csv)
print('doc:\n', doc_df.head())

groupcode_list = list(set(pop_df['groupcode']))
for groupcode in groupcode_list:
    pop_df_tmp = pop_df[pop_df['groupcode'] == groupcode]
    doc_df_tmp = doc_df[doc_df['groupcode'] == groupcode]
    pop_df_tmp.to_csv('demand/cook_blocks_2020_15mibuffer_pop_demandscore_V9_166980_byInsurances_' +
                      str(groupcode) + '.csv', index=False)
    doc_df_tmp.to_csv('supply/cookcounty_15mi_indivuals_doc_latlon_byInsuraces_161717_V18_' +
                      str(groupcode) + '.csv', index=False)
