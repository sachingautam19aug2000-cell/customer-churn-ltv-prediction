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



import pandas as pd
import matplotlib.pyplot as plt

df["Churn"].value_counts().plot(kind="bar")
plt.title("Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Customers")
plt.show()

pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar", stacked=True)
plt.title("Contract vs Churn")
plt.ylabel("Customers")
plt.show()


pd.crosstab(df["InternetService"], df["Churn"]).plot(kind="bar", stacked=True)
plt.title("Internet Service vs Churn")
plt.ylabel("Customers")
plt.show()


df.boxplot(column="MonthlyCharges", by="Churn")
plt.title("Monthly Charges by Churn")
plt.suptitle("")
plt.show()


df.boxplot(column="tenure", by="Churn")
plt.title("Tenure by Churn")
plt.suptitle("")
plt.show()
