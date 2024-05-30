#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
# Import the data into a DataFrame 
books_df = pd.read_csv("BL-Flickr-Images-Book.csv") 
# Display the first few rows of the DataFrame 
print("Original DataFrame:") 
print(books_df.head()) 
# Find and drop the columns which are irrelevant for the book information 
irrelevant_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 
'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks'] 
books_df.drop(columns=irrelevant_columns, inplace=True) 
# Change the Index of the DataFrame 
books_df.set_index('Identifier', inplace=True) 
# Tidy up fields in the data such as date of publication with the help of simple regular expression 
books_df['Date of Publication'] = books_df['Date of Publication'].str.extract(r'^(\d{4})', expand=False) 
# Combine str methods with NumPy to clean columns 
books_df['Date of Publication'] = pd.to_numeric(books_df['Date of Publication'], errors='coerce') 
# Display the cleaned DataFrame 
print("\nCleaned DataFrame:") 
print(books_df.head())


# In[ ]:




