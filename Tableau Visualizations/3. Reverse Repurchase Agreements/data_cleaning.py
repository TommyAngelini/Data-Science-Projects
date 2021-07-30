'''
This script will clean the reverse repo dataset 
'''

import pandas as pd
import numpy as np
import seaborn as sb

df = pd.read_csv('./Data/rrpData.csv')
print(df)

df = df[df['RRPONTSYD'] != '.']

sb.pointplot(df, df['DATE'], df['RRPONTSYD'])