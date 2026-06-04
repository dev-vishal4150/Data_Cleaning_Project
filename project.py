import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dummy Raw Dataset
np.random.seed(42)
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 101, 107, 108, 109],
    'Name': ['Amit', 'Rahul', 'Priya', 'Sonia', 'Vijay', 'Anjali', 'Amit', 'Raj', 'Neha', 'Vikram'],
    'Age': [25, np.nan, 29, 45, 34, 120, 25, 28, np.nan, 31],
    'Salary': [50000, 60000, np.nan, 85000, 70000, 55000, 50000, 92000, 62000, 1500000],
    'Department': ['IT', 'HR', 'Data Science', 'IT', 'HR', 'Data Science', 'IT', 'Management', 'HR', 'Data Science']
}
df_raw = pd.DataFrame(data)

# 2. Data Cleaning
df_cleaned = df_raw.drop_duplicates()
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].median())
df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df_cleaned['Salary'].mean())
df_cleaned.loc[df_cleaned['Age'] > 100, 'Age'] = df_cleaned['Age'].median()
salary_cap = df_cleaned['Salary'].quantile(0.95)
df_cleaned.loc[df_cleaned['Salary'] > salary_cap, 'Salary'] = salary_cap

# 3. Data Visualization
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.barplot(x='Department', y='Salary', data=df_cleaned, ax=axes[0], palette='Blues_d', ci=None)
axes[0].set_title('Average Salary by Department')

sns.histplot(df_cleaned['Age'], bins=5, kde=True, ax=axes[1], color='purple')
axes[1].set_title('Age Distribution')

plt.tight_layout()
plt.savefig('insights_dashboard.png')
