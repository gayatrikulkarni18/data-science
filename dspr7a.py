#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
import os
import pandas as pd
import sqlite3 as sq
if sys.platform == 'linux':
    Base=os.path.expanduser('~')
else:
    Base='D:\practical-data-science-master\VKHCG'
    print('Working Base :' ,Base, 'using', sys.platform)
    sDataWarehouseDir=Base + '/99-DW'
    if not os.path.exists(sDataWarehouseDir):
        os.markedirs(sDataWarehouseDir)
sDatabaseName=sDataWarehouseDir +'/datawarehouse.db'
conn1 = sq.connect(sDatabaseName)
sDatabaseName=sDataWarehouseDir +'/datamart.db'
conn2 = sq.connect(sDatabaseName)  


# In[10]:


print('--------------------')
sTable = 'Dim-BMI'
print('Loading :' ,sDatabaseName, '\nTable:' ,sTable)
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
print(PersonFrame0)
print('---------------')


# In[11]:


sTable ='Dim-BMI'
print('Loading :', sDatabaseName,'Table:',sTable)
print('---------------------------')
sSQL="SELECT PersonID,      Height,      Weight,      bmi,      Indicator   FROM [Dim-BMI]   WHERE   Height > 1.5   and Indicator =1   ORDER BY          Height,        Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
DimPerson=PersonFrame1
print(PersonFrame1)


# In[15]:


DimPersonIndex=DimPerson.set_index(['PersonID'],inplace=False)
sTable = 'Dim-BMI-Horizontal'
print('------------------------------')
print('Storing :', sDatabaseName,'\n Table:' ,sTable)
print('------------------------------')
DimPersonIndex.to_sql(sTable, conn2, if_exists="replace")
print('------------------------------')


# In[17]:


sTable = 'Dim-BMI-Horizontal'
print('------------------------------')
print('Loading :', sDatabaseName,' Table:' ,sTable)
print('------------------------------')
sSQL="SELECT * FROM [Dim-BMI];"
PersonFrame2=pd.read_sql_query(sSQL, conn2)
print('------------------------------')


# In[18]:


print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columnss):', PersonFrame0.shape[1])
print('------------------------------')
print('Horizontal Data Set (Rows):', PersonFrame2.shape[0])
print('Horizontal Data Set (Columns):', PersonFrame2.shape[1])


# In[ ]:




