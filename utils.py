import pandas as pd
def load_titanic_female():
    df = pd.read_csv('data/titanic.csv')
    print(df.columns)
    print(df["sex"].unique())
    female_df = df[df["sex"]=="female"]
    print(female_df)

load_titanic_female()