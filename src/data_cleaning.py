import pandas as pd

# Load dataset
df = pd.read_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/ab_data.csv")
print("Dataset Shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

# remove duplicates
df = df.drop_duplicates()

# check mismatched rows
df = df[(df['group'] == 'treatment') & (df['landing_page'] == 'new_page') |
        (df['group'] == 'control') & (df['landing_page'] == 'old_page')]

# save cleaned data
df.to_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/cleaned_ab_data.csv", index=False)
print("Cleaned dataset saved.")