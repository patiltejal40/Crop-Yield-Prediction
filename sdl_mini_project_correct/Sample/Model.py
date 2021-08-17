#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


# In[7]:


df = pd.read_csv('updated.csv')
df


# In[8]:



reg = linear_model.LinearRegression()
reg.fit(df[['Crop_Year','Crop','Area']],df.Production)


# In[9]:


import pickle
pickle.dump(reg, open('Model.pkl','wb'))


# In[10]:


model = pickle.load(open('Model.pkl','rb'))

# In[ ]:




