import pandas as pd
df = pd.read_csv('data/titanic.csv')
print(df.columns)
print(df["sex"].unique())
female_df = df[df["sex"]=="female"]
print(female_df)