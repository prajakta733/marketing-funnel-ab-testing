import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/cleaned_ab_data.csv")

# Funnel stages
visitors = len(df)
landing_page = len(df["landing_page"])
converted = df["converted"].sum()

stages = ["Visitors", "Landing Page Views", "Conversions"]
values = [visitors, landing_page, converted]

# Plot funnel chart
plt.figure(figsize=(8,5))
plt.barh(stages, values)

plt.title("Marketing Funnel Analysis")
plt.xlabel("Number of Users")

plt.savefig("C:/mlflow_vscode_practice/marketing_funnel_project/outputs/funnel_chart.png")
plt.close()