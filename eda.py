# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 21:13:16 2022

@author: PC
"""
import pandas as pd
file = pd.read_csv("C:/Users/PC/Music/New folder/cartier_catalog.csv")

file.head()
# Function to calculate missing values by column# Funct

# totall null
file.isnull().sum()

#in column categorie have value in
file.categorie.value_counts()

#count in DF
categorie = file[file['categorie'] == 'rings']



#print 2 column with name == categori and price
categorie1 =categorie[["categorie","price"]]




# a = categorie1.mean(axis=1)
# avg = categorie1.price.sum() / 259
# avg.round(2)
file.groupby('categorie').price.mean()
categorie.groupby('categorie').price.mean().round(2)
#tag,



tags =file["tags"].str.split(",")
# for i in tags :
#     tag_0 = i[0]
#     print(tag_0)
file["yenXinhGaiNhatTrenDoi"]= file.tags.apply(lambda x: x.split(',')[0])
