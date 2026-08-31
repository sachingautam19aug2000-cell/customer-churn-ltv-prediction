import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
