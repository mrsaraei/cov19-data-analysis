import warnings
import os
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt

# Filter warnings
warnings.filterwarnings("ignore")

# Load DataFrame
df = pd.read_csv('result/covid_data_preprocessed.csv')

# Select Features and Target Data
df_f = df.iloc[:, 0: -1]
df_t = df.iloc[:, -1]

# Apply SelectKBest with informative output
BF = SelectKBest(score_func = chi2, k = 10)
fit = BF.fit(df_f, df_t)

print("\nSelected Features:\n", df_f.columns[fit.get_support()])  # Print selected features
print("\nFeature scores:\n", pd.DataFrame(fit.scores_, index=df_f.columns))  # Print feature scores

# Create the "plots" directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Plot feature importance with clear labels and formatting
plt.figure(figsize=(10, 6))  
FS = pd.DataFrame({'Feature': df_f.columns, 'Score': fit.scores_})
FS = FS.sort_values(by='Score', ascending=False)  
plt.bar(FS['Feature'], FS['Score'])
plt.xlabel("Chi-Squared Score")
plt.ylabel("Feature")
plt.title("Feature Importance using SelectKBest (Chi-Squared)")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/SelectKBest_Important_Feature.png')
plt.close()