import pandas as pd
import mlflow
from statsmodels.stats.proportion import proportions_ztest

# Load dataset
df = pd.read_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/cleaned_ab_data.csv")

# Split groups
control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

# Conversions
conversions = [control["converted"].sum(),
               treatment["converted"].sum()]

# Visitors
visitors = [control["converted"].count(),
            treatment["converted"].count()]

# Z-test
z_stat, p_value = proportions_ztest(conversions, visitors)

# Conversion rates
control_rate = control["converted"].mean()
treatment_rate = treatment["converted"].mean()

# MLflow tracking
with mlflow.start_run():

    mlflow.log_metric("control_conversion_rate", control_rate)
    mlflow.log_metric("treatment_conversion_rate", treatment_rate)
    mlflow.log_metric("z_score", z_stat)
    mlflow.log_metric("p_value", p_value)

    print("Experiment logged in MLflow")

print("Control Rate:", control_rate)
print("Treatment Rate:", treatment_rate)
print("Z-score:", z_stat)
print("P-value:", p_value)