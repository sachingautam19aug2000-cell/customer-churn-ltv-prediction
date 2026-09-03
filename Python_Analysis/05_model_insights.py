import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna(subset=["TotalCharges"])

df = df.drop(columns=["customerID"])

df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

X = df.drop(columns=["Churn"])
y = df["Churn"]

categorical_columns = X.select_dtypes(
    include=["object"]
).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)

model = LogisticRegression(max_iter=1000)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

pipeline.fit(X_train, y_train)

feature_names = (
    pipeline
    .named_steps["preprocessor"]
    .get_feature_names_out()
)

coefficients = (
    pipeline
    .named_steps["model"]
    .coef_[0]
)

importance = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": coefficients
})

importance["Absolute_Importance"] = (
    importance["Coefficient"].abs()
)

importance = importance.sort_values(
    "Absolute_Importance",
    ascending=False
)

print("========== MODEL INSIGHTS ==========")

print(
    importance[
        ["Feature", "Coefficient", "Absolute_Importance"]
    ].head(15)
)

print("\nPositive coefficient = higher churn tendency")
print("Negative coefficient = lower churn tendency")

print("\nModel insights completed successfully.")
