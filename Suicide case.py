#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()


# In[2]:


import pandas_profiling


# In[3]:


import sys
get_ipython().system('{sys.executable} -m pip install pandas-profiling')


# In[12]:


sus_data = pd.read_csv("C:\\Users\\Acer\\Downloads\\archive\\master.csv")


# In[14]:


sus_data.head()


# In[16]:


sus_data.shape


# In[17]:


sus_data.columns


# In[18]:


sus_data.describe(include = "all")


# In[19]:


sus_data.describe()


# In[20]:


sus_data.info()


# In[24]:


sus_data.groupby('year')['suicides_no'].count().sort_values(ascending = False)


# In[21]:


sus_data


# In[27]:


sus_data.groupby('year')['suicides_no'].sum().sort_values(ascending = False)


# In[28]:


sus_data.groupby('country')['suicides_no'].sum().sort_values(ascending = False)


# In[63]:


sus_data.groupby(["country" ,"sex"])['suicides_no'].sum().sort_values(ascending = False)


# In[29]:


sns.heatmap(sus_data.corr(), annot = True)


# In[30]:


sus_data.isnull().sum()


# In[32]:


sns.boxplot(data = sus_data)


# In[34]:


sus_data.drop('HDI for year', axis=1,inplace= True)


# In[35]:


sus_data.isnull().sum()


# In[36]:


sus_data


# In[37]:



sus_data['age'] = sus_data['age'].str.replace('years',"")


# In[38]:


sus_data


# In[42]:


sus_data[' gdp_for_year ($) '] = sus_data[' gdp_for_year ($) '].str.replace(',' , "")


# In[41]:


sus_data.columns


# In[43]:


sus_data


# In[45]:


sns.heatmap(sus_data.corr(), annot = True)


# In[46]:


sus_data.info()


# In[52]:


sus_data[' gdp_for_year ($) '] = sus_data[' gdp_for_year ($) '].astype(np.int64)


# In[53]:


sus_data


# In[54]:


sns.heatmap(sus_data.corr(), annot = True)


# In[77]:


profile= pandas_profiling.ProfileReport(sus_data)
profile


# In[78]:


profile.to_file(output_file = "Preprocessing_of_sus_data.html")


# In[ ]:





# In[ ]:




