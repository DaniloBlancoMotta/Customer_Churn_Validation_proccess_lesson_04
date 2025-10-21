import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

# Load and prepare data
df = pd.read_csv('telco_customer_churn.csv')
df.columns = df.columns.str.lower().str.replace(' ', '_')
categorical_columns = list(df.dtypes[df.dtypes == 'object'].index)
for c in categorical_columns:
    df[c] = df[c].str.lower().str.replace(' ', '_')
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)
df.churn = (df.churn == 'yes').astype(int)

# Split data
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

y_train = df_train.churn.values
y_val = df_val.churn.values

del df_train['churn']
del df_val['churn']

# Train model
dv = DictVectorizer(sparse=False)
train_dict = df_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

val_dict = df_val.to_dict(orient='records')
X_val = dv.transform(val_dict)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Feature importance analysis
feature_names = dv.get_feature_names_out()
coefficients = model.coef_[0]

# Get top 14 most important features
feature_importance = list(zip(feature_names, coefficients))
feature_importance.sort(key=lambda x: abs(x[1]), reverse=True)
top_features = feature_importance[:14]

# Create bar plot
features, importances = zip(*top_features)
plt.figure(figsize=(10, 8))
plt.barh(range(len(features)), importances)
plt.yticks(range(len(features)), features)
plt.xlabel('Coefficient Value')
plt.title('Top 14 Feature Importances (Logistic Regression Coefficients)')
plt.tight_layout()
plt.show()

# Print feature importance
print("Top 14 Feature Importances:")
for feature, importance in top_features:
    print(f"{feature}: {importance:.4f}")