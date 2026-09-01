import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna(subset=["TotalCharges"])

# Tenure groups
def create_tenure_group(tenure):
    if tenure <= 12:
        return "0-12 Months"
    elif tenure <= 24:
        return "13-24 Months"
    elif tenure <= 36:
        return "25-36 Months"
    elif tenure <= 48:
        return "37-48 Months"
    elif tenure <= 60:
        return "49-60 Months"
    else:
        return "60+ Months"

df["TenureGroup"] = df["tenure"].apply(create_tenure_group)

# Churn flag
df["ChurnFlag"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# LTV
df["LTV"] = df["MonthlyCharges"] * df["tenure"]

print("========== FEATURE ENGINEERING ==========")

print("\nTenure Groups:")
print(df["TenureGroup"].value_counts())

print("\nAverage LTV:")
print(round(df["LTV"].mean(), 2))

print("\nMedian LTV:")
print(round(df["LTV"].median(), 2))

print("\nChurn Rate:")
print(round(df["ChurnFlag"].mean() * 100, 2), "%")

print("\nFeature engineering completed successfully.")
