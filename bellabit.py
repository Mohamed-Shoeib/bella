#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('dailyActivity_merged.csv')
df


# In[3]:


df.Id.nunique()


# In[4]:


cols = ['Id','ActivityDate','TotalSteps','VeryActiveMinutes','FairlyActiveMinutes','LightlyActiveMinutes','SedentaryMinutes','Calories']
df_new = df[cols]


# In[5]:


df_new


# In[6]:


df_new.rename(columns={'ActivityDate':'Date'}, inplace=True)


# In[7]:


df_new


# In[8]:


df_new['TotalMinutes'] = df.VeryActiveMinutes + df.FairlyActiveMinutes + df.LightlyActiveMinutes + df.SedentaryMinutes


# In[9]:


df_new


# In[10]:


df_new['TotalHours'] = round(df_new.TotalMinutes/60)
df_new


# In[11]:


df_new.info()


# In[34]:


# df.date = pd.to_datetime(df_new.Date)
df_new['Date'] = pd.to_datetime(df_new['Date'])


# In[35]:


df_new


# In[36]:


df_new.info()


# In[37]:


df_new


# In[40]:


import datetime as dt
df_new['DayOfWeek'] = df_new.Date.dt.day_name()


# In[41]:


df_new


# In[42]:


df_new.isnull().sum()


# In[43]:


df.duplicated().sum()


# In[46]:


df_new.describe()


# In[51]:


plt.figure(figsize =((6,4)))
plt.hist(df_new.DayOfWeek , bins = 7 , color = 'lightskyblue' ,width = 0.6)
plt.grid(True)

plt.xlabel('Day of Week')
plt.ylabel('Frequency')
plt.title('freq of day of week')

plt.show()


# In[52]:


df_new.corr()


# In[53]:


sns.heatmap(df_new.corr())


# In[61]:


plt.figure(figsize = ((6,4)))
plt.scatter(df_new.TotalSteps , df_new.Calories , c = df_new.Calories)

median_steps = 7405
median_calories = 2134

plt.axhline(median_calories , color = 'blue' , label = 'median of calories')
plt.axvline(median_steps , color = 'red' , label = 'median of steps')

plt.xlabel('steps')
plt.ylabel('calories')
plt.title('calories by total steps')
plt.legend()

plt.show()


# In[62]:


plt.figure(figsize = ((6,4)))
plt.scatter(df_new.TotalHours , df_new.Calories , c = df_new.Calories)

median_hours = 24
median_calories = 2134

plt.axhline(median_calories , color = 'blue' , label = 'median of calories')
plt.axvline(median_hours , color = 'red' , label = 'median of hours')

plt.xlabel('hours')
plt.ylabel('calories')
plt.title('calories by total steps')
plt.legend()

plt.show()


# In[69]:


VeryActiveMinutes = df_new.VeryActiveMinutes.sum()
FairlyActiveMinutes = df_new.FairlyActiveMinutes.sum()
LightlyActiveMinutes = df_new.LightlyActiveMinutes.sum()
SedentaryMinutes = df_new.SedentaryMinutes.sum()

minutes = [VeryActiveMinutes , FairlyActiveMinutes , LightlyActiveMinutes , SedentaryMinutes]

labels = ['VeryActiveMinutes' , 'FairlyActiveMinutes' , 'LightlyActiveMinutes' , 'SedentaryMinutes']

plt.pie(minutes , labels = labels , autopct ='%1.1f%%', explode = [0,0,0,0.1])
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




