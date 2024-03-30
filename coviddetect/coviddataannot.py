import warnings
import pandas as pd

# Filter warning
warnings.filterwarnings("ignore")

def dataframe_target(df):
    df['Target'] = 0
    return df
     
def annotate_target(row):
    if   ((row['RT_PCR'] == 1) | (row['RT_PCR'] == 2)):
        return "3" 
    elif (row['RT_PCR'] == 0)  & ((row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)):
        return "1"
    elif (row['RT_PCR'] == 0) & ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4) | (row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3) | (row['Cough'] == 1) | (row['Cough'] == 2) | (row['Cough'] == 3) | (row['Fatigue'] == 1) | (row['Fatigue'] == 2) | (row['Headache'] == 1) | (row['LoT_S'] == 1) | (row['GI'] == 1) | (row['Dyspnea'] == 1) | (row['LoS_M_C'] == 1) | (row['Ch_P'] == 1)):
        return "2"
    elif (row['RT_PCR'] == 0) & ((row['Pyrexia'] == 0) & (row['Hypoxemia'] == 0) & (row['Cough'] == 0) & (row['Fatigue'] == 0) & (row['Headache'] == 0) & (row['LoT_S'] == 0) & (row['GI'] == 0) & (row['Dyspnea'] == 0) | (row['LoS_M_C'] == 0) | (row['Ch_P'] == 0)):
        return "0"
    else:
        return "0"

# Annotate Clinical Symptoms & Pysiological Signs Encoded Data
df = pd.read_csv('result/covid_data_encoded.csv')
df = df.assign(Target=df.apply(annotate_target, axis=1))
df.to_csv('result/covid_data_annotated.csv', index=False)

# [0 = Not-Confirmed]
# [1 = Suspected (Needing Lung CT)]
# [2 = Suspected (Needing CBC, ESR, LDH, D-Dimer, & CRP)]
# [3 = Confirmed]