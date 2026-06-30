import pandas as pd
def analyze(df):
    print("\n SHAPE")
    print(f"Rows and coulmns: {df.shape}")
    print("\n COLUMN TYPES")
    print(df.dtypes)
    print("\n EMPTY CELLS")
    print(df.isnull().sum())
    print("\n STATS")
    print(df.describe())
