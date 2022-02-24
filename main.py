import pandas as pd
import numpy as np


df_ocurrence = pd.read_excel('occurrence.xlsx')
df_divipola = pd.read_excel('DIVIPOLA_20210416.xlsx')

columns = [
    "stateProvince",
    "spcm",
    "spc",
    ]

for column in columns:
    np.in1d(df_ocurrence[column], df_divipola[column])
