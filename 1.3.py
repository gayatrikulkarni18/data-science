# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:58:39 2023

@author: Admin
"""

import datetime as dt

#Convert YYYY/MM/DD to DD Month YYYY
baddata = "Data Science with too many spaces is bad!!!"
print('#3 Reformatting data entry to match specific formatting criteria.')
baddata = dt.date(2019,10,31)
baddata=format(baddata,'%Y-%m-%d')
gooddata=dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddata,'%d%B%Y')
print('Bad Data :',baddata)
print('Good Data :',baddata)