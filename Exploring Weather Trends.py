#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Calling Libraries: 

import numpy as np
import pandas as pd                  # for loading data into the notebook
from matplotlib import pyplot as plt #for making line chart


# In[16]:


## Importing the extracted Data Set:

data = pd.read_excel (r'C:\Users\Sahi\Desktop\Nanodegree\Results.xlsx')
print (data)


# In[17]:


## Moving Averages: 

def moving_avg(mA_range, data_input):   # with local variables
    output = data_input.rolling(window = mA_range, center = False, on = "ctemp").mean().dropna()
    return output

## Function Calling with the range of Moving Average:
mA_value = 150

chart_moving_avg = moving_avg(mA_value, data)     # with global variables

##Drawing the graph: Global Temperature
plt.plot(chart_moving_avg['year'], chart_moving_avg['gtemp'], label='Global')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Global Average Temperature")
plt.show()


# In[18]:


## Drawing the graph:Austin and Global Temperature:

plt.plot(chart_moving_avg['year'], chart_moving_avg['ctemp'], label='Austin')
plt.plot(chart_moving_avg['year'], chart_moving_avg['gtemp'], label='Global')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Temperature (°C)")
plt.title("Austin Vs Global Average Temperature")
plt.show()


# In[19]:


data.tail(10)


# In[20]:


data.head(10)


# In[ ]:




