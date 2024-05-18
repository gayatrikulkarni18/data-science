# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:48:02 2024

@author: Gayatri kulkarni
"""


import sys
import os
import pandas as pd
import matplotlib as ml
from matplotlib import pyplot as plt
################################################################
if sys.platform == 'linux' or sys.platform == ' darwin':
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
GBase = Base+'/01-Vermeulen/06-Report/01-EDS/02-Python/'
ml.style.use('ggplot')

data=[
['London', 29.2, 17.4],
['Glasgow', 18.8, 11.3],
['Cape Town', 15.3, 9.0],
['Houston', 22.0, 7.8],
['Perth', 18.0, 23.7],
['San Francisco', 11.4, 33.3]
]
os_new=pd.DataFrame(data)
pd.Index(['Item', 'Value', 'Value Percent', 'Conversions', 'ConversionPercent',
'URL', 'Stats URL'],dtype='object')
os_new.rename(columns = {0 : "Warehouse Location"}, inplace=True)
os_new.rename(columns = {1 : "Profit 2016"}, inplace=True)
os_new.rename(columns = {2 : "Profit 2017"}, inplace=True)
explode = (0, 0, 0, 0, 0, 0.1)
labels=os_new['Warehouse Location']
colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral',
'lightcyan','lightblue']
os_new.plot(figsize=(10, 10),kind="pie", y="Profit 2017",autopct='%.2f%%', \
shadow=True, explode=explode, legend = False, colors = colors_mine,\
labels=labels, fontsize=20)
sPicNameOut1=GBase+'pie_explode.png'
plt.savefig(sPicNameOut1,dpi=600)
