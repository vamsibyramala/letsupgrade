#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
print(pd.__version__)


# In[51]:


a = np.array(['vamsi', 'sai', 'Althaf', 'Rakesh'])
s = pd.Series(a)
print(s)


# In[56]:


a = np.array(['vamsi', 'sai', 'Althaf', 'Rakesh'])
s = pd.Series(a)
print(s)
df1 = s.to_frame()
df1.reset_index(level = 0, inplace = True)
print(df1)


# In[78]:


import seaborn as sns
print(sns.get_dataset_names())
df2 = sns.load_dataset('mpg')
print(df2.head())


# In[80]:


#Question-5:
print(df2['origin'].unique())


# In[84]:


usa = (df2['origin'] == 'usa')
df_usa = df2[usa]
print(df_usa)


# In[ ]:




