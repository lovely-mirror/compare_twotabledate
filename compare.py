# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:13:46 2018

@author: lhh
"""

import pandas as pd 

# =============================================================================
# #import  datasets
# =============================================================================
file_01 = open(r'C:\Users\lhh\Desktop\compare\one000001.SZ.csv')
file_02 = open(r'C:\Users\lhh\Desktop\compare\two000001.SZ.csv')

data_01 = pd.read_csv(file_01)
data_02 = pd.read_csv(file_02)


alldata = pd.merge(data_01,data_02,on = 'S_DTE')

alldata_drop = alldata.drop(['S_DTE'],axis=1)
alldata_drop = alldata_drop.drop(['S_ADJ_PRECLOSEPRICE'],axis=1)
alldata_drop = alldata_drop.drop(['S_TOT_NON_CUR_LIAB'],axis=1)
alldata_drop = alldata_drop.drop(['S_STSTATE'],axis=1)
alldata_drop = alldata_drop.drop(['S_EST_EPS'],axis=1)
alldata_drop = alldata_drop.drop(['S_EXP_FUT_PROFIT2Y'],axis=1)
alldata_drop = alldata_drop.drop(['S_EXP_FUT_PROFIT1Y'],axis=1)


data_01_drop = data_01.drop(['S_ADJ_PRECLOSEPRICE'],axis=1)
data_01_drop = data_01_drop.drop(['S_TOT_NON_CUR_LIAB'],axis=1)
data_01_drop = data_01_drop.drop(['S_STSTATE'],axis=1)
data_01_drop = data_01_drop.drop(['S_DTE'],axis=1)

col_list = list(data_01_drop.columns)

equal_list = []
for name in col_list:
    equal_list.append(name+'_equal')
    alldata_drop[name+'_equal'] = alldata_drop[name + '_x'] == alldata_drop[name + '_y']

if_equal = alldata_drop[equal_list].apply(pd.value_counts)