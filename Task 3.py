#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

''' Load the data into a DataFrame
Sample data as householdtask3 '''
df = pd.read_csv(r"C:\Users\Admin\Downloads\householdtask3.csv")
print(df.head())


# In[20]:


# Bar Chart
plt.figure(figsize=(12, 6))
plt.bar(df['year'], df['tot_hhs'], color='pink', label='Total Households')
plt.bar(df['year'], df['own'], color='purple', label='Owned Households')

plt.xlabel('Year')
plt.ylabel('Number of Households')
plt.title('Total Households and Owned Households Over Years')
plt.legend()
plt.grid(True)
plt.show()


# In[22]:


# Line Chart
plt.figure(figsize=(12, 6))
plt.plot(df['year'], df['income'], marker='o', linestyle='-', color='red', label='Income')
plt.plot(df['year'], df['expenditure'], marker='o', linestyle='--', color='indigo', label='Expenditure')

plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Income and Expenditure Over Years')
plt.legend()
plt.show()


# In[ ]:




