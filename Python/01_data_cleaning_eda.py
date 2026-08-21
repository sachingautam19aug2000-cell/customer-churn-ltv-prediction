import pandas as pd

df = pd.read_csv("../WA_Fn-UseC_-Telco-Customer-Churn.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].isnull().sum())
print(df[df["TotalCharges"].isnull()])
print(df[df["TotalCharges"].isnull()][["customerID", "tenure", "MonthlyCharges", "TotalCharges"]])

print(df[df["TotalCharges"].isnull()]["tenure"].value_counts())
print(df["Churn"].value_counts())
print(df["Churn"].value_counts(normalize=True) * 100)
print(pd.crosstab(df["Contract"], df["Churn"]))
print(pd.crosstab(df["InternetService"], df["Churn"]))
print(pd.crosstab(df["PaymentMethod"], df["Churn"]))
print(df.groupby("Churn")["tenure"].mean())
print(df.groupby("Churn")["MonthlyCharges"].mean())
print(df.groupby("Churn")["TotalCharges"].mean())
