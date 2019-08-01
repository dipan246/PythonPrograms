#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Define a list

l = [1,2,3]
print(l) # =====> [1, 2, 3]


l2 = list()
l2.append(1)
l2.append(2)
l2.append('a')
print(l2)
[1, 2, 'a'] # =======> [1, 2, 'a']

# indexing with square bracket [] 
l = [1,2,3,4,5]
l[0] # ===> 2
l[4] # ====> 5
l[-2] # ====> 4

# Slicing with square brackets []
l = ['Dipan','Hari','Divyanshu','Neha', 'Monalisa']
l[0:2] # ====> ['Dipan', 'Hari']
l[0:1][0] # 'Dipan'
l[0:1][0][2] # ====> 'p'