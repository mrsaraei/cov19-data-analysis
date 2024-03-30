import warnings
import os
import pandas as pd
from sklearn.linear_model import LassoCV
import matplotlib.pyplot as plt

# Filter warnings
warnings.filterwarnings("ignore")

# Load DataFrame
df = pd.read_csv('result/covid_data_preprocessed.csv')

# Select Features and Target Data
df_f = df.iloc[:, 0: -1]
df_t = df.iloc[:, -1]

# Set random state for reproducibility 
reg = LassoCV(random_state=42)
reg.fit(df_f, df_t)

# Extract coefficients for plotting
coef = pd.Series(reg.coef_, index = df_f.columns)

# Print the best score and some informative statistics
print("\nBest alpha using LassoCV: {:.4f}".format(reg.alpha_))
print("Best score (R-squared) using LassoCV: {:.4f}".format(reg.score(df_f, df_t)))
print("Number of features with non-zero coefficients:", sum(coef != 0))
print("Number of features eliminated by Lasso:", sum(coef == 0))

# Create the "plots" directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Plot feature importance with clear labels and formatting
plt.figure(figsize=(10, 6))
imp_coef = coef.sort_values(ascending=False)
imp_coef.plot(kind="bar")
plt.xlabel("Coefficient Magnitude")
plt.ylabel("Feature")
plt.title("Feature Importance using LassoCV")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('plots/LassoCV_Important_Feature.tiff')  
plt.close()  
