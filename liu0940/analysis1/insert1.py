import xlrd
import sys
import json
import pymongo
from pymongo import MongoClient

#连接数据库
client=MongoClient('localhost',27017)
db1=client.diabete
account1=db1.liuzhe
data1=xlrd.open_workbook('data\diabete.xlsx')
table1=data1.sheets()[0]
#读取excel第一行数据作为存入mongodb的字段名
rowstag=table1.row_values(0)
nrows=table1.nrows
ncols=table1.ncols
print nrows
returnData={}
for i in range(1,nrows):
    #将字段名和excel数据存储为字典形式，并转换为json格式
    returnData[i]=json.dumps(dict(zip(rowstag,table1.row_values(i))))
    #通过编解码还原数据
    returnData[i]=json.loads(returnData[i])
    print returnData[i]
    account1.insert(returnData[i])
    
db2=client.health    
account2=db2.liuzhe
data2=xlrd.open_workbook('data\health.xlsx')
table2=data2.sheets()[0]
#读取excel第一行数据作为存入mongodb的字段名
rowstag=table2.row_values(0)
nrows=table2.nrows
ncols=table2.ncols
print nrows
returnData={}
for i in range(1,nrows):
    #将字段名和excel数据存储为字典形式，并转换为json格式
    returnData[i]=json.dumps(dict(zip(rowstag,table2.row_values(i))))
    #通过编解码还原数据
    returnData[i]=json.loads(returnData[i])
    print returnData[i]
    account2.insert(returnData[i])