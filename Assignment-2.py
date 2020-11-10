#!/usr/bin/env python
# coding: utf-8

# In[3]:


#question 1
l =[]
for i in range(10):
    x = int(input())
    if x%2==0:
        l.append(x)
print(l)


# In[4]:


#question 2

l = [x for x in range(20)]
print(l)


# In[9]:


# question 3
d = {}
x = int(input())
x = x+1
for i in range(1, x):
    d[i]=i*i
print(d)


# In[8]:


# question 3
d = {}
x = int(input())
x = x+1
for i in range(1, x):
    d1 = {i:i*i}
    d.update(d1)
print(d)


# In[19]:


#question 4
import math
x = 0
y = 0
n = int(input())
for i in range(n):
    


# In[24]:


import math
x, y = 0, 0
while True:
    s = input("step with direction(UP/DOWN/LEFT/RIGHT):")
    if s =="":
        break
    else:
        s = s.split(" ")
        if s[0]=="UP":
            y = y + int(s[1])
        elif s[0] == "DOWN":
            y = y - int(s[1])
        elif s[0] == "RIGHT":
            x = x + int(s[1])
        elif s[0] == "LEFT":
            x = x - int(s[1])
        
l = math.sqrt(x**2 + y**2)
d = round(l)
print(d)
            


# In[ ]:




