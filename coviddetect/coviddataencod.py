import warnings
import pandas as pd

# Filter warning
warnings.filterwarnings("ignore")

def encode_pyrexia(x):
    if x >= 36.5 and x <= 37.8:
        return 0
    elif x >= 37.9 and x <= 39:
        return 1
    elif x >= 39.1 and x <= 40:
        return 2
    elif x >= 40.1 and x <= 41.4:
        return 3
    else:
        return 4

def encode_spo2(x):
    if x >= 95:
        return 0
    elif x >= 93 and x < 95:
        return 1
    elif x >= 90 and x < 93:
        return 2
    else:
        return 3

def encode_cough(x):
    if x == "Wet":
        return 1
    elif x == "Dry":
        return 2
    elif x == "Others":
        return 3
    else:
        return 0

def encode_fatigue(x):
    if x == "Mild":
        return 1
    elif x == "Severe":
        return 2
    else:
        return 0

def encode_lot_s(x):
    if x == "Mild":
        return 1
    elif x == "Severe":
        return 2
    else:
        return 0

def encode_headache(x):
    if x == "Yes":
        return 1
    else:
        return 0

def encode_gi(x):
    if x == "Yes":
        return 1
    else:
        return 0

def encode_dyspnea(x):
    if x == "Yes":
        return 1
    else:
        return 0

def encode_los_m_c(x):
    if x == "Yes":
        return 1
    else:
        return 0

def encode_chp(x):
    if x == "Yes":
        return 1
    else:
        return 0

def encode_contact(x):
        if x == "Close":
            return(1)
        elif x == "Far":
            return(2)
        else:
            return(0)
        
def encode_age(x):
        if x >= 60:
            return(1)
        else:
            return(0)
        
def encode_anamnesis(x):
        if x == "Weak":
            return(1)
        elif x == "Moderate":
            return(2)
        elif x == "Strong":
            return(3)
        else:
            return(0)
        
def encode_gender(x):
        if x == "Male":
            return(1)
        else:
            return(0)

def encode_pcr(x):
        if x < 38:
            return(1)
        elif x >= 38 and x <= 40:
            return(2)
        else:
            return(0)

# Encode Physiological Signs
df_phs = pd.read_csv('docs/covid_physiologicalsign_rawdata.csv')
df_phs['Pyrexia'] = df_phs['Pyrexia'].apply(encode_pyrexia)
df_phs['Hypoxemia'] = df_phs['Hypoxemia'].apply(encode_spo2)

# Encode Clinical Symptoms
df_cls = pd.read_csv('docs/covid_clinicalsymptom_rawdata.csv')
df_cls['Cough'] = df_cls['Cough'].apply(encode_cough)
df_cls['Fatigue'] = df_cls['Fatigue'].apply(encode_fatigue)
df_cls['LoT_S'] = df_cls['LoT_S'].apply(encode_lot_s)
df_cls['Headache'] = df_cls['Headache'].apply(encode_headache)
df_cls['GI'] = df_cls['GI'].apply(encode_gi)
df_cls['Dyspnea'] = df_cls['Dyspnea'].apply(encode_dyspnea)
df_cls['LoS_M_C'] = df_cls['LoS_M_C'].apply(encode_los_m_c)
df_cls['Ch_P'] = df_cls['Ch_P'].apply(encode_chp)

# Encode Electronic Health Records
df_ehr = pd.read_csv('docs/covid_electronichealthrecord_rawdata.csv')
df_ehr['Contact'] = df_ehr['Contact'].apply(encode_contact)
df_ehr['Age'] = df_ehr['Age'].apply(encode_age)
df_ehr['Anamnesis'] = df_ehr['Anamnesis'].apply(encode_anamnesis)
df_ehr['Gender'] = df_ehr['Gender'].apply(encode_gender)

# Encode PCR-Realtime Laboratoy Test
df_pcr = pd.read_csv('docs/covid_pcr_rawdata.csv')
df_pcr['RT_PCR'] = df_pcr['RT_PCR'].apply(encode_pcr)

# Concate Clinical Symptoms & Pysiological Signs Encoded Data
df = pd.concat([df_phs, df_cls, df_ehr, df_pcr], axis=1)
df.to_csv('result/covid_data_encoded.csv', index=False)

# print("-------- fever(Temperature) --------")
## [-3 = Severe Hypothermia(20-28'C)], [-2 = Moderate Hypothermia(28-32'C)], [-1 = Mild Hypothermia(32-35'C)]
## [0 = Normal(36.5-37.8'C)], [1 = Mild Pyrexia(37.9-39'C)], [2 = Moderate Pyrexia(39.1-40'C)], [3 = High Pyrexia(40.1-41.5'C)]
## [4 = Hyperpyrexia(>41.5'C)]

# print("--------- Hypoxemia (SPo2) --------")
## [0 = Normal (SpO2>=95%)]
## [1 = Mild Hypoxemia (93%=<SpO2>95%)]
## [2 = Moderate Hypoxemia (90%=<SpO2<93%)]
## [3 = Severe Hypoxemia (SpO2<90%)]

# print("-------- Cough --------")
## [0 = Not/Without Cough]
## [1 = Wet Cough]
## [2 = Dry Cough]
## [3 = Other Types of Cough]

# print("-------- Fatigue (Tiredness) --------")
## [0 = Not/Without Fatigue]
## [1 = Mild Fatigue]
## [2 = Severe Fatigue]

# print("------------ Loss of Taste & Smell ----------")
## [0 = Not/Without Loss of Taste & Smell]
## [1 = Mild Loss of Taste & Smell]
## [2 = Severe Loss of Taste & Smell]

# print("------------ Contact Background ---------------")
## [0 = Not/Without Contact]
## [1 = Close Contact]
## [2 = Far Contact]

# Print ("--- Comorbidities & Past Medical History (PMH)/Anamnesis ---")
## [0 = Not/Without Anamnesis]
## [1 = Weak Anamnesis]
## [2 = Moderate Anamnesis]

# print("----------- RT-PCR ------------")
## [0 = Negative Result(>40)]
## [1 = Positive Result(<38)]
## [2 = Probable Result (38>=x<=40)]