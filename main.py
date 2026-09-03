import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
np.random.seed(42)

# Step 1 Simulate Logistics Dataset
n_samples = 1000
data = {
    "distance_km": np.random.uniform(2, 50, n_samples),
    "shipment_volume_units": np.random.randint(10, 200, n_samples),
    "actual_transit_hrs": np.random.uniform(0.5, 6.0, n_samples),
    "fuel_cost_usd": np.random.uniform(5, 80, n_samples),
    "labor_cost_usd": np.random.uniform(15, 120, n_samples),
    "delay_minutes": np.random.exponential(scale=20, size=n_samples)
}
df = pd.DataFrame(data)
df["total_cost_usd"] = df["fuel_cost_usd"] + df["labor_cost_usd"]

# Step 2. EDA: Print Summary Statistics
print("--- CENTRAL TENDENCIES & STATISTICAL SUMMARY ---")
print(df.describe().T[["mean", "50%", "std", "min", "max"]])
print("\n")

# Step 3. Visualization 1: Transit Duration Distribution (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df["actual_transit_hrs"], kde=True, color="skyblue", bins=30)
plt.title("Distribution of Delivery Transit Durations", fontsize=12, fontweight="bold")
plt.xlabel("Actual Transit Duration (Hours)")
plt.ylabel("Shipment Frequency")
plt.tight_layout()
plt.savefig("transit_duration_distribution.png")
plt.close()

# Step 4. Visualization 2: Distance vs. Fuel Cost (Scatter Plot)
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x="distance_km", 
    y="fuel_cost_usd", 
    hue="shipment_volume_units", 
    palette="viridis", 
    alpha=0.8
)
plt.title("Route Distance vs. Fuel Cost by Shipment Volume", fontsize=12, fontweight="bold")
plt.xlabel("Distance (km)")
plt.ylabel("Fuel Cost ($)")
plt.tight_layout()
plt.savefig("distance_vs_fuel_cost.png")
plt.close()

# Step 5. Visualization 3: Operational Correlation Heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Logistics Metric Correlation Matrix", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.savefig("logistics_correlation_heatmap.png")
plt.close()

print("[+] EDA Script Executed Successfully. Visualizations saved as PNG files.")

