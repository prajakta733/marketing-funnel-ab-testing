import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("C:/mlflow_vscode_practice/marketing_funnel_project/data/cleaned_ab_data.csv")

print("Dataset Shape:", df.shape)

# -----------------------------------
# 1 Conversion Rate Overall
# -----------------------------------

conversion_rate = df["converted"].mean()
print("Overall Conversion Rate:", conversion_rate)

# -----------------------------------
# 2 Conversion Rate by Group
# -----------------------------------

group_conversion = df.groupby("group")["converted"].mean()

print("\nConversion Rate by Group:")
print(group_conversion)

group_conversion.plot(kind="bar")

plt.title("Conversion Rate by Group")
plt.ylabel("Conversion Rate")
plt.show()

# -----------------------------------
# 3 Conversion Rate by Landing Page
# -----------------------------------

page_conversion = df.groupby("landing_page")["converted"].mean()

print("\nConversion Rate by Landing Page:")
print(page_conversion)

page_conversion.plot(kind="bar")

plt.title("Conversion Rate by Landing Page")
plt.ylabel("Conversion Rate")
plt.show()

# -----------------------------------
# 4 Users Distribution
# -----------------------------------

sns.countplot(x="group", data=df)

plt.title("User Distribution by Group")
plt.show()

# -----------------------------------
# 5 Conversion Distribution
# -----------------------------------

sns.countplot(x="converted", data=df)

plt.title("Conversion Distribution")
plt.show()