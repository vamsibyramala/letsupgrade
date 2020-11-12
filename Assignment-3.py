#!/usr/bin/env python
# coding: utf-8

# # question-1:

# In[4]:


import numpy as np
a = np.arange(2,51,3)
print(a)


# # question-2:

# In[ ]:


l1 = []
l2 = []
for i in range(5):
    e1 = int(input("1st list elements:"))
    l1.append(e1)
    a1 = np.array(l1)
    s1 = np.sort(a1)
    
for i in range(5):
    e2 = int(input("2nd list elements:"))
    l2.append(e2)
    a2 = np.array(l2)
    s2 = np.sort(a2)
    
print(a1)
print(a2)
c = np.concatenate((a1, a2))
cs = np.sort(c)
print(c)
print(s1)
print(s2)
print(cs)


# # Question-3:

# In[11]:


n = int(input("enter number of elements in array:"))
a = np.arange(1,n)
print(a.ndim)
print(a.shape)
print(np.size(a))


# # Question-4:

# In[32]:


d1 = np.arange(1,7)
d2= np.reshape(d1, (2, 3))
print(d1)
print(d2)
a = d1[:,np.newaxis]
a2 = np.expand_dims(a, axis=0)
print(a)
print(a2)
print(a2.shape)


# # Question-5:

# In[38]:


a = np.arange(1,10)
b = np.arange(21,30)
a1 = np.reshape(a, (3,3))
a2 = np.reshape(b, (3,3))
print(a1)
print(a2)
v = np.vstack((a1, a2))
h = np.hstack((a1, a2))
print(v)
print(h)


# # Question-6:

# In[42]:



l = []
n = int(input("enter number of elements in array:"))
for i in range(n):
    x = int(input("element"))
    l.append(x)
print(l)
u = np.unique(l)
print(u)

