#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Tanmay\Downloads\archive (9)\Student Stress Factors.csv')
correlation_matrix = data.corr()
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Student Stress Factors")
plt.show()


# In[ ]:




