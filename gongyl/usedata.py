import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import getdata as gd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
########################################################################

#数据读取
dataD = gd.getDataD()
#dataH = gd.getDataH()


# ================================================r=============================
# #记录完整性雷达图   
# labels = []
# data = []
# dataLenth = 0
# 
# for i in dataH.columns:
#     labels.append(i)
#     counta = 0
#     countb = 0
#     for j in dataH[i]:
#         if j is None:
#             countb = countb + 1
#         else:
#             counta = counta + 1
#     data.append(counta / (counta+countb))
#     dataLenth = dataLenth + 1
# 
# print(data)
# labels = np.array(labels)
# data = np.array(data)
# 
# angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
# data = np.concatenate((data, [data[0]])) # 闭合
# angles = np.concatenate((angles, [angles[0]])) # 闭合
# 
# fig = plt.figure()
# ax = fig.add_subplot(111, polar=True)# polar参数
# ax.plot(angles, data, 'bo-', linewidth=2)# 画线
# ax.fill(angles, data, facecolor='r', alpha=0.25)# 填充
# ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
# ax.set_title("记录完整性雷达图", va='bottom', fontproperties="SimHei")
# ax.set_rlim(0,1)
# ax.grid(True)
# plt.show()
# 
# #详细指标相关性系数表
# dataA = pd.DataFrame()
# col = ['脉率','呼吸',	'左侧收缩压','左侧舒张压','右侧收缩压','右侧舒张压','空腹血糖',
#        '随机血糖','餐后血糖','总胆固醇','甘油三酯','低密度脂蛋白','高密度脂蛋白',
#        '血清谷丙转氨酶','血清谷草转氨酶','白蛋白','总胆红素','结合胆红素','血清肌酐',
#        '血尿素氮','血钾浓度','血钠浓度','锻炼频率','吸烟情况','饮酒情况','饮酒种类',
#        '皮肤','巩膜','淋巴结','肺桶状胸','肺呼吸音','肺罗音','心脏心率']
# 
# for i in col:
#     dataA[i] = dataH[i]
#   
# #求解相关系数
# data = dataA.corr()
# #print(data)
# fig,ax = plt.subplots(figsize = (9,9))
# sns.heatmap(data,annot = True,vmax = 1,vmin = 0,
#             xticklabels = True,yticklabels = True,
#             square = True,cmap = "YlGnBu")
# 
# ax.set_title('详细指标相关性系数表',fontsize = 15)
# 
# plt.show()
# 
# =============================================================================

#患病种类相关性

temp = pd.DataFrame()
p = [0] * 36
temp['illness'] = p
for i in dataD['慢性病']:
    for j in i:
        if (j != ','):
            j = int(j)
            temp.iloc[j-1,0] = temp.iloc[j-1,0] + 1

temp = list(temp['illness'])

#print(temp)
#[8846, 56138, 118422, 3579, 1625, 258, 799, 777, 389, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 301]

index = np.arange(1,37)

ills = ['无','高血压','糖尿病','冠心病','慢性阻塞性肺疾病','恶性肿瘤','脑卒中','重性精神疾病','结核病','肝炎',
        '其他法定传染病','职业病','其他','','','','','','','',
        '婚检其他','心脏病','肺结核','肝脏病','泌尿生殖系疾病','性病','癫痫', 
        '甲亢','先天疾病','肾脏疾病','贫血','其他','孕12周其他','麻痹','肝脏疾病','孕妇名册其他']

plt.title('慢性病分析')
plt.xticks(index, ills, rotation = 80)
plt.bar(index,temp,width = 0.3,color = 'b')
plt.show()










