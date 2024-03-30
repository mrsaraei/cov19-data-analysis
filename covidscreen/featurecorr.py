import warnings
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Filter warnings
warnings.filterwarnings("ignore")

# Load DataFrame using explicit encoding (if needed)
df = pd.read_csv('result/covid_data_preprocessed.csv')

# Select Features and Target Data efficiently
df_f = df.iloc[:, :-1]
df_t = df.iloc[:, -1]

# Calculate Feature Correlation directly
CF = df_f.corr().abs()

# Filter top-correlated features efficiently
top_corr_features = CF.nlargest(10, columns=df_f.columns).index

# print top features
print("\nFeature Importances:\n", top_corr_features)

# Create the "plots" directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Plot heatmap with clear title and labels
plt.figure(figsize=(12, 10))
sns.heatmap(df_f[top_corr_features].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Top-Correlated Features")
plt.xlabel("Features")
plt.ylabel("Features")
plt.savefig('plots/Feature_Correlation_Heatmap.tiff')
plt.close()

