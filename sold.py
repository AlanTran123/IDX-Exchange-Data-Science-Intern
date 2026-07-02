import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load all CSV files
# -----------------------------

data_folder = "data"

csv_files = sorted(glob.glob(os.path.join(data_folder, "*.csv")))

if len(csv_files) == 0:
    print("No CSV files found.")
    exit()

dfs = []

for file in csv_files:
    df = pd.read_csv(file, low_memory=False)
    dfs.append(df)

sold_df = pd.concat(dfs, ignore_index=True)

print("\nFinished loading data!")
print(f"Number of CSV files: {len(csv_files)}")
print(f"Rows: {sold_df.shape[0]}")
print(f"Columns: {sold_df.shape[1]}")

print("\nFirst 5 rows:")
print(sold_df.head())

# -----------------------------
# Filter the data
# -----------------------------

sold_df = sold_df[
    (sold_df["PropertyType"] == "Residential") &
    (sold_df["PropertySubType"] == "SingleFamilyResidence")
]

print("\nAfter filtering:")
print(sold_df.shape)

print(f"\nNumber of Residential SingleFamilyResidence homes: {len(sold_df)}")

# -----------------------------
# Dataset information
# -----------------------------

print("\nDataset Info")
sold_df.info()

# -----------------------------
# Columns for exploration
# -----------------------------

columns = [
    "ClosePrice",
    "LivingArea",
    "BedroomsTotal",
    "BathroomsTotalInteger",
    "LotSizeAcres"
]

eda_df = sold_df[columns]

# -----------------------------
# Data types
# -----------------------------

print("\nData Types")
print(eda_df.dtypes)

# -----------------------------
# Missing values
# -----------------------------

print("\nMissing Values")
print(eda_df.isnull().sum())

# -----------------------------
# Summary statistics
# -----------------------------

print("\nSummary Statistics")
print(eda_df.describe())

# -----------------------------
# Create plots folder
# -----------------------------

plots_folder = "plots"
os.makedirs(plots_folder, exist_ok=True)

# -----------------------------
# Histograms
# -----------------------------

for column in columns:

    plt.figure(figsize=(8, 5))

    plt.hist(eda_df[column].dropna(), bins=50)

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig(os.path.join(plots_folder, f"{column}_histogram.png"))

    plt.close()

# -----------------------------
# Boxplots
# -----------------------------

for column in columns:

    plt.figure(figsize=(5, 6))

    plt.boxplot(eda_df[column].dropna())

    plt.title(f"Boxplot of {column}")

    plt.tight_layout()

    plt.savefig(os.path.join(plots_folder, f"{column}_boxplot.png"))

    plt.close()

print(f"\nAll plots have been saved to the '{plots_folder}' folder.")