#coding:UTF-8
import re
import sys
import json
import xlrd
import pymongo
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from pymongo import MongoClient, collection

import warnings
warnings.filterwarnings('ignore')

#创建与mongo数据库的连接
client=MongoClient('localhost',12345)
db1=client.diabete
account1=db1.linfeng
db2=client.health  
account2=db2.linfeng

d_age=[]
for item in account1.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        if(item[u'年龄']>20 and item[u'年龄']<107):
            d_age.append(int(item[u'年龄']))            

h_age=[]
for item in account2.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        if(item[u'年龄']>20 and item[u'年龄']<107):
            h_age.append(int(item[u'年龄']))

d_sex=[]
for item in account1.find():
    if item.has_key(u'性别') and item[u'性别']:
        d_sex.append(item[u'性别'])

h_sex=[]
for item in account2.find():
    if item.has_key(u'性别') and item[u'性别']:
        h_sex.append(item[u'性别'])

age=[]
for i in d_age:
    age.append(i)
for i in h_age:
    age.append(i)
sex=[]
for i in d_sex:
    sex.append(i)
for i in h_sex:
    sex.append(i)
condition=[]
for i in d_age:
    condition.append(1)
for i in h_age:
    condition.append(0)
frame1=pd.DataFrame({u"年龄":age})
frame2=pd.DataFrame({u"性别":sex})
frame=frame1.join(frame2)

teen_df = frame[(frame[u'年龄']>20) & (frame1[u'年龄']<= 40)]
mid_df = frame[(frame[u'年龄']>40) & (frame[u'年龄']<= 60)]
midold_df = frame[(frame[u'年龄']>60) & (frame[u'年龄']<= 80)]
old_df= frame[(frame[u'年龄']>80) & (frame[u'年龄']<= 110)]
sns.set(style="whitegrid") 
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(5,5))
plt.subplot(221)
teen_df[u"性别"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'青年')

plt.subplot(222)
mid_df[u"性别"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'中年')

plt.subplot(223)
midold_df[u"性别"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'中老年')

plt.subplot(224)
old_df[u"性别"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'老年')
plt.show()