
# coding: utf-8

# In[5]:


import pandas as pd


# In[2]:


datafile='G:/Dakang/Python/data mining practice/031806450jkj.xls'   #他娘的是反斜杠啊啊啊啊啊啊，给我记住哦！！！！！！


# In[3]:


resultfile='G:/Dakang/Python/data mining practice/explore.xls'


# In[33]:


#-*-coding:utf-8-*-
data=pd.read_excel(datafile,sheet_name='航空公司客户数据',encoding='utf-8')   #记得导入的是哪个sheet


# In[35]:


explore=data.describe(percentiles=[],include='all').T


# In[36]:


explore['null']=len(data)-explore['count']


# In[37]:


explore=explore[['null','max','min']]


# In[38]:


explore.columns=[u'空值数',u'最大值',u'最小值']


# In[39]:


explore.to_excel(resultfile)  #这玩意居然还需要一个其他的包叫xlwt（心理问题）！！！！！


# In[4]:


cleanfile='G:/Dakang/Python/data mining practice/cleaned.xls'


# In[48]:


data=data[data['EXPENSE_SUM_YR_1'].notnull()*data['EXPENSE_SUM_YR_2'].notnull()]


# In[49]:


index1=data['EXPENSE_SUM_YR_1']!=0
index2=data['EXPENSE_SUM_YR_2']!=0
index3=(data['SEG_KM_SUM']==0)&(data['avg_discount']==0)


# In[50]:


data=data[index1|index2|index3]


# In[53]:


data.to_excel(cleanfile)


# In[7]:


cleanfile='G:/Dakang/Python/data mining practice/cleaned.xls'


# In[8]:


zscorefile='G:/Dakang/Python/data mining practice/zscore.xls'


# In[9]:


data=pd.read_excel(cleanfile)


# In[13]:


L=data['LOAD_TIME']-data['FFP_DATE']


# In[14]:


data['L']=L


# In[15]:


print(data)


# In[19]:


data=data.drop(columns=['FFP_DATE','LOAD_TIME'])


# In[20]:


data.columns=['F','M','R','C','L']


# In[22]:


data=data[['L','R','F','M','C']]


# In[23]:


print(data)


# In[24]:


data.to_excel(cleanfile)


# In[25]:


cleanfile='G:/Dakang/Python/data mining practice/cleaned.xls'


# In[26]:


zscorefile='G:/Dakang/Python/data mining practice/zscore.xls'


# In[27]:


data=pd.read_excel(cleanfile)


# In[28]:


data=(data-data.mean(axis=0))/(data.std(axis=0))


# In[29]:


data.colums=['Z'+i for i in data.columns]


# In[30]:


data.to_excel(zscorefile)


# In[32]:


from sklearn.cluster import KMeans


# In[33]:


inputfile='G:/Dakang/Python/data mining practice/zscore.xls'


# In[34]:


k=5


# In[35]:


data=pd.read_excel(inputfile)


# In[36]:


kmodel=KMeans(n_clusters=k,n_jobs=4)
kmodel.fit(data)


# In[38]:


kmodel.cluster_centers_
kmodel.labels_


# In[39]:


kmodel.fit(data)


# In[43]:


kmodel.cluster_centers_


# In[46]:


kmodel.labels_


# In[47]:


kmodel.labels_


# In[48]:


print(kmodel)

