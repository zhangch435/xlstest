#coding:UTF-8
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient

import warnings
warnings.filterwarnings('ignore')

#连接数据库    
#两个数据库  taskdb  为患病数据库   health  为健康数据库
client=MongoClient('localhost',27017)
db1=client.taskdb
account1=db1.admin
db2=client.health    
account2=db2.data

################################################################

#年龄分布与患病率的直方图
#将taskdb数据库中的年龄集录入到t_age集合中
t_age=[]
for item in account1.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        if(item[u'年龄']>20 and item[u'年龄']<107):
            t_age.append(int(item[u'年龄']))
            
#将health数据库中的年龄集录入到h_age集合中
h_age=[]
for item in account2.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        if(item[u'年龄']>20 and item[u'年龄']<107):
            h_age.append(int(item[u'年龄']))

age=[]
for i in t_age:
    age.append(i)
for i in h_age:
    age.append(i)
condition=[]
for i in t_age:
    condition.append(1)
for i in h_age:
    condition.append(0)
frame1=pd.DataFrame({u"年龄":age})
frame2=pd.DataFrame({u"患病情况":condition})
frame=frame1.join(frame2)

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 
fig, axis1 = plt.subplots(1,1,figsize=(45,4))
age = frame[[u'年龄',u'患病情况']].groupby([u'年龄'],as_index=False).mean()
sns.barplot(x=u'年龄', y=u'患病情况', data=age)
plt.show()


################################################################
#年龄分布与患病率的关系折线图
#将taskdb数据库中的年龄集录入到t_age集合中

t_age=[0 for i in range(0,95,1)]
for item in account1.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        for i in range(20,95,1):
            if(item[u'年龄']== i):
                t_age[i]=t_age[i]+1
            else:
                continue
            
            
#将health数据库中的年龄集录入到h_age集合中
h_age=[0 for i in range(0,95,1)]
for item in account2.find():
    if item.has_key(u'年龄') and item[u'年龄']:
        for i in range(20,95,1):
            if(item[u'年龄']== i):
                h_age[i]=h_age[i]+1
            else:
                continue
            
aage=[0 for i in range(0,95,1)]
for i in range(20,95):
    aage[i]=t_age[i]+h_age[i]

age=np.arange(0.000,0.095,0.001)
for i in range(0,95,1):
    if aage[i]==0:
        age[i]=float(0)
    else:
        age[i]=float(t_age[i])/float(aage[i])
        
heng=[i for i in range(0,95,1)]
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 
plt.figure(figsize=(8,4)) 
plt.plot(heng,age)
plt.xlabel(u'年龄') #X轴标签  
plt.ylabel(u'占比')  #Y轴标签  
new_ticks = np.linspace( 0,95,20)
plt.xticks(new_ticks)
plt.title(u'各年龄患病人数占本年龄人数比折线图') #图标题  
plt.show()  #显示图  


################################################################

#患病人中性别比例情况饼状图
#将taskdb数据库中的性别集录入到t_sex集合中
t_sex=[]
for item in account1.find():
    if item.has_key(u'性别') and item[u'性别']:
        t_sex.append(item[u'性别'])
h_sex=[]
for item in account2.find():
    if item.has_key(u'性别') and item[u'性别']:
        h_sex.append(item[u'性别'])
sex=[]
for i in t_sex:
    sex.append(i);
for i in h_sex:
    sex.append(i);
sign=[]
for i in t_sex:
    sign.append(1);
for i in h_sex:
    sign.append(0);
    
frame1=pd.DataFrame({u"性别":sex})
frame2=pd.DataFrame({u"患病情况":sign}) 
frame=frame1.join(frame2)

male_df = frame[frame[u'性别'] == u'男']
female_df = frame[frame[u'性别'] == u'女']
sns.set(style="whitegrid") 
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(10,5))
plt.subplot(121)
male_df[u"患病情况"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'男性')

plt.subplot(122)
female_df[u"患病情况"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'女性')
plt.show()



################################################################
#绘体质指标与患病情况的箱型图
#将taskdb数据库中的体质指标集录入到t_zdgc集合中
t_zdgc=[]
for item in account1.find():
    if item.has_key(u'总胆固醇') and item[u'总胆固醇']:
        t_zdgc.append(float(item[u'总胆固醇']))
#将health数据库中的高密度脂蛋白集录入到h_zdgc集合中
h_zdgc=[]
for item in account2.find():
    if item.has_key(u'总胆固醇') and item[u'总胆固醇']:
        h_zdgc.append(float(item[u'总胆固醇'])) 
        
kfxt=[]
for i in t_zdgc:
    kfxt.append(i)
for i in h_zdgc:
    kfxt.append(i)
condition=[]
for i in t_zdgc:
    condition.append(u'患病')
for i in h_zdgc:
    condition.append(u'健康')
frame1=pd.DataFrame({u"患病情况":condition})
frame2=pd.DataFrame({u"总胆固醇":kfxt})
frame=frame1.join(frame2)
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 
plt.figure(figsize=(10,5))
frame.boxplot(column=u'总胆固醇', by=u'患病情况', showfliers=False)
plt.show()

#其余箱型图同理  只改变名称即可


################################################################
#空腹血糖、性别、体重、患病情况小提琴图
#将taskdb数据库中的年龄集录入到t_kfxt集合中
t_kfxt=[]
for item in account1.find():
    if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        t_kfxt.append(item[u'空腹血糖'])
#将health数据库中的年龄集录入到h_kfxt集合中
h_kfxt=[]
for item in account2.find():
    if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        h_kfxt.append(item[u'空腹血糖'])  

#将taskdb数据库中的性别集录入到t_sex集合中
t_sex=[]
for item in account1.find():
    if item.has_key(u'性别') and item[u'性别']:
        t_sex.append(item[u'性别'])
#将health数据库中的年龄集录入到h_age集合中
h_sex=[]
for item in account2.find():
    if item.has_key(u'性别') and item[u'性别']:
        h_sex.append(item[u'性别'])
        
#将taskdb数据库中的吸烟情况集录入到t_weight集合中
t_weight=[]
for item in account1.find():
    if item.has_key(u'体重') and item[u'体重']:
        if(item[u'体重']>110):
            t_weight.append(110)
        elif(item[u'体重']<10):
            t_weight.append(10)
        else:
            t_weight.append(item[u'体重'])
#将health数据库中的吸烟情况集录入到h_weight集合中
h_weight=[]
for item in account2.find():
    if item.has_key(u'体重') and item[u'体重']:
        if(item[u'体重']>110):
            h_weight.append(110)
        elif(item[u'体重']<10):
            h_weight.append(10)
        else:
            h_weight.append(item[u'体重'])     
            
#分别合并kfxt集合、sex集合、weight集合以及生成condition集合表示患病个体
kfxt=[]
for i in t_kfxt:
    tzzb.append(i)
for i in h_kfxt:
    tzzb.append(i)
sex=[]
for i in t_sex:
    sex.append(i)
for i in h_sex:
    sex.append(i)
weight=[]
for i in t_weight:
    weight.append(i)
for i in h_weight:
    weight.append(i)
condition=[]
for i in t_sex:
    condition.append(1)
for i in h_sex:
    condition.append(0)
    
#将三个数组转化为dataframe格式并合并
frame1=pd.DataFrame({u"性别":sex})
frame2=pd.DataFrame({u"空腹血糖":kfxt})
frame3=pd.DataFrame({u"体重":weight})
frame4=pd.DataFrame({u"患病情况":condition})
frame5=frame1.join(frame2)
frame6=frame5.join(frame3)
frame=frame6.join(frame4)

#空腹血糖、体重、年龄、性别与患病率与否的关系
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 
fig, ax = plt.subplots(1, 2, figsize = (18, 16))
sns.violinplot(u"性别",u"空腹血糖", hue=u"患病情况", data=frame,palette="muted",split=True,ax=ax[0])
ax[0].set_title(u'空腹血糖、性别、患病关系')
ax[0].set_yticks(range(0, 20, 5))
sns.violinplot(u"性别",u"体重", hue=u"患病情况", data=frame,palette="muted",split=True,ax=ax[1])
ax[1].set_title(u'体重、性别与患病与否的关系')
ax[1].set_yticks(range(0, 110, 10))
plt.show()
