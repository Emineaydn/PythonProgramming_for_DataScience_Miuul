import numpy as np


def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("miuul")

students = ["Jhon", "Mark", "Venassa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

students = ["Jhon", "Mark", "Venassa", "Mariam"]
A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)
print(A, B)

students = ["Jhon", "Mark", "Venassa", "Mariam"]


def divide_student(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


divide_student(students)


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("hi my name is john and i am learning python")

##################
# Zip
##################

students = ["Jhon", "Mark", "Venassa", "Mariam"]

departments = ["math", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

C = list(zip(students, departments, ages))
print(C)

#################################
# ALIŞTIRMALAR
#################################

##2
text = "The goal is to turn data into information, and information into insight."
A = text.upper().replace(",", " ").replace(".", " ").split()
print(A)

##3
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
B = len(lst)
print(B)
lst[0]
lst[10]
C = list(lst[0:4])
print(C)

lst.pop(8)
print(lst)

lst.append("W")
print(lst)

lst.insert(8, "N")
print(lst)

##4

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
A = dict.keys()
print(A)

B = dict.values()
print(B)

dict.update({'Daisy': ["England", 13]})
print(dict)

dict.update({'Ahmet': ["Turkey", 24]})
print(dict)

dict.pop("Antonio")
print(dict)

##5

odd_list = []
even_list = []
l = [2, 13, 18, 93, 22]


def fuc(list):
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


print(fuc(l))

##6

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, student in enumerate(ogrenciler):
    if i < 3:
        i += 1
        print("Mühendislik Fakültesi ", i, ". öğrenci", student)
    else:
        i -= 2
        print("Tıp Fakültesi", i, ". öğrenci:", student)

##7
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print("Kredisi", kredi, ders_kodu, "kodlu dersin", "kontenjanı", kontenjan, "kişidir.")

##8

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kume(kume1, kume2)

##########################################################################
# çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.

# Some code within the function
numbers = range(10)
new_dict = {n: n ** 2 for n in numbers if n % 2 == 0}
print(new_dict)

numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
print(new_dict)

#######################################################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A
print(df.columns)

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
print(df.columns)

##########################

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

A = ["FLAG_" + col if "INS" in col else "NO_FLAG" + col for col in df.columns]
print(A)

############################################################
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

B = num_cols = [col for col in df.columns if df[col].dtype != "0"]

soz = {}

agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

print(soz)
# Define a dictionary of aggregation functions for numerical columns


wages = [1000, 2000, 3000, 4000, 5000]
new_wages = lambda x: x * 0.20 + x
A = list(map(new_wages, wages))
print(A)

##################################################################
# NUMPY
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
A = a * b
print(A)
##################

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
A = a.ndim
print(A)
B = a.shape
print(B)
C = a.size
print(C)
D = a.dtype
print(D)

##############################
import numpy as np

v = np.array([1, 2, 3, 4, 5])
A = v[v < 3]
print(A)
##############################

import numpy as np

v = np.array([1, 2, 3, 4, 5])
A = np.subtract(v, 1)
print(A)
B = np.add(v, 1)
print(B)
C = np.mean(v)
print(C)
D = np.sum(v)
print(D)
E = np.min(v)
print(E)
F = np.max(v)
print(F)
G = np.var(v)
print(G)

############################################
# 5*x0 + x1 = 12
# x0 + 3*x1 =10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

S = np.linalg.solve(a, b)
print(S)

a = np.random.randint(0, 10, size=5)
print(a)

###########################################################
##PANDAS
###########################################################

import pandas as pd

A = pd.Series([10, 77, 12, 4, 5])
print(A)
print(type(A))
print(A.index)
print(A.dtype)
print(A.size)
print(A.ndim)
print(A.values)
print(type(A.values))
print(A.head(3))
print(A.tail(3))

#############################
##READING DATA
############################

df = pd.read_csv("datasets/Advertising.csv")
print(df.head())

##QUICK LOOK at DATA

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns)
print(df.index)
print(df.describe().T)
print(df.isnull().values.any())
print(df.isnull().sum())
print(df["sex"].head())
print(df["sex"].value_counts())

#################################
# SELECTION in PANDAS

df = sns.load_dataset("titanic")

print(df.head())
print(df.index)
print(df[0:13])
print(df.drop(0, axis=0).head())
delete_index = [1, 3, 5, 7]
print(df.drop(delete_index, axis=0).head(10))

# kalıcı olarak kaydetme
# df=df.drop(delete_index, axis=0)
# df.drop(delete_index, axis=0, inplace=True) inplace kullanarak da kalıcı kaydedebiliriz

#####################
# DEĞIŞKENİ INDEX E CEVIRME

df["age"].head()
df.age.head()

df.index = df["age"]
print(df.drop("age", axis=1, inplace=True))
df.head()

###############################
# INDEX I DEGISKENE CEVIRME

df.index
df["age"] = df.index
print(df.head())
df.drop("age", axis=1, inplace=True)

df = df.reset_index()
print(df.head())

#############################################
# DEGISKENLER UZERINDE ISLEMLER
############################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
print(df.head())

print("age" in df)
print(df["age"].head())
print(df.age.head())

print(df[["age"]].head())
print(type(df[["age"]].head()))

print(df[["age", "alive"]])

col_names = ["age", "adult_male", "alive"]
print(df[col_names])
df["age2"] = df["age"] ** 2
print(df.head())

df["age3"] = df["age"] / df["age2"]
print(df.head())
print(df.drop("age3", axis=1).head())
print(df.drop(col_names, axis=1).head())

print(df.loc[:, ~df.columns.str.contains("age")].head())  # ~ dışında demek ##loc secme işlemi yapar

####################################################################################################
# iloc and loc

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc:integer based selection

print(df.iloc[0:3])

# loc: label based selection

print(df.loc[0:3])

print(df.iloc[0:3, 0:3])
print(df.loc[0:3, "age"])

col_names = ["age", "embarked", "alive"]
print(df.loc[0:3, col_names])

####################################################################
##CONDITIONAL SELECTION
####################################################################

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

print(df[df["age"] > 50].head())
print(df[df["age"] > 50]["age"].count())

print(df.loc[df["age"] > 50, ["age", "class"]].head())
print(df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head())

###################################################################################
# AGGREGATION & GROUPING
############################################################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - pivot table

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

print(df["age"].mean())

print(df.groupby("sex")["age"].mean())

print(df.groupby("sex").agg({"age": "mean"}))

print(df.groupby("sex").agg({"age": ["mean", "sum"]}))

print(df.groupby("sex").agg({"age": ["mean", "sum"],
                             "survived": "mean"}))

print(df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                              "survived": "mean"}))

print(df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                       "survived": "mean"}))

print(df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"}))

#############################
## PIVOT TABLE

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

print(df.pivot_table("survived", "sex", "embarked"))  # pivot da columns ve rows kesişimleri ortalama verir

print(df.pivot_table("survived", "sex", "embarked", aggfunc="std"))
print(df.pivot_table("survived", "sex", ["embarked", "class"]))

a = df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
print(df.head())
print(df.pivot_table("survived", "sex", ["new_age", "class"]))

pd.set_option('display.width', 500)
print(df.pivot_table("survived", "sex", ["new_age", "class"]))

######################################################
# APPLY AND LAMBDA
######################################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

print((df["age"] / 10).head())
print((df["age2"] / 10).head())
print((df["age3"] / 10).head())

for col in df.columns:
    if "age" in col:
        print((df[col] / 10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

print(df.head())

print(df[["age", "age2", "age3"]].apply(lambda x: x / 10).head())

print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head())

print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head())


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


print(df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head())

#########################################################################################
# JOINING PROCEDURES
#########################################################################################

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

print(pd.concat([df1, df2], ignore_index=True))

###################################
##JOINING PROCEDURES with MERGE

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

print(pd.merge(df1, df2))

print(pd.merge(df1, df2, on="employees"))

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

print(pd.merge(df3, df4))

###############################################################
# ALISTIRMALAR
###############################################################

# 1
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("car_crashes")
df.columns
df.info()

print(["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns])

# 2
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("car_crashes")
df.columns
df.info()
print([col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns])

# 3
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())

##PANDAS ALISTIRMALAR

import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# 1

# Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız
df = sns.load_dataset("titanic")
df.head()
print(df.shape)

# 2

# Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
print(df["sex"].value_counts())

# 3

# Her bir sutuna ait unique değerlerin sayısını bulunuz.
print(df.nunique())

# 4

# pclass değişkeninin unique değerlerinin sayısını bulunuz.
print(df["pclass"].unique())

# 5

# pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz
print(df[["pclass", "parch"]].nunique())

# 6

# embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

print(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype
print(df.info())

# 7

# embarked değeri C olanların tüm bilgelerini gösteriniz.
print(df[df["embarked"] == "C"].head())

# 8

# embarked değeri S olmayanların tüm bilgelerini gösteriniz
print(df[df["embarked"] != "S"].head())

# 9

# Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
print(df[(df["age"] < 30) & (df["sex"] == "female")].head())

# 10

# Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
print(df[(df["fare"] > 500) | (df["age"] > 70)].head())

# 11

# Her bir değişkendeki boş değerlerin toplamını bulunuz.

print(df.isnull().sum())

# 12

# who değişkenini dataframe’den çıkarınız.
print(df.drop("who", axis=1, inplace=True))

# 13

# deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
print(df["deck"].isnull().sum())

# 14

# age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz
df["age"].fillna(df["age"].median(), inplace=True)
print(df["age"].isnull().sum())

# 15

# survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

print(df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]}))


# 16

# 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))
df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
print(df["age_flag"])

# 17

# Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
df.head()
print(df.shape)

# 18

# Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
print(df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]}))

# 19

# Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
print(df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]}))

# 20

# Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.

# df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum","min","max","mean"],
#  "tip":  ["sum","min","max","mean"],
#  "Lunch" : lambda x:  x.nunqiue()})

# 21

# size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
print(df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean())

# 22

# total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()
print(df["total_bill_tip_sum"])

# 23

# total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
print(new_df.shape)

#######################################################################################################
## VERI GORSELLESTIRME: MATPLOTLIB  SEABORN
#######################################################################################################

############################################################
# MATPLOTLIB
############################################################

# Kategorik değişken: sütun grafik, countplot bar
# sayısal değişken: hit, boxplot

#####################################################
# Kategorik Değişken Görselleştirme
#####################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df["sex"].value_counts().plot(kind="bar")
plt.show()

#####################################################
# Sayısal Değişken Görselleştirme
#####################################################

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

#####################################################
# MATPLOTLIB OZELLIKLERI
#####################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

#######################
# plot
#######################

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])
plt.plot(x, y)
plt.show()

#######################
# marker
#######################

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')
plt.show()

#######################
# line
#######################

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
plt.show()

plt.plot(y, linestyle="dotted")
plt.show()

plt.plot(y, linestyle="dashdot", color="r")
plt.show()

#######################
# Multiple lines
#######################

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])

plt.plot(x)
plt.plot(y)
plt.show()

#######################
# Labels
#######################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)

# Başlık
plt.title("Bu ana başlık")

# X eksenini isimlendirmek
plt.xlabel("X ekseninin isimlendirilmesi")

# Y ekseninin isimlendirilmesi
plt.ylabel("Y ekseninin isimlendirilmesi")

plt.grid()
plt.show()

#######################
# Subplots
#######################

# plot1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1)
plt.title("1")
plt.plot(x, y)

# plot2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2)
plt.title("2")
plt.plot(x, y)

# plot3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
plt.title("3")
plt.plot(x, y)

plt.show()

############################################################
# SEABORN
############################################################

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
df.head()
df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)
plt.show()

df["sex"].value_counts().plot(kind='bar')
plt.show()

####################################
# Sayısal Değişken Görselleştirme
####################################

sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()

###############################################################################
## ADVANCED FUNCTIONAL EDA
###############################################################################

# 1. Genel Resim
# 2. Analysis of Categorical Variables
# 3. Analysis of Numerical Variables
# 4. Analysis of Target Variables
# 5. Analysis of Correlation


######################################
# 1. Genel Resim
######################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA#####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("flights")
check_df(df)

######################################
# 2. Analysis of Categorical Variables
######################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

print(df["embarked"].value_counts())
print(df["sex"].unique())
print(df["class"].nunique())

cat_cols = [col for col in df.columns if str(df[col].dtypes in ["category", "object", "bool"])]
print(df[cat_cols])

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
print(num_but_cat)

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes in ["category", "object"])]
print(cat_but_car)

cat_cols = num_but_cat + cat_cols
print(cat_cols)

cat_cols = [col for col in cat_cols if col not in cat_but_car]
print(df[cat_cols].nunique())

df["survived"].value_counts()
100 + df["survived"].value_counts() / len(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("################################################")


cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts()
                                 / len(dataframe)}))
    print("################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("sdhfkjdfdf")
    else:
        cat_summary(df, col, plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
    else:
        cat_summary(df, col, plot=True)


def cat_summary(dataframe, col_name, plot=False):
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts()
                                     / len(dataframe)}))
        print("################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts()
                                     / len(dataframe)}))
        print("################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


cat_summary(df, col, plot=True)

######################################
# 3. Analysis of Numerical Variables
######################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df[["age", "fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
num_cols = [col for col in num_cols if col not in cat_cols]
print(num_cols)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


num_summary(df, "age", plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

#########################################################################
##Capturing Variables and Generalizing Operations

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


# docstring
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.

    Parameters
    ----------
    dataframe: dataframe
        değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
        numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
        kategorik fakat kategorik olan değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
        Kategorik değişken listesi
    num_cols: list
        Numerik değişken listesi
    cat_but_car: list
        Kategorik görünümlü kordinal değişken listesi

    Notes
    ------
    cat_?cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """

    cat_cols = [col for col in df.columns if str(df[col].dtypes in ["category", "object", "bool"])]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes in ["category", "object"])]

    cat_cols = num_but_cat + cat_cols

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)

######################################
# 4. Analysis of Target Variables
######################################

df["survived"].value_counts()
print(cat_summary(df, "survived"))

##########################
# Hedef Değişkenin Kategorik Değişken ile Analizi
##########################

df.groupby("sex")["survived"].mean()


def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")


target_summary_with_cat(df, "survived", "pclass")

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)

##########################
# Hedef Değişkenin Sayısal Değişkenler ile Analizi
##########################

df.groupby("survived")["age"].mean()
df.groupby("survived").agg({"age": "mean"})


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")


target_summary_with_num(df, "survived", "age")

for col in num_cols:
    target_summary_with_num(df, "survived", col)

######################################
# 5. Analysis of Correlation
######################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/dataset/data.csv")

print(df.head())

num_cols = [col for col in df.columns if df[col].dtype in ["int", "float"]]
corr = df[num_cols].corr()
print(corr)
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

##########################
# Yüksek Korelasyonlu Değişkenlerin Silinmesi
##########################


cor_matrix = df.corr().abs()

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool))
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
print(drop_list)
cor_matrix[drop_list]
df.drop(drop_list, axis=1)

def high_correlated_cols(dataframe, plot= False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list

high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)