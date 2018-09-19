import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s
# yaha libraries import kari hai mne


df = pd.read_csv('googleplaystore.csv')
# print(df.head(5))
# print(df.columns)

# Now the Data cleaning part is as follows:-
df['Size'] = df['Size'].map(lambda x: str(x)[:-1])
# to remove the last character from the Size columns
# for example 19M will now become 19 because this is the info we need
df['Installs'] = df['Installs'].map(lambda x: str(x)[:-1])
df['Installs'] = df['Installs'].map(lambda x: x.replace(',',''))
df['Size'] = df['Size'].map(lambda x: x.replace(',',''))
df['Reviews'] = df['Reviews'].map(lambda x: x.replace('M',''))
df['Installs'] = df['Installs'].map(lambda x: x.replace('Fre',''))
df['Price'] = df['Price'].map(lambda x: x.replace('$',''))
# installs contains ',' we need to remove this to make it a numeric column
df['Category'] = df['Category'].map(lambda x: str(x)[:3])
# we only wnat the first three characters of the category it is making visualisation look bad
# dropping all columns not needed this is done after performing feature engineering analysis of all the columns
df.drop(['App','Content Rating','Last Updated','Current Ver','Android Ver','Genres'],axis=1,inplace= True)
# now lets check for the null values in these columns
# print(df.isnull().values.sum()) gives the total number of null values

# print(df.isnull().any())
# so Rating and Type contain null values, lets fix them
df.dropna(inplace=True)
print(df.isnull().any())
#
df['Size'] = df['Size'].replace('Varies with devic',np.nan).dropna()
df.dropna(inplace=True)
df['Installs'].replace('', np.nan, inplace=True)
df.dropna(inplace=True)
# size contains 'Varies with devic' we must get rid of it to actually make it numeric
# pd.to_numeric(df['Size'],errors='coerce')
# print(df['Size'])

print(df.dtypes)
print(df.columns)
# now lets create dummy variable for the cetagorical variable Type
df_type = pd.get_dummies(df['Type'])
d = pd.concat([df,df_type],axis=1)
d.drop(['Type'],axis=1,inplace=True)
print(d.head(5))
# print(d['Size'])
# After Data Analysis is done
# now creating some basic plots
# s.countplot(df['Type'])
# plt.show()
# s.countplot(df['Category'])
# plt.show()
# s.distplot(pd.to_numeric(df['Size']),bins=50)
# plt.show()
# s.distplot(pd.to_numeric(df['Rating']),bins=30)
# plt.show()
# s.jointplot(pd.to_numeric(d['Rating']),pd.to_numeric(d['Size']),kind='scatter')
# plt.show()
# s.jointplot(pd.to_numeric(d['Rating']),pd.to_numeric(d['Installs']),kind='scatter')
# plt.show()
# s.jointplot(pd.to_numeric(d['Rating']),pd.to_numeric(d['Reviews']),kind='scatter')
# plt.show()
# s.jointplot(pd.to_numeric(d['Price']),pd.to_numeric(d['Installs']),kind='reg')
# plt.show()
# s.barplot(pd.to_numeric(d['Price']),pd.to_numeric(d['Installs']))
# plt.show()
