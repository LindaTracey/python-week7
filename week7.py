# iris_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    url = "https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/iris_dataset.csv"
    df = pd.read_csv(url)
    print("✅ Dataset loaded successfully!")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")
    exit()

# Display first few rows
print("\n🔍 First 5 rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\n📋 Dataset Info:")
print(df.info())

print("\n🕳️ Missing Values:")
print(df.isnull().sum())

# Drop missing values
df_cleaned = df.dropna()

# Add index for simulated time-series
df_cleaned['Index'] = range(len(df_cleaned))

# Summary statistics
print("\n📊 Summary Statistics:")
print(df_cleaned.describe())

# Group by species and compute mean
print("\n📈 Mean values grouped by species:")
grouped = df_cleaned.groupby("target").mean()
print(grouped)

# ------------------- Visualization Section -------------------

# Set Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Line Chart: Sepal Length over Index
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_cleaned, x='Index', y='sepal length (cm)', hue='target')
plt.title("Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart: Average Petal Length per Species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.show()

# 3️⃣ Histogram: Sepal Width Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df_cleaned['sepal width (cm)'], bins=20, kde=True)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_cleaned, x='sepal length (cm)', y='petal length (cm)', hue='target')
plt.title("Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.tight_layout()
plt.show()
