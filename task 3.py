#!/usr/bin/env python
# coding: utf-8

# # Task : Exploratory Data Analysis - Retail

# # Name: Shivani Agrawal

# In[1]:


pwd


# In[24]:


#import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


#importing the csv file

url='C:\\Users\Admin\Downloads\SampleSuperstore.csv'
data=pd.read_csv(url)
print("Data imported successfully")

data.head(5)


# In[11]:


data.shape


# In[12]:


data.columns


# In[13]:


data.info()


# In[14]:


data.isnull().sum()


# In[15]:


#checking for duplicate data

data.duplicated().sum()


# In[16]:


#removingg duplicate data
data.drop_duplicates(inplace=True)
data.duplicated().sum()


# In[17]:


#removing the unnecessary data
data.Country.unique()


# In[18]:


data.drop(columns=["Country","Postal Code"],inplace=True)
data.columns


# In[19]:


#lets select columns which have numbers in its value

data_s = data.select_dtypes(include=[np.number])
data_s.head()


# In[20]:


#Detecting Outliers
cols=data_s.columns.to_list()
cols


# In[21]:


# finding correlation
data.corr()


# In[22]:


plt.figure(figsize=(12,12))
sns.heatmap(data.corr(),annot=True,linewidths=0.5,cmap="BuGn")


# # Data Visualization

# In[23]:


print("shipping mode types:",data['Ship Mode'].unique())
print("\n")
print("Segment types:",data['Segment'].unique())
print("\n")
print("Category of products:",data['Category'].unique())
print("\n")
print("Region:",data['Region'].unique())
print("\n")
print("Sub ategory:",data['Sub-Category'].unique())
print("\n")


# 
# # Visualization of sales and profit

# In[42]:


explore_col=['Ship Mode','Segment','Category','Sub-Category']
plt.figure(figsize=(18,7))
for i in explore_col:
    un_sor=data.groupby(i)['Sales'].sum().to_frame().reset_index().sort_values(by='Sales',ascending=False)
    sns.catplot(x=i,y='Sales',data=un_sor,kind='bar',aspect=2.5)
    plt.ylabel('Sales')
    plt.xlabel(i)
    plt.title('Sales in different classes of{}'.format(i))
    plt.show()
    print('\n')


# Intrepration: phones and chairs have highest sales in sub-category

# In[45]:


#counter plot of diffferent features in object type columns of dataset
for i in explore_col:
    plt.figure(figsize=(10,8))
    sns.countplot(data[i],palette='inferno')
    plt.show()


# Interpretation : In the ship mode standard class has the highest count which implies that the customer gives first priority to                  this type.
#                
#                 In segment, the customer have the highest count which means that the customer do the most of shipping
#                
#                 The customer count of west region is the highest in regions graph
#                
#                 From the items category, it is observed that the office supplies category has the highest sales discount.
# 
# 

# In[29]:


plt.figure(figsize=(20,12))
sns.countplot(x='Ship Mode',hue='Segment',data=data)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('Shipping Modes')
plt.ylabel('Count')
plt.legend(loc=5,fontsize=20)


# Interpretation : It is seen that standard class has the maximum count which indicaates that it has most preffered shipping mod and most of the orders are done by customers which are followed by corporates

# In[30]:


#product wise data visualization


# In[32]:


items=data.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values(by='Profit',ascending=False)
items.head()


# In[43]:


plt.figure(figsize=(20,12))
sns.catplot('Sub-Category','Profit',data=items.head(10),kind='bar',aspect=2.5,height=5,palette='inferno')
plt.title('Top 10 profitable products',size=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('cumulative profit',size=15)
plt.ylabel('Product',size=10)
plt.legend(loc=5,fontsize=20)


# Interpretation : Copier, phones and Acccessories are most prefable products.

# In[44]:


items=data.groupby('Sub-Category')['Profit'].sum().reset_index().nsmallest(5,'Profit')
items


# Interpretation:Tables,Bookcases and Supplies are the subitems which are harming the company's profit, proper care should be taken in order to boost their profits. 

# In[ ]:




