#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as reg
url = 'https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_Electronics_0_Gaming%20Laptops'


# In[6]:


uClient = reg(url)
html_page = uClient.read()
uClient.close()
page_soup = soup(html_page,"html.parser")
containers = page_soup.findAll("div" , {"class","_2kSfQ4"})
number_of_laptops = len(containers)
i = 0 
DataSet = []
while(i<number_of_laptops):
    data ={}
    container = containers[i]
    data['Name'] = container.div.img['alt']
    data['Current_price'] = container.find(class_="_1vC4OE").get_text(strip=True)
    try:
        data['Original_price'] = container.find(class_="_3auQ3N").get_text(strip=True)
    except AttributeError:
         data['Original_price']=None
    try:
         data['Discount'] = container.find(class_="VGWI6T").get_text(strip=True)
    except AttributeError:
          data['Discount']=None
    try:
        data['Rating'] =container.find(class_="hGSR34").get_text(strip=True)
    except AttributeError:
        data['Rating'] = None
        
    DataSet.append(data)
    i = i + 1


# In[7]:


import pandas as pd
dataframe = pd.DataFrame(DataSet)
col_names = ["Name","Original_price","Current_price","Discount","Rating"]
dataframe = dataframe.reindex(columns=col_names)
dataframe


# In[8]:


dataframe.to_csv("Output.csv")


# In[ ]:




