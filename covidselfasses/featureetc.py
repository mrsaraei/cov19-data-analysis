import warnings
import os
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt

# Filter warnings
warnings.filterwarnings("ignore")

# Load DataFrame
df = pd.read_csv('result/covid_data_preprocessed.csv')

# Select Features and Target Data
df_f = df.iloc[:, :-1]
df_t = df.iloc[:, -1]

# Set random state for reproducibility
ETC = ExtraTreesClassifier(random_state=42)
ETC.fit(df_f, df_t)

# Print important features with meaningful formatting
print("\nFeature Importances:\n", ETC.feature_importances_)

# Create the "plots" directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Plot feature importance with clear labels and formatting
plt.figure(figsize=(12, 10))
FI = pd.Series(ETC.feature_importances_, index=df_f.columns)
FI.nlargest(10).plot(kind='bar')
plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("10 Most Important Features for ExtraTreesClassifier")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/ETC_Important_Feature.png')
plt.close()
