import pandas as pd
df = pd.read_csv("C:/Users/PC/Music/New folder/Credit/bengaluru_house_prices.csv")

#  khu vuc
#  trang thai bds , co chuyen den dc luon klo
#  bn phong
# bathly : ban cong
#  1
null = df.isnull().sum()

# 2
typeArea = df["area_type"].unique()
# 3 unique bn gia tri
df["area_type"].value_counts()

null = df.isnull().sum()

location = df["location"].unique()
df["location"].value_counts()

size = df["size"].unique()
df["size"].value_counts()

society = df["society"].unique()
df["society"].value_counts()

bath = df["bath"].unique()
df["bath"].value_counts()

balcony = df["balcony"].unique()
df["balcony"].value_counts()

# dropna

df_new = df.drop(['society'],axis =1)
# khong co y nghia

#  dua tren nhung con so
df_new.corr()


df_new.isnull().sum()


dfNew = df_new.dropna()
dfNew.isnull().sum()

dfNew["size"].value_counts()

a = dfNew["size"].iloc[0]
int(a.split(" ")[0])



# c=[]
# #  moi lan chay vong lap tao list c rong
# # de ngoai no chi tao 1 list 1 lan
# for i in range(len(dfNew)):
#     a = dfNew["size"].iloc[i]
#     b = int( a.split(" ")[0])
#     c.append(b)
# print(c)
# dfNew['ádsada'] = c

dfNew['size_split'] = dfNew['size'].apply(lambda x: int(x.split(" ")[0]))
float("1234")
# "2010-2018" -==> avg
#  "3mter" == 0
# ##string "135.6" ==>135
##string "1234" ==>float con cua th 1

def convert_to_num(x):
    list0 = x
    splitList = list0.split("-")
    try:
        if len(splitList) == 2:
            conver = round((float(splitList[0]) + float(splitList[1]))/2, 0)
        elif len(splitList) == 1:
            conver = round(float(splitList[0]),0)
        return conver
    except ValueError:
        return 0

# convert_to_num("135.6")

dfNew['total_sqft_convert_to_num'] = dfNew['total_sqft'].apply(convert_to_num)

dfNew["m2Price"] = round(dfNew['price'] /dfNew["total_sqft_convert_to_num"],2)

location = dfNew["location"].unique
#  tan suat xuat hien location <= 8 =>delete

# Ví dụ: 'Electronic City Phase II': 8 lần => 'Others'
#         'Chikka Tirupathi': 60 lần => 'Chikka Tirupathi'
location = dfNew["location"].value_counts()
location_lessthan10 = location[location<10]

dfNew['new_location'] = dfNew['location'].apply(lambda x: 'other' if x in location_lessthan10 else x)
