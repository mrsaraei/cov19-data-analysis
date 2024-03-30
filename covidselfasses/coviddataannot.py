import warnings
import pandas as pd

# Filter warning
warnings.filterwarnings("ignore")

def dataframe_target(df):
    df['Target'] = 0
    return df
     
def annotate_target(row):
    if (row['LoT_S'] == 2):
        return "2"  
    elif (row['Ch_P'] == 1) | (row['LoS_M_C'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Cough'] == 2):
        return "1"
    elif (row['Hypoxemia'] == 3) & (row['Dyspnea'] == 1) & (row['Fatigue'] == 2):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['GI'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Dyspnea'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['GI'] == 1):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Dyspnea'] == 1):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['Headache'] == 1):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['GI'] == 1):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1):
        return "1"        
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Headache'] == 1) & (row['GI'] == 1):
        return "1"       
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1):
        return "1"       
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['GI'] == 1) & (row['Dyspnea'] == 1):
        return "1"           
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2):
        return "1"            
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1):
        return "1"                
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['GI'] == 1):
        return "1"                   
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Dyspnea'] == 1):
        return "1"                    
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['Headache'] == 1):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['GI'] == 1):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1) & (row['GI'] == 1):
        return "1"
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1):
        return "1"    
    elif (row['Hypoxemia'] == 1) & (row['GI'] == 1) & (row['Dyspnea'] == 1):
        return "1" 
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['Headache'] == 1):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['GI'] == 1):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & (row['GI'] == 1):
        return "1"   
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1):
        return "1"   
    elif (row['Fatigue'] == 2) & (row['Headache'] == 1) & (row['GI'] == 1):
        return "1"
    elif (row['Fatigue'] == 2) & (row['Headache'] == 1) & (row['Dyspnea'] == 1):
        return "1"
    elif (row['Fatigue'] == 2) & (row['GI'] == 1) & (row['Dyspnea'] == 1):
        return "1"
    elif (row['Headache'] == 1) & (row['GI'] == 1) & (row['Dyspnea'] == 1):
        return "1"
    else:
        return "0"

# Annotate Clinical Symptoms & Pysiological Signs Encoded Data
df = pd.read_csv('result/covid_data_encoded.csv')
df = df.assign(Target=df.apply(annotate_target, axis=1))
df.to_csv('result/covid_data_annotated.csv', index=False)

# [0 = Unsuspected]
# [1 = Suspected]
# [2 = Probable]