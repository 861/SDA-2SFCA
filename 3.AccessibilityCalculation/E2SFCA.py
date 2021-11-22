'''
Description: 
Version: 1.0
Autor: 
Date: 2021-11-20 23:35:12
LastEditors: 
LastEditTime: 2021-11-22 14:00:34
'''
# -*- coding: utf-8 -*-
from access import Access, weights, datasets
import pandas as pd
import time


doc_path = "doctor_in_buffer_15mi.csv"
pop_path = "cook_blocks_2020_15mibuffer_pop_demandscore_V9_166980.csv"
od_path = "od_30min_W.csv"


start = time.time()
doc = pd.read_csv(doc_path)
pop = pd.read_csv(pop_path)
od = pd.read_csv(od_path)

print(doc.head())
print(pop.head())
print(od.head())


acc = Access(demand_df=pop,
             demand_index='orig',
             demand_value='pop',
             supply_df=doc,
             supply_index='dest',
             supply_value=["doc"],
             cost_df=od,
             cost_origin='orig',
             cost_dest='dest',
             cost_name='duration')

gaussian5 = weights.gaussian(600)


acc.enhanced_two_stage_fca(name='acc', weight_fn=gaussian5)
acc.access_df.to_csv("access_E2SFCA_30.csv")
end_time = time.time()
print(end_time - start)


od_path = "od_45min_W.csv"
start = time.time()
doc = pd.read_csv(doc_path)
pop = pd.read_csv(pop_path)
od = pd.read_csv(od_path)

print(doc.head())
print(pop.head())
print(od.head())


acc = Access(demand_df=pop,
             demand_index='orig',
             demand_value='pop',
             supply_df=doc,
             supply_index='dest',
             supply_value=["doc"],
             cost_df=od,
             cost_origin='orig',
             cost_dest='dest',
             cost_name='duration')

gaussian5 = weights.gaussian(900)


acc.enhanced_two_stage_fca(name='acc', weight_fn=gaussian5)
acc.access_df.to_csv("access_E2SFCA_45.csv")
end_time = time.time()
print(end_time - start)
