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




df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df = df.drop("customerID", axis=1)
print(df.select_dtypes(include="object").columns)
df = pd.get_dummies(df, drop_first=True, dtype=int)
X = df.drop("Churn", axis=1)
y = df["Churn"]
print(X.shape)
print(y.shape)


from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, classification_report, roc_auc_score

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
y_prob = model.predict_proba(X_test)[:, 1]
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05,
    random_state=42,
    eval_metric="logloss"
)

xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
print("XGBoost Accuracy:", accuracy_score(y_test, xgb_pred))
print(classification_report(y_test, xgb_pred))
xgb_prob = xgb_model.predict_proba(X_test)[:, 1]
print("XGBoost ROC-AUC:", roc_auc_score(y_test, xgb_prob))


print("Logistic Regression ROC-AUC:", roc_auc_score(y_test, y_prob))
print("XGBoost ROC-AUC:", roc_auc_score(y_test, xgb_prob))


import shap

explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test)

shap.summary_plot(shap_values, X_test)

df["LTV"] = df["MonthlyCharges"] * df["tenure"]

print("Average LTV:", df["LTV"].mean())
print(df.groupby("Churn")["LTV"].mean())

df_model = X_test.copy()
df_model["Churn_Probability"] = xgb_model.predict_proba(X_test)[:, 1]

print(df_model.sort_values("Churn_Probability", ascending=False).head(10))

import joblib

joblib.dump(xgb_model, "xgb_churn_model.pkl")


