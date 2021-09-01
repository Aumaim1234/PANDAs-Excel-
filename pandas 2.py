#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd


# In[9]:


##Quiz 1##

#Read csv file
df = pd.read_csv('C:/Users/Acer/Desktop/HW/coding/Final/1-9/Salaries.csv')


# In[10]:


# first 10
df.head(10)


# In[11]:


# first 20
df.head(20)


# In[12]:


# first 50
df.head(50)


# In[15]:


#the last few records ex. 10 from last
df.tail(10)


# In[16]:


####### 13 exercises in PPT (page.50 - 61)#########


#Data Frames groupby method
#Group data using rank
#1
df_rank = df.groupby(['rank'])


# In[17]:


#2
df_rank.mean()


# In[18]:


#3
df.groupby('rank')[['salary']].mean()


# In[19]:


#4 (เรียงจากมากไปหาน้อย)
df.groupby(['rank'], sort=False)[['salary']].mean()


# In[23]:


#5 filtering
df_sub = df[ df['salary'] > 120000 ]
df_sub


# In[25]:


#6  
df_f = df[ df['sex'] == 'Female' ]
df_f


# In[26]:


#7 Slicing select a range of rows  
df['salary']


# In[27]:


#8
df[['rank','salary']]


# In[28]:


#9
df[10:20]


# In[29]:


#10
df_sub.loc[10:20,['rank','sex','salary']]


# In[30]:


#11 iloc //select a range of rows and/or columns, 
df_sub.iloc[10:20,[0, 3, 4, 5]]


# In[31]:


#12 sort the data by a value in the column
df_sorted = df.sort_values( by ='service')
df_sorted.head()


# In[32]:


#13
df_sorted = df.sort_values( by =['service', 'salary'], ascending = [True, False])
df_sorted.head(10)

