import warnings
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scikitplot as skplt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier

# Filter warnings
warnings.filterwarnings("ignore")

# Load the preprocessed dataset
df = pd.read_csv('result/covid_data_preprocessed.csv')

# Split the dataset into features (X) and target variable (y)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Create machine learning models
models = {
    'KNN': KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2),
    'DTC': DecisionTreeClassifier(max_depth=None, min_samples_split=2, min_samples_leaf=1),
    'GNB': GaussianNB(),
    'SVM': SVC(probability=True),
    'LRG': LogisticRegression(solver='liblinear', penalty='l2', C=1.0),
    'RFC': RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, min_samples_leaf=1),
    'GBC': GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3),
    'XGB': XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3),
    'ABC': AdaBoostClassifier(n_estimators=100, algorithm="SAMME.R", random_state=0),
}

# Initialize dictionaries to store results
train_times = {}
pred_times = {}
train_accuracies = {}
test_accuracies = {}
baseline_accuracies = {}
kfold_avg_accuracies = {}
t_pred_probs = {}
t_preds = {}

# Train and evaluate machine learning models
for model_name, model in models.items():
    # Training
    train_start_time = time.perf_counter()
    model.fit(X_train, y_train)
    train_end_time = time.perf_counter()
    train_times[model_name] = train_end_time - train_start_time

    # Prediction
    pred_start_time = time.perf_counter()
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    pred_end_time = time.perf_counter()
    pred_times[model_name] = pred_end_time - pred_start_time

    # Accuracy
    train_accuracies[model_name] = accuracy_score(y_train, y_train_pred)
    test_accuracies[model_name] = accuracy_score(y_test, y_test_pred)

    # Baseline Accuracy
    baseline_accuracies[model_name] = accuracy_score(y_test, model.predict(X_test))

    # K-Fold Cross Validation
    kfold_avg_accuracy = np.mean(cross_val_score(model, X, y, cv=10, scoring='accuracy'))
    kfold_avg_accuracies[model_name] = kfold_avg_accuracy

    # ROC-AUC scores
    pred_prob = model.predict_proba(X_test)
    t_pred_probs[model_name] = pred_prob
    
    # Classification Report
    t_preds[model_name] = y_test_pred

# Print training and prediction times
print("\nTraining Times:")
for model_name, train_time in train_times.items():
    print(f"{model_name}: {train_time:.4f} seconds")

print("\nPrediction Times:")
for model_name, pred_time in pred_times.items():
    print(f"{model_name}: {pred_time:.4f} seconds")

# Print training and testing accuracies
print("\nTraining Accuracies:")
for model_name, train_accuracy in train_accuracies.items():
    print(f"{model_name} Train Accuracy: {train_accuracy:.3f}")

print("\nTesting Accuracies:")
for model_name, test_accuracy in test_accuracies.items():
    print(f"{model_name} Test Accuracy: {test_accuracy:.3f}")

# Print overfitting-underfitting values
print("\nOverfitting-Underfitting Values:")
for model_name in models:
    ou_value = train_accuracies[model_name] - test_accuracies[model_name]
    print(f"{model_name} Overfitting-Underfitting Value: {ou_value:.3f}")

# Print baseline accuracies
print("\nBaseline ML Models Accuracy:")
for model_name, baseline_accuracy in baseline_accuracies.items():
    print(f"{model_name} Baseline Accuracy: {baseline_accuracy:.3f}")

# Print k-fold cross-validation average accuracies
print("\nK-Fold Cross Validation Average Accuracy:")
for model_name, kfold_avg_accuracy in kfold_avg_accuracies.items():
    print(f"{model_name} K-Fold C.V. Avg. Accuracy: {kfold_avg_accuracy:.3f}")

# Print roc-auc score
print("\nML Models ROC-AUC Scores:")
for model_name, pred_prob in t_pred_probs.items():
    roc_auc = roc_auc_score(y_test, pred_prob, multi_class='ovo', average='weighted')
    print(f"{model_name} ROC-AUC Score: {roc_auc:.3f}")
    
# Print classification reports
print("\nClassification Reports:")
for model_name, preds in t_preds.items():
    report = classification_report(y_test, preds)
    print(f"{model_name} Classification Report:")
    print(report)

# Calculate and print confusion matrices
print("\nConfusion Matrices:")
for model_name, preds in t_preds.items():
    matrix = confusion_matrix(y_test, preds)
    print(f"{model_name} Confusion Matrix:")
    print(matrix)
    print()

# Create the "plots" directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

plt.figure(figsize=(10, 6))
for model_name, model in models.items():
    # Plot confusion matrix
    skplt.metrics.plot_confusion_matrix(y_test, preds)
    plt.title(f"{model_name} Confusion Matrix")
    plt.savefig(f"plots/{model_name}_confusion_matrix.tiff")
    plt.close()  

    # Plot learning curve
    skplt.estimators.plot_learning_curve(model, X, y)
    plt.title(f"{model_name} Learning Curve")
    plt.savefig(f"plots/{model_name}_learning_curve.tiff")
    plt.close()  

    # Plot precision-recall curve
    skplt.metrics.plot_precision_recall_curve(y_test, pred_prob)
    plt.title(f"{model_name} Precision Recall Curve")
    plt.savefig(f"plots/{model_name}_precision_recall_curve.tiff")
    plt.close()  
    
    # Plot ROC curve
    skplt.metrics.plot_roc_curve(y_test, pred_prob)
    plt.title(f"{model_name} ROC Curve")
    plt.savefig(f"plots/{model_name}_roc_curve.tiff")
    plt.close()  
   
# [0 = No Sign/Symptom]
# [1 = Mild Level]
# [2 = Moderate Level]
# [3 = Severe Level]
# [4 = Critical Level]