#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv("netflix_data.csv")
df


# In[2]:


df.insert(5,"num_of_cast"," ")
df


# In[11]:


df.groupby('type').size()


# In[ ]:




