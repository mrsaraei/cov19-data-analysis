import warnings
import pandas as pd

# Filter warning
warnings.filterwarnings("ignore")

def dataframe_target(df):
    df['Target'] = 0
    return df
     
def annotate_target(row):
    if  (row['RT_PCR'] == 0):
        return "0"
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & (row['Hypoxemia'] == 3) & (row['LoS_M_C'] == 1):
        return "4" 
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Hypoxemia'] == 3) & (row['Dyspnea'] == 1)) & ((row['CSS'] == 4) | (row['CSS'] == 5)):
        return "3"
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Hypoxemia'] == 2) & ((row['Dyspnea'] == 1) | (row['Ch_P'] == 1)) & ((row['CSS'] == 1) | (row['CSS'] == 2) | (row['CSS'] == 3))):
        return "2"
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Pyrexia'] == 1) & (row['Hypoxemia'] == 1) & ((row['Cough'] == 2) | (row['Fatigue'] == 1) | (row['Headache'] == 1) | (row['LoT_S'] == 1) | (row['GI'] == 1) | (row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1))):
        return "1"
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Pyrexia'] == 1) | (row['Cough'] == 2) | (row['Fatigue'] == 1) | (row['Headache'] == 1) | (row['LoT_S'] == 1) | (row['GI'] == 1) | (row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)) & ((row['Age'] == 1) | (row['Anamnesis'] == 3)):     
        return "1"    
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Pyrexia'] == 1) | (row['Hypoxemia'] == 1) | (row['Cough'] == 2) | (row['Fatigue'] == 1) | (row['Headache'] == 1) | (row['LoT_S'] == 1) | (row['GI'] == 1) | (row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)) & (row['Contact'] == 1):
        return "1"
    elif ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)) & ((row['Pyrexia'] == 0) & (row['Hypoxemia'] == 0) & (row['Cough'] == 0) & (row['Fatigue'] == 0) & (row['Headache'] == 0) & (row['LoT_S'] == 0) & (row['GI'] == 0) & (row['Dyspnea'] == 0) & (row['LoS_M_C'] == 0) | (row['Ch_P'] == 0)):
        return "0" 
    else:
        return "0"

# Annotate Clinical Symptoms & Pysiological Signs Encoded Data
df = pd.read_csv('result/covid_data_encoded.csv')
df = df.assign(Target=df.apply(annotate_target, axis=1))
df.to_csv('result/covid_data_annotated.csv', index=False)

# [0 = No Sign/Symptom]
# [1 = Mild Level]
# [2 = Moderate Level]
# [3 = Severe Level]
# [4 = Critical Level]