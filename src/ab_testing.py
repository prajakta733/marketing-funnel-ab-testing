import pandas as pd
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/cleaned_ab_data.csv")

# Separate groups
control = df[df["group"] == "control"]
treatment = df[df["group"] == "treatment"]

# Number of conversions
conversions = [control["converted"].sum(),
               treatment["converted"].sum()]

# Number of users
visitors = [control["converted"].count(),
            treatment["converted"].count()]

# Z-test
z_stat, p_value = proportions_ztest(conversions, visitors)

print("Z-score:", z_stat)
print("P-value:", p_value)

# Conversion rates
control_rate = control["converted"].mean()
treatment_rate = treatment["converted"].mean()

print("\nControl Conversion Rate:", control_rate)
print("Treatment Conversion Rate:", treatment_rate)

# Decision
if p_value < 0.05:
    result = "Significant difference between pages"
else:
    result = "No significant difference"

print("\nResult:", result)

# Save results to outputs folder
with open("C:/mlflow_vscode_practice/marketing_funnel_project/outputs/ab_test_results.txt", "w") as f:
    f.write(f"Z-score: {z_stat}\n")
    f.write(f"P-value: {p_value}\n")
    f.write(f"Control Conversion Rate: {control_rate}\n")
    f.write(f"Treatment Conversion Rate: {treatment_rate}\n")
    f.write(f"Result: {result}\n")

# Create conversion rate chart
rates = [control_rate, treatment_rate]
labels = ["Control", "Treatment"]

plt.bar(labels, rates)
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")

plt.savefig("C:/mlflow_vscode_practice/marketing_funnel_project/outputs/conversion_rate_chart.png")
plt.show()