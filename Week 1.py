#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import json
import csv


# In[9]:


with open("TAMID-Week-1.json") as json_file:
    data = json.load(json_file)


# In[10]:


print(data)


# In[15]:


score_data = data['World Series']


# In[18]:


data_file = open('TAMID-Week-1.json', 'w')
csv_writer = csv.writer(data_file)
csv_writer.writerow(score_data[0].keys())


# In[19]:


for score in score_data:
    csv_writer.writerow(score.values())
data_file.close()


# In[21]:


df = pd.read_csv('TAMID-Week-1.json')
df


# In[22]:


df.describe()


# In[23]:


df['Winner']

