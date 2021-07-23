import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

'''
This script is for cleaning the water potability dataset and preparing it for use in 
EDA and Modeling
'''
DATA_PATH = "./Data/water_potability.csv"

# read in df
df = pd.read_csv(DATA_PATH)
print(df.head())

# count number of total rows
print(f'Shape of dataframe: {df.shape}')
# count number of rows with NaNs
print('Number of NaNs for each feature')
print(df.isnull().sum(axis = 0))

# lets try removing all NaNs and seeing how many observations we're left with
df2 = df[df['ph'].notna()]
df2 = df2[df2['Sulfate'].notna()]
df2 = df2[df2['Trihalomethanes'].notna()]

print(f'New dataframe shape without NaNs: {df2.shape}')
print(f'{df.shape[0] - df2.shape[0]} rows lost')

# we lose 1265 observations with NaNs, lets do some data imputing using the mean of the columns with missing values 

X = df.drop(['Potability'], axis=1)
imp_mean = SimpleImputer(missing_values=np.nan, strategy = 'mean')
imp_mean.fit(X)
X = pd.DataFrame(imp_mean.transform(X), columns=['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity'])
X['Potability'] = df['Potability']

# now that we've filled the missing values, we can save this dataframe to begin our EDA 
X.to_csv('./Data/cleaned_water_potability.csv', index=False)
