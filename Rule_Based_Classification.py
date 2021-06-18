
import pandas as pd
import numpy as np
pd.pandas.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

import os
os.chdir(r"C:\Users\user\PycharmProjects\dsm\Data")

df = pd.read_csv("persona.csv")

#SORU1

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
#SORU2
df["SOURCE"].unique()
df["SOURCE"].value_counts()
#SORU3
df["PRICE"].unique()
#SORU4
df["PRICE"].value_counts()
#SORU5
df["COUNTRY"].value_counts()
#SORU6
df.groupby("COUNTRY").agg({"PRICE" : "sum"})
#SORU7
df["SOURCE"].value_counts()
#SORU8
df.groupby("COUNTRY").agg({"PRICE" : "mean"})
#SORU9
df.groupby("SOURCE").agg({"PRICE" : "mean"})
#SORU10
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE" : "mean"})

#### GÖREV2
df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "sum"})

#### GÖREV3
agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE" : "sum"}).sort_values(by="PRICE",ascending=False)

#### GÖREV4
agg_df.head(10)
agg_df = agg_df.reset_index()

###GÖREV5

agg_df["AGE"] = pd.cut(agg_df["AGE"], bins = [0, 18, 23, 30, 40 ,70],labels=["0_18","19_23","24_30","31_40","41_70"])
agg_df["AGE"].value_counts()
["0_18","19_24","25_30","31_40","41_70"]
### GÖREV6
agg_df.info()
agg_df.head()

agg_df["customer_level_based"] = ["_".join(row[0:4]).upper() for row in agg_df.values]
persona_df = agg_df[["customer_level_based","PRICE"]]
persona_df.head()
#persona_df["customer_level_based"].value_counts()

agg_df = persona_df.groupby("customer_level_based").agg({"PRICE":"mean"})
agg_df.head()
## groupby çekilmiş son hali segmentlere ayırılacak

###### GÖREV-7

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4, labels=["D","C","B","A"] )

agg_df.groupby("SEGMENT").agg({"PRICE":["sum","mean","max","min"]})

agg_df[agg_df["SEGMENT"]=="C"].describe().T


pd.DataFrame({"SEGMENT":  agg_df["SEGMENT"].value_counts() ,
              "RATİO":100 * agg_df["SEGMENT"].value_counts() / len(agg_df) })

import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x = "SEGMENT", y ="PRICE", data = agg_df)
plt.show()
plt.boxplot(agg_df["PRICE"])
plt.show()
plt.hist(agg_df["PRICE"])
plt.show()


### TAHMİNLEME
# CUSTOMER LEVEL BASED SÜTUNU İNDEX OLARAK DURUYOR SIFIRLA
agg_df = agg_df.reset_index()

agg_df[agg_df["customer_level_based"] == new_user]
agg_df[agg_df["customer_level_based"] == new_user].iloc[0,[1,2]]

def search_persona(country,system,sex,age):
    if (0 < age) and (18 >= age):
        new_age = "0_18"
    if (18 < age) and (23 >= age):
        new_age = "19_23"
    if (24 <= age) and (30 >= age):
        new_age = "24_30"
    if (30 < age) and (40 >= age):
        new_age = "31_40"
    if (40 < age) and (70 >= age):
        new_age = "41_70"
    # new_user = country.upper() + "_" + system.upper() + "_" + sex.upper() + "_" + new_age.upper()
    new_user =  "_".join([country,system,sex,new_age]).upper()
    print(agg_df[agg_df["customer_level_based"] == new_user].iloc[0,[1,2]])

search_persona("usa","ios","male",24)

# QUEST-1
search_persona("tur","android","female",23)
# QUEST-2
search_persona("fra","ios","female",18)


# "_".join([country,system,sex,age])
# country = "USA"
# system = "IOS"
# sex = "FEMALE"
# age= 40


