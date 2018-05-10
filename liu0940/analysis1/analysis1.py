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
client=MongoClient('localhost',27017)
db1=client.diabete
account1=db1.liuzhe
db2=client.health    
account2=db2.liuzhe




##体重、体质指标、性别与患病率与否的关系----小提琴图
##将diabete数据库中的年龄集录入到d_tzzb集合中
#d_tzzb=[]
#for item in account1.find():
    #if item.has_key(u'体质指标') and item[u'体质指标']:
        #if(item[u'体质指标']>40):
            #d_tzzb.append(40)
        #elif(item[u'体质指标']<0):
            #d_tzzb.append(0)
        #else:
            #d_tzzb.append(item[u'体质指标'])
##将health数据库中的年龄集录入到h_tzzb集合中
#h_tzzb=[]
#for item in account2.find():
    #if item.has_key(u'体质指标') and item[u'体质指标']:
        #if(item[u'体质指标']>40):
            #h_tzzb.append(40)
        #elif(item[u'体质指标']<0):
            #h_tzzb.append(0)
        #else:
            #h_tzzb.append(item[u'体质指标'])  

##将diabete数据库中的性别集录入到d_sex集合中
#d_sex=[]
#for item in account1.find():
    #if item.has_key(u'性别') and item[u'性别']:
        #d_sex.append(item[u'性别'])
##将health数据库中的年龄集录入到h_age集合中
#h_sex=[]
#for item in account2.find():
    #if item.has_key(u'性别') and item[u'性别']:
        #h_sex.append(item[u'性别'])
        
##将diabete数据库中的吸烟情况集录入到d_weight集合中
#d_weight=[]
#for item in account1.find():
    #if item.has_key(u'体重') and item[u'体重']:
        #if(item[u'体重']>110):
            #d_weight.append(110)
        #elif(item[u'体重']<10):
            #d_weight.append(10)
        #else:
            #d_weight.append(item[u'体重'])
##将health数据库中的吸烟情况集录入到h_weight集合中
#h_weight=[]
#for item in account2.find():
    #if item.has_key(u'体重') and item[u'体重']:
        #if(item[u'体重']>110):
            #h_weight.append(110)
        #elif(item[u'体重']<10):
            #h_weight.append(10)
        #else:
            #h_weight.append(item[u'体重'])     
            
##分别合并tzzb集合、sex集合、weight集合以及生成condition集合表示患病个体
#tzzb=[]
#for i in d_tzzb:
    #tzzb.append(i)
#for i in h_tzzb:
    #tzzb.append(i)
#sex=[]
#for i in d_sex:
    #sex.append(i)
#for i in h_sex:
    #sex.append(i)
#weight=[]
#for i in d_weight:
    #weight.append(i)
#for i in h_weight:
    #weight.append(i)
#condition=[]
#for i in d_sex:
    #condition.append(1)
#for i in h_sex:
    #condition.append(0)
    
##将三个数组转化为dataframe格式并合并
#frame1=pd.DataFrame({u"性别":sex})
#frame2=pd.DataFrame({u"体质指标":tzzb})
#frame3=pd.DataFrame({u"体重":weight})
#frame4=pd.DataFrame({u"患病情况":condition})
#frame5=frame1.join(frame2)
#frame6=frame5.join(frame3)
#frame=frame6.join(frame4)

##体重、年龄、性别与患病率与否的关系
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#fig, ax = plt.subplots(1, 2, figsize = (18, 16))
#sns.violinplot(u"性别",u"体质指标", hue=u"患病情况", data=frame,palette="muted",split=True,ax=ax[0])
#ax[0].set_title(u'体质指标、性别与患病与否的关系')
#ax[0].set_yticks(range(0, 50, 10))
#sns.violinplot(u"性别",u"体重", hue=u"患病情况", data=frame,palette="muted",split=True,ax=ax[1])
#ax[1].set_title(u'体重、性别与患病与否的关系')
#ax[1].set_yticks(range(0, 110, 10))
#plt.show()





###挑选一些主要的特征，生成特征之间的关联图，查看特征与特征之间的相关性：相关性图
####将diabete数据库中的血清肌酐集录入到d_xqjg集合中
###d_xqjg=[]
###for item in account1.find():
    ###if item.has_key(u'血清肌酐') and item[u'血清肌酐']:
        ###d_xqjg.append(float(item[u'血清肌酐']))
####将health数据库中的血清肌酐集录入到h_xqjg集合中
###h_xqjg=[]
###for item in account2.find():
    ###if item.has_key(u'血清肌酐') and item[u'血清肌酐']:
        ###h_xqjg.append(float(item[u'血清肌酐']))
        
###将diabete数据库中的右侧舒张压集录入到d_ycszy集合中
##d_ycszy=[]
##for item in account1.find():
    ##if item.has_key(u'右侧舒张压') and item[u'右侧舒张压']:
        ##d_ycszy.append(float(item[u'右侧舒张压']))
###将health数据库中的右侧舒张压集录入到h_ycszy集合中
##h_ycszy=[]
##for item in account2.find():
    ##if item.has_key(u'右侧舒张压') and item[u'右侧舒张压']:
        ##h_ycszy.append(float(item[u'右侧舒张压']))
        
####将diabete数据库中的白蛋白集录入到d_bdb集合中
###d_bdb=[]
###for item in account1.find():
    ###if item.has_key(u'白蛋白') and item[u'白蛋白']:
        ###d_bdb.append(float(item[u'白蛋白']))
####将health数据库中的白蛋白集录入到h_bdb集合中
###h_bdb=[]
###for item in account2.find():
    ###if item.has_key(u'白蛋白') and item[u'白蛋白']:
        ###h_bdb.append(float(item[u'白蛋白']))
        
####将diabete数据库中的低密度脂蛋白集录入到d_dmdzdb集合中
###d_dmdzdb=[]
###for item in account1.find():
    ###if item.has_key(u'低密度脂蛋白') and item[u'低密度脂蛋白']:
        ###d_dmdzdb.append(float(item[u'低密度脂蛋白']))
####将health数据库中的低密度脂蛋白集录入到h_dmdzdb集合中
###h_dmdzdb=[]
###for item in account2.find():
    ###if item.has_key(u'低密度脂蛋白') and item[u'低密度脂蛋白']:
        ###h_dmdzdb.append(float(item[u'低密度脂蛋白']))
        
###将diabete数据库中的左侧收缩压集录入到d_zcssy集合中
##d_zcssy=[]
##for item in account1.find():
    ##if item.has_key(u'左侧收缩压') and item[u'左侧收缩压']:
        ##d_zcssy.append(float(item[u'左侧收缩压']))
###将health数据库中的左侧收缩压集录入到h_zcssy集合中
##h_zcssy=[]
##for item in account2.find():
    ##if item.has_key(u'左侧收缩压') and item[u'左侧收缩压']:
        ##h_zcssy.append(float(item[u'左侧收缩压']))  
        
####将diabete数据库中的甘油三酯集录入到d_gysz集合中
###d_gysz=[]
###for item in account1.find():
    ###if item.has_key(u'甘油三酯') and item[u'甘油三酯']:
        ###d_gysz.append(float(item[u'甘油三酯']))
####将health数据库中的甘油三酯集录入到h_gysz集合中
###h_gysz=[]
###for item in account2.find():
    ###if item.has_key(u'甘油三酯') and item[u'甘油三酯']:
        ###h_gysz.append(float(item[u'甘油三酯']))
        
####将diabete数据库中的总胆红素集录入到d_zdhs集合中
###d_zdhs=[]
###for item in account1.find():
    ###if item.has_key(u'总胆红素') and item[u'总胆红素']:
        ###d_zdhs.append(float(item[u'总胆红素']))
####将health数据库中的总胆红素集录入到h_zdhs集合中
###h_zdhs=[]
###for item in account2.find():
    ###if item.has_key(u'总胆红素') and item[u'总胆红素']:
        ###h_zdhs.append(float(item[u'总胆红素']))
        
###将diabete数据库中的右侧收缩压集录入到d_ycssy集合中
##d_ycssy=[]
##for item in account1.find():
    ##if item.has_key(u'右侧收缩压') and item[u'右侧收缩压']:
        ##d_ycssy.append(float(item[u'右侧收缩压']))
###将health数据库中的右侧收缩压集录入到h_ycssy集合中
##h_ycssy=[]
##for item in account2.find():
    ##if item.has_key(u'右侧收缩压') and item[u'右侧收缩压']:
        ##h_ycssy.append(float(item[u'右侧收缩压']))
        
####将diabete数据库中的总胆固醇集录入到d_zdgc集合中
###d_zdgc=[]
###for item in account1.find():
    ###if item.has_key(u'总胆固醇') and item[u'总胆固醇']:
        ###d_zdgc.append(float(item[u'总胆固醇']))
####将health数据库中的总胆固醇集录入到h_zdgc集合中
###h_zdgc=[]
###for item in account2.find():
    ###if item.has_key(u'总胆固醇') and item[u'总胆固醇']:
        ###h_zdgc.append(float(item[u'总胆固醇'])) 
        
###将diabete数据库中的左侧舒张压集录入到d_zcszy集合中
##d_zcszy=[]
##for item in account1.find():
    ##if item.has_key(u'左侧舒张压') and item[u'左侧舒张压']:
        ##d_zcszy.append(float(item[u'左侧舒张压']))
###将health数据库中的总胆固醇集录入到h_zcszy集合中
##h_zcszy=[]
##for item in account2.find():
    ##if item.has_key(u'左侧舒张压') and item[u'左侧舒张压']:
        ##h_zcszy.append(float(item[u'左侧舒张压'])) 
        
###将diabete数据库中的心脏心率集录入到d_xzxl集合中
##d_xzxl=[]
##for item in account1.find():
    ##if item.has_key(u'心脏心率') and item[u'心脏心率']:
        ##d_xzxl.append(float(item[u'心脏心率']))
###将health数据库中的心脏心率集录入到h_xzxl集合中
##h_xzxl=[]
##for item in account2.find():
    ##if item.has_key(u'心脏心率') and item[u'心脏心率']:
        ##h_xzxl.append(float(item[u'心脏心率'])) 
        
####将diabete数据库中的高密度脂蛋白集录入到d_gmdzdb集合中
###d_gmdzdb=[]
###for item in account1.find():
    ###if item.has_key(u'高密度脂蛋白') and item[u'高密度脂蛋白']:
        ###d_gmdzdb.append(float(item[u'高密度脂蛋白']))
####将health数据库中的高密度脂蛋白集录入到h_gmdzdb集合中
###h_gmdzdb=[]
###for item in account2.find():
    ###if item.has_key(u'高密度脂蛋白') and item[u'高密度脂蛋白']:
        ###h_gmdzdb.append(float(item[u'高密度脂蛋白'])) 
        
###将diabete数据库中的空腹血糖集录入到d_kfxt集合中
##d_kfxt=[]
##for item in account1.find():
    ##if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        ##d_kfxt.append(float(item[u'空腹血糖']))
###将health数据库中的高密度脂蛋白集录入到h_kfxt集合中
##h_kfxt=[]
##for item in account2.find():
    ##if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        ##h_kfxt.append(float(item[u'空腹血糖'])) 
        
####将diabete数据库中的脉率集录入到d_ml集合中
###d_ml=[]
###for item in account1.find():
    ###if item.has_key(u'脉率') and item[u'脉率']:
        ###d_ml.append(float(item[u'脉率']))
####将health数据库中的脉率集录入到h_ml集合中
###h_ml=[]
###for item in account2.find():
    ###if item.has_key(u'脉率') and item[u'脉率']:
        ###h_ml.append(float(item[u'脉率'])) 
        
####将diabete数据库中的血小板集录入到d_xxb集合中
###d_xxb=[]
###for item in account1.find():
    ###if item.has_key(u'血小板') and item[u'血小板']:
        ###d_xxb.append((item[u'血小板'])
####将health数据库中的血小板集录入到h_xxb集合中
###h_xxb=[]
###for item in account2.find():
    ###if item.has_key(u'血小板') and item[u'血小板']:
        ###h_xxb.append(item[u'血小板'])
        
####将diabete数据库中的白细胞集录入到d_bxb集合中
###d_bxb=[]
###for item in account1.find():
    ###if item.has_key(u'白细胞') and item[u'白细胞']:
        ###d_bxb.append(float(item[u'白细胞']))
####将health数据库中的白细胞集录入到h_bxb集合中
###h_bxb=[]
###for item in account2.find():
    ###if item.has_key(u'白细胞') and item[u'白细胞']:
        ###h_bxb.append(float(item[u'白细胞'])) 
        
####将diabete数据库中的血红蛋白集录入到d_xhdb集合中
###d_xhdb=[]
###for item in account1.find():
    ###if item.has_key(u'血红蛋白') and item[u'血红蛋白']:
        ###d_xhdb.append(float(item[u'血红蛋白']))
####将health数据库中的血红蛋白集录入到h_xhdb集合中
###h_xhdb=[]
###for item in account2.find():
    ###if item.has_key(u'血红蛋白') and item[u'血红蛋白']:
        ###h_xhdb.append(float(item[u'血红蛋白'])) 
        
####将diabete数据库中的血尿素氮集录入到d_xnsd集合中
###d_xnsd=[]
###for item in account1.find():
    ###if item.has_key(u'血尿素氮') and item[u'血尿素氮']:
        ###d_xnsd.append(float(item[u'血尿素氮']))
####将health数据库中的血尿素氮集录入到h_xnsd集合中
###h_xnsd=[]
###for item in account2.find():
    ###if item.has_key(u'血尿素氮') and item[u'血尿素氮']:
        ###h_xnsd.append(float(item[u'血尿素氮'])) 
        
###xqjg=[]
###for i in d_xqjg:
    ###xqjg.append(i)
###for i in h_xqjg:
    ###xqjg.append(i)
    
##condition=[]
##for i in d_zcszy:
    ##condition.append(1)
##for i in h_zcszy:
    ##condition.append(0)
    
##ycszy=[]
##for i in d_ycszy:
    ##ycszy.append(i)
##for i in h_ycszy:
    ##ycszy.append(i)
    
###bdb=[]
###for i in d_bdb:
    ###bdb.append(i)
###for i in h_bdb:
    ###bdb.append(i)

###dmdzdb=[]
###for i in d_dmdzdb:
    ###dmdzdb.append(i)
###for i in h_dmdzdb:
    ###dmdzdb.append(i)

##zcssy=[]
##for i in d_zcssy:
    ##zcssy.append(i)
##for i in h_zcssy:
    ##zcssy.append(i)

###gysz=[]
###for i in d_gysz:
    ###gysz.append(i)
###for i in h_gysz:
    ###gysz.append(i)

###zdhs=[]
###for i in d_zdhs:
    ###zdhs.append(i)
###for i in h_zdhs:
    ###zdhs.append(i)
    
##ycssy=[]
##for i in d_ycssy:
    ##ycssy.append(i)
##for i in h_ycssy:
    ##ycssy.append(i)

###zdgc=[]
###for i in d_zdgc:
    ###zdgc.append(i)
###for i in h_zdgc:
    ###zdgc.append(i)

##zcszy=[]
##for i in d_zcszy:
    ##zcszy.append(i)
##for i in h_zcszy:
    ##zcszy.append(i)

##xzxl=[]
##for i in d_xzxl:
    ##xzxl.append(i)
##for i in h_xzxl:
    ##xzxl.append(i)

###gmdzdb=[]
###for i in d_gmdzdb:
    ###gmdzdb.append(i)
###for i in h_gmdzdb:
    ###gmdzdb.append(i)

##kfxt=[]
##for i in d_kfxt:
    ##kfxt.append(i)
##for i in h_kfxt:
    ##kfxt.append(i)

###ml=[]
###for i in d_ml:
    ###ml.append(i)
###for i in h_ml:
    ###ml.append(i)

###xxb=[]
###for i in d_xxb:
    ###xxb.append(i)
###for i in h_xxb:
    ###xxb.append(i)

###bxb=[]
###for i in d_bxb:
    ###bxb.append(i)
###for i in h_bxb:
    ###bxb.append(i)

###xhdb=[]
###for i in d_xhdb:
    ###xhdb.append(i)
###for i in h_xhdb:
    ###xhdb.append(i)

###xnsd=[]
###for i in d_xnsd:
    ###xnsd.append(i)
###for i in h_xnsd:
    ###xnsd.append(i)
   
##frame0=pd.DataFrame({u"患病情况":condition})
###frame1=pd.DataFrame({u"血清肌酐":xqjg})
##frame2=pd.DataFrame({u"右侧舒张压":ycszy})
###frame3=pd.DataFrame({u"白蛋白":bdb})
###frame4=pd.DataFrame({u"低密度脂蛋白":dmdzdb})
##frame5=pd.DataFrame({u"左侧收缩压":zcssy})
###frame6=pd.DataFrame({u"甘油三酯":gysz})
###frame7=pd.DataFrame({u"总胆红素":zdhs})
##frame8=pd.DataFrame({u"右侧收缩压":ycssy})
###frame9=pd.DataFrame({u"总胆固醇":zdgc})
##frame10=pd.DataFrame({u"左侧舒张压":zcszy})
##frame11=pd.DataFrame({u"心脏心率":xzxl})
###frame12=pd.DataFrame({u"高密度脂蛋白":gmdzdb})
##frame13=pd.DataFrame({u"空腹血糖":kfxt})
###frame14=pd.DataFrame({u"脉率":ml})
###frame15=pd.DataFrame({u"血小板":xxb})
###frame16=pd.DataFrame({u"白细胞":bxb})
###frame17=pd.DataFrame({u"血红蛋白":xhdb})
###frame18=pd.DataFrame({u"血尿素氮":xnsd})

##f1=frame0.join(frame2)
###f2=f1.join(frame2)
###f3=f2.join(frame3)
###f4=f3.join(frame4)
##f5=f1.join(frame5)
###f6=f5.join(frame6)
###f7=f6.join(frame7)
##f8=f5.join(frame8)
###f9=f8.join(frame9)
##f10=f8.join(frame10)
##f11=f10.join(frame11)
###f12=f11.join(frame12)
##frame=f11.join(frame13)
###f14=f13.join(frame14)
###f15=f14.join(frame15)
###f16=f15.join(frame16)
###frame=f13.join(frame17)
###frame=f17.join(frame18)

##from pylab import *
##mpl.rcParams['font.sans-serif'] = ['SimHei']
##mpl.rcParams['axes.unicode_minus'] = False 
##plt.figure(figsize=(10,10)) 
##Correlation = frame
##colormap = plt.cm.viridis
##plt.title(u'各特征之间的相关性分析', y=1.05, size=15)
##sns.heatmap(Correlation.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
##plt.show()


##做出年龄分布与患病率的关系
##将diabete数据库中的年龄集录入到d_age集合中
#d_age=[]
#for item in account1.find():
    #if item.has_key(u'年龄') and item[u'年龄']:
        #if(item[u'年龄']>20 and item[u'年龄']<107):
            #d_age.append(int(item[u'年龄']))
            
##将health数据库中的年龄集录入到h_age集合中
#h_age=[]
#for item in account2.find():
    #if item.has_key(u'年龄') and item[u'年龄']:
        #if(item[u'年龄']>20 and item[u'年龄']<107):
            #h_age.append(int(item[u'年龄']))

#age=[]
#for i in d_age:
    #age.append(i)
#for i in h_age:
    #age.append(i)
#condition=[]
#for i in d_age:
    #condition.append(1)
#for i in h_age:
    #condition.append(0)
#frame1=pd.DataFrame({u"年龄":age})
#frame2=pd.DataFrame({u"患病情况":condition})
#frame=frame1.join(frame2)

#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#fig, axis1 = plt.subplots(1,1,figsize=(45,4))
#age = frame[[u'年龄',u'患病情况']].groupby([u'年龄'],as_index=False).mean()
#sns.barplot(x=u'年龄', y=u'患病情况', data=age)
##axis1.set_xticks(range(0,110,10))
#plt.show()




##吸烟、喝酒情况对患病情况的影响
##将diabete数据库中的吸烟情况集录入到d_smoke集合中
#d_smoke=[]
#for item in account1.find():
    #if item.has_key(u'吸烟情况') and item[u'吸烟情况']:
        #d_smoke.append(item[u'吸烟情况'])
            
##将health数据库中的吸烟情况集录入到h_smoke集合中
#h_smoke=[]
#for item in account2.find():
    #if item.has_key(u'吸烟情况') and item[u'吸烟情况']:
        #h_smoke.append(item[u'吸烟情况'])

#smoke=[]
#for i in d_smoke:
    #smoke.append(i)
#for i in h_smoke:
    #smoke.append(i)
#condition=[]
#for i in d_smoke:
    #condition.append(1)
#for i in h_smoke:
    #condition.append(0)
#frame1=pd.DataFrame({u"吸烟情况":smoke})
#frame2=pd.DataFrame({u"患病情况":condition})
#frame=frame1.join(frame2)

#sibsp_df = frame[frame[u"患病情况"] != 0]
#no_sibsp_df = frame[frame[u"患病情况"] == 0]
#sns.set(style="whitegrid") 
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 

#plt.figure(figsize=(10,5))
#plt.subplot(121)
#sibsp_df[u"吸烟情况"].value_counts().plot.pie(autopct = '%1.1f%%')
#plt.xlabel(u'患病')

#plt.subplot(122)
#no_sibsp_df[u"吸烟情况"].value_counts().plot.pie(autopct = '%1.1f%%')
#plt.xlabel(u'不患病')

#plt.show()


#将diabete数据库中的饮酒情况集录入到d_drink集合中
d_drink=[]
for item in account1.find():
    if item.has_key(u'饮酒情况') and item[u'饮酒情况']:
        d_drink.append(item[u'饮酒情况'])
            
#将health数据库中的吸烟情况集录入到h_drink集合中
h_drink=[]
for item in account2.find():
    if item.has_key(u'饮酒情况') and item[u'饮酒情况']:
        h_drink.append(item[u'饮酒情况'])

drink=[]
for i in d_drink:
    drink.append(i)
for i in h_drink:
    drink.append(i)
condition=[]
for i in d_drink:
    condition.append(1)
for i in h_drink:
    condition.append(0)
frame1=pd.DataFrame({u"饮酒情况":drink})
frame2=pd.DataFrame({u"患病情况":condition})
frame=frame1.join(frame2)

sibsp_df = frame[frame[u"患病情况"] != 0]
no_sibsp_df = frame[frame[u"患病情况"] == 0]
sns.set(style="whitegrid") 
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(10,5))
plt.subplot(121)
sibsp_df[u"饮酒情况"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'患病')

plt.subplot(122)
no_sibsp_df[u"饮酒情况"].value_counts().plot.pie(autopct = '%1.1f%%')
plt.xlabel(u'不患病')

plt.show()

##绘制空腹血糖与患病情况的箱型图
##将diabete数据库中的空腹血糖集录入到d_kfxt集合中
#d_kfxt=[]
#for item in account1.find():
    #if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        #d_kfxt.append(float(item[u'空腹血糖']))
##将health数据库中的高密度脂蛋白集录入到h_kfxt集合中
#h_kfxt=[]
#for item in account2.find():
    #if item.has_key(u'空腹血糖') and item[u'空腹血糖']:
        #h_kfxt.append(float(item[u'空腹血糖'])) 
        
#kfxt=[]
#for i in d_kfxt:
    #kfxt.append(i)
#for i in h_kfxt:
    #kfxt.append(i)
#condition=[]
#for i in d_kfxt:
    #condition.append(1)
#for i in h_kfxt:
    #condition.append(0)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"空腹血糖":kfxt})
#frame=frame1.join(frame2)
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#plt.figure(figsize=(10,5))
#frame.boxplot(column=u'空腹血糖', by=u'患病情况', showfliers=False)
#plt.show()


#绘制身高与腰围_患病情况的覆盖型曲线图
##将diabete数据库中的身高集录入到d_sg集合中
#d_sg=[]
#for item in account1.find():
    #if item.has_key(u'身高') and item[u'身高']:
        #if(item[u'身高']>50 and item[u'身高']<200):
            #d_sg.append(float(item[u'身高']))
##将health数据库中的高密度脂蛋白集录入到h_sg集合中
#h_sg=[]
#for item in account2.find():
    #if item.has_key(u'身高') and item[u'身高']:
        #if(item[u'身高']>50 and item[u'身高']<200):
            #h_sg.append(float(item[u'身高'])) 
        
#sg=[]
#for i in d_sg:
    #sg.append(i)
#for i in h_sg:
    #sg.append(i)
#condition=[]
#for i in d_sg:
    #condition.append(1)
#for i in h_sg:
    #condition.append(0)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"身高":sg})
#frame=frame1.join(frame2)
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#facet = sns.FacetGrid(frame, hue=u"患病情况",aspect=4)
#facet.map(sns.kdeplot,u'身高',shade= True)
#facet.set(xlim=(120, frame[u'身高'].max()))
#facet.add_legend()
#plt.show()
#将diabete数据库中的身高集录入到d_yw集合中
#d_yw=[]
#for item in account1.find():
    #if item.has_key(u'腰围') and item[u'腰围']:
        #if(item[u'腰围']>50 and item[u'腰围']<120):
            #d_yw.append(float(item[u'腰围']))
##将health数据库中的高密度脂蛋白集录入到h_sg集合中
#h_yw=[]
#for item in account2.find():
    #if item.has_key(u'腰围') and item[u'腰围']:
        #if(item[u'腰围']>00 and item[u'腰围']<120):
            #h_yw.append(float(item[u'腰围'])) 
        
#yw=[]
#for i in d_yw:
    #yw.append(i)
#for i in h_yw:
    #yw.append(i)
#condition=[]
#for i in d_yw:
    #condition.append(1)
#for i in h_yw:
    #condition.append(0)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"腰围":yw})
#frame=frame1.join(frame2)
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#facet = sns.FacetGrid(frame, hue=u"患病情况",aspect=4)
#facet.map(sns.kdeplot,u'腰围',shade= True)
#facet.set(xlim=(10, frame[u'腰围'].max()))
#facet.add_legend()
#plt.show()
##将diabete数据库中的身高集录入到d_xzxl集合中
#d_xzxl=[]
#for item in account1.find():
    #if item.has_key(u'心脏心率') and item[u'心脏心率']:
        #if(item[u'心脏心率']>00 and item[u'心脏心率']<120):
            #d_xzxl.append(float(item[u'心脏心率']))
##将health数据库中的高密度脂蛋白集录入到h_xzxl集合中
#h_xzxl=[]
#for item in account2.find():
    #if item.has_key(u'心脏心率') and item[u'心脏心率']:
        #if(item[u'心脏心率']>00 and item[u'心脏心率']<120):
            #h_xzxl.append(float(item[u'心脏心率'])) 
        
#xzxl=[]
#for i in d_xzxl:
    #xzxl.append(i)
#for i in h_xzxl:
    #xzxl.append(i)
#condition=[]
#for i in d_xzxl:
    #condition.append(1)
#for i in h_xzxl:
    #condition.append(0)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"心脏心率":xzxl})
#frame=frame1.join(frame2)
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#facet = sns.FacetGrid(frame, hue=u"患病情况",aspect=4)
#facet.map(sns.kdeplot,u'心脏心率',shade= True)
#facet.set(xlim=(10, frame[u'心脏心率'].max()))
#facet.add_legend()
#plt.show()
##将diabete数据库中的脉率集录入到d_ml集合中
#d_ml=[]
#for item in account1.find():
    #if item.has_key(u'脉率') and item[u'脉率']:
        #if(item[u'脉率']>0 and item[u'脉率']<120):
            #d_ml.append(float(item[u'脉率']))
##将health数据库中的脉率集录入到h_ml集合中
#h_ml=[]
#for item in account2.find():
    #if item.has_key(u'脉率') and item[u'脉率']:
        #if(item[u'脉率']>0 and item[u'脉率']<120):
            #h_ml.append(float(item[u'脉率'])) 
        
#ml=[]
#for i in d_ml:
    #ml.append(i)
#for i in h_ml:
    #ml.append(i)
#condition=[]
#for i in d_ml:
    #condition.append(1)
#for i in h_ml:
    #condition.append(0)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"脉率":ml})
#frame=frame1.join(frame2)
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 
#facet = sns.FacetGrid(frame, hue=u"患病情况",aspect=4)
#facet.map(sns.kdeplot,u'脉率',shade= True)
#facet.set(xlim=(10, frame[u'脉率'].max()))
#facet.add_legend()
#plt.show()

##联合分布:厨房燃料、厕所
##将diabete数据库中的厨房燃料集录入到d_cfrl集合中
#d_cfrl=[]
#for item in account1.find():
    #if item.has_key(u'厨房燃料') and item[u'厨房燃料']:
            #d_cfrl.append(item[u'厨房燃料'])
##将health数据库中的厨房燃料集录入到h_cfrl集合中
#h_cfrl=[]
#for item in account2.find():
    #if item.has_key(u'厨房燃料') and item[u'厨房燃料']:
            #h_cfrl.append(item[u'厨房燃料'])
###将diabete数据库中的厕所集录入到d_cs集合中
##d_cs=[]
##for item in account1.find():
    ##if item.has_key(u'厕所') and item[u'厕所']:
            ##d_cs.append(item[u'厕所'])
###将health数据库中的厨房燃料集录入到h_cs集合中
##h_cs=[]
##for item in account2.find():
    ##if item.has_key(u'厕所') and item[u'厕所']:
            ##h_cs.append(item[u'厕所'])
##cs=[]
##for i in d_cs:
    ##cs.append(i)
##for i in h_cs:
    ##cs.append(i)
#condition=[]
#for i in d_cfrl:
    #condition.append(1)
#for i in h_cfrl:
    #condition.append(0)
#cfrl=[]
#for i in d_cfrl:
    #cfrl.append(i)
#for i in h_cfrl:
    #cfrl.append(i)
#frame1=pd.DataFrame({u"患病情况":condition})
#frame2=pd.DataFrame({u"厨房燃料":cfrl})
##frame2=pd.DataFrame({u"厕所":cs})
#frame=frame1.join(frame2)
##frame=f1.join(frame3)

#sibsp_df = frame[frame[u"患病情况"] != 0]
#no_sibsp_df = frame[frame[u"患病情况"] == 0]
#sns.set(style="whitegrid") 
#from pylab import *
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#mpl.rcParams['axes.unicode_minus'] = False 

#plt.figure(figsize=(10,5))
#plt.subplot(121)
#sibsp_df[u"厨房燃料"].value_counts().plot.pie(autopct = '%1.1f%%')
#plt.xlabel(u'患病')

#plt.subplot(122)
#no_sibsp_df[u"厨房燃料"].value_counts().plot.pie(autopct = '%1.1f%%')
#plt.xlabel(u'不患病')

#plt.show()