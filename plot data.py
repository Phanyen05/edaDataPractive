# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:23:46 2022

@author: PC
"""

import pandas as pd
# read file
pl16 = pd.read_csv("C:/Users/PC/Desktop/New folder/pl_15-16.csv")
pl17 = pd.read_csv("C:/Users/PC/Desktop/New folder/pl_16-17.csv")
pl18 = pd.read_csv("C:/Users/PC/Desktop/New folder/pl_17-18.csv")
pl19 = pd.read_csv("C:/Users/PC/Desktop/New folder/pl_18-19.csv")
pl20 = pd.read_csv("C:/Users/PC/Desktop/New folder/pl_19-20.csv")

# open file
#posotion vij tri choi
pl16
# g
pl16["year"] = '2015-2016'
# loc cột thứ 2


pl17["year"] = '2016-2017'
pl18['year'] = '2017-2018'
pl19['year'] = '2018-2019'
pl20['year'] = '2019-2020'

# d.concat([df1, df3], sort=False)
table_session = pd.concat([pl16,pl17,pl18,pl19,pl20])
table_session.isnull().sum()
 # fillana
table_new = table_session.fillna(0)
# dãd ra sân trong mùa giải
d_zero = table_new[table_new["Appearances"] != 0]


# pl20
pl20_new = pl20.fillna(0)
pl20_zero = pl20_new[pl20_new["Appearances"] != 0]


# top 5 ra saan nhieu nhat
# sorting data frame by name
pl20_zero.sort_values("Appearances", axis = 0, ascending = False,
                 inplace = True)
top5_appe = pl20_zero.head(5) #tail

# extracting greatest 5
large5 = pl20_zero.nlargest(5, "Goals")
large5.plot(kind='bar',x='Name',y='Goals',title= 'Top 5 Goal scorers - 2019-2020',color='blue')


# kiến tạo
pl20_new['scores'] = pl20_new["Goals"] + pl20_new["Assists"]
large50 = pl20_new.nlargest(5, "scores")
large50.plot(kind='bar',x='Name',y='scores',title= 'Top 5 Goal scorers - 2019-2020',color='blue')


#
