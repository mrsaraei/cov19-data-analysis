import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.impute import SimpleImputer
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE

# Filter warning
warnings.filterwarnings("ignore")

def load_data(input_path):
    df = pd.read_csv(input_path)
    return df

def split_data(df):
    df_f = df.iloc[:, :-1]
    df_t = df['Target']
    return df_f, df_t

def normalize_data(df_f):
    scaler = MinMaxScaler(feature_range=(0, 1))
    return scaler.fit_transform(df_f)

def concat_data(df_f, df_t):
    df_f = pd.DataFrame(df_f, columns=[f'feature_{i}' for i in range(df_f.shape[1])])
    return pd.concat([df_f, df_t], axis=1)

def handle_missing_values(df):
    df.replace("?", np.nan, inplace=True)
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    return imp.fit_transform(df)

def remove_duplicates(df):
    df_deduplicated = df.drop_duplicates().reset_index(drop=True)
    return df_deduplicated

def remove_outliers(df):
    ISF = IsolationForest(contamination=0.1)
    outliers = ISF.fit_predict(df)
    return df[outliers != -1]

def visualize_data(df):
    plt.hist(df)
    plt.xlabel('Data Value', fontsize=11)
    plt.ylabel('Data Frequency', fontsize=11)
    plt.title('Visualize the Preprocessed Data')
    plt.savefig('plots/covid_data_distribution.tif', dpi=600)
    plt.close()

def save_data(df):
    pd.DataFrame(df).to_csv('result/covid_data_preprocessed.csv', index=False)

def save_feature_name(df, output_file):
    row_names = df.columns.values.tolist()
    first_row_df = pd.DataFrame([row_names], columns=row_names)
    first_row_df.to_csv(output_file, index=False)

def preprocess_csv(input_path):
    
    # Load CSV-based input data
    df = load_data(input_path)

    # Convert feature names to string type
    df.columns = df.columns.astype(str) 

    # Split features and target data
    df_f, df_t = split_data(df)
    
    print('\nPrint Initial Information Before Preprocessing:')
    print('***********************************************\n')
    print('Feature:', df_f.shape)
    print('Target:', df_t.shape)
    print() 
    print(df.head(5))
    print()
    print(df.info())
    print("\nSample and (Feature + Target):", df.shape)
    print("\nMissing Values (NaN):")
    print(df.isnull().sum())
    print("\nDuplicate Records:", df.duplicated().sum())  
    print('\nData After Balancing:', sorted(Counter(df_t).items()))

    # Normalize features
    df_normalized = normalize_data(df_f)

    # Concatenate features and target data
    df_concat = concat_data(df_normalized, df_t)

    # Handle missing values
    df_preprocessed = handle_missing_values(pd.DataFrame(df_concat).fillna(method='ffill'))

    # Remove duplicates
    df_preprocessed = remove_duplicates(pd.DataFrame(df_preprocessed))

    # Remove outliers
    df_preprocessed = remove_outliers(df_preprocessed)

    print('\nPrint Initial Information After Preprocessing:')
    print('**********************************************\n')
    print(df_preprocessed.head(5))
    print()
    print(df_preprocessed.info())
    print("\nSample & (Feature + Target):", df_preprocessed.shape)
    print("\nMissing Values (NaN):")
    print(df_preprocessed.isnull().sum())
    print("\nDuplicate Records:", df_preprocessed.duplicated().sum())

    # OverSampling (OS)
    OS = SMOTE(k_neighbors=1)
    df_f_os, df_t_os = OS.fit_resample(df_preprocessed.iloc[:, :-1], df_preprocessed.iloc[:, -1])

    # Print initial information After Balancing
    print('\nData After Balancing:', sorted(Counter(df_t_os).items()))

    # Combine oversampled features and target
    df_preprocessed_os = pd.concat([df_f_os, df_t_os], axis=1)

    # Visualize the preprocessed data
    visualize_data(df_preprocessed_os)

    # Save the preprocessed data
    save_data(df_preprocessed_os)

    # Save the names of the features as a CSV file
    save_feature_name(df_preprocessed_os.iloc[:, :-1], 'result/featurename.csv')

    # Return the preprocessed DataFrame
    return df_preprocessed_os

# Call the function with the file path as an argument
preprocessed_df = preprocess_csv('result/covid_data_annotated.csv')

# [0 = Normal]
# [1 = Suspected]
# [2 = Probable]