#Regular EDA(Exploratory Data Analysis) & Plotting Libraries
import numpy as np
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('base\Dataset of Diabetes .csv')
Le = LabelEncoder()
df['CLASS']=Le.fit_transform(df['CLASS'])

df['CLASS'] = df['CLASS'].replace([4],1)
df['CLASS'] = df['CLASS'].replace([1],0)

df['CLASS'] = df['CLASS'].replace([3],'Y')
df['CLASS'] = df['CLASS'].replace([0],'N')
df['CLASS'] = df['CLASS'].replace([2],'P')

df.drop('ID',axis=1,inplace=True)
df.drop('No_Pation',axis=1,inplace=True)

Urea_i = []
y=0

for i in df['Urea']:
  if i>12:
    Urea_i.append(y)

  y+=1

HbA1c_i = []
y=0

for i in df['HbA1c']:
  if i<3:
    HbA1c_i.append(y)
  if i>15:
    HbA1c_i.append(y)
  y+=1

Chol_i = []
y = 0

for i in df['Chol']:
  if i<1:
    Chol_i.append(y)
  if i>9:
    Chol_i.append(y)
  y+=1

TG_i = []
y = 0

for i in df['TG']:
  if i>7:
    TG_i.append(y)
  y+=1

HDL_i = []
y=0

for i in df['HDL']:
  if i>3:
    HDL_i.append(y)
  y+=1

LDL_i = []
y=0

for i in df['LDL']:
  if i>6:
    LDL_i.append(y)
  y+=1

VLDL_i = []
y=0

for i in df['VLDL']:
  if i>4:
    VLDL_i.append(y)
  
  y+=1

Urea_i = set(Urea_i)
HbA1c_i = set(HbA1c_i)
Chol_i = set(Chol_i)
TG_i = set(TG_i)
HDL_i = set(HDL_i)
LDL_i = set(LDL_i)
VLDL_i = set(VLDL_i)

Urea_i = Urea_i-HbA1c_i
Urea_i = Urea_i-Chol_i
Urea_i = Urea_i-TG_i
Urea_i = Urea_i-HDL_i
Urea_i = Urea_i-LDL_i
Urea_i = Urea_i-VLDL_i

HbA1c_i = HbA1c_i - Chol_i
HbA1c_i = HbA1c_i - TG_i
HbA1c_i = HbA1c_i - HDL_i
HbA1c_i = HbA1c_i - LDL_i
HbA1c_i = HbA1c_i - VLDL_i

Chol_i = Chol_i - TG_i
Chol_i = Chol_i - HDL_i
Chol_i = Chol_i - LDL_i
Chol_i = Chol_i - VLDL_i

TG_i = TG_i - HDL_i
TG_i = TG_i - LDL_i
TG_i = TG_i - VLDL_i

HDL_i = HDL_i - LDL_i
HDL_i = HDL_i - VLDL_i

LDL_i = LDL_i-VLDL_i

df.drop(Urea_i,axis=0,inplace=True)
df.drop(HbA1c_i,axis=0,inplace=True)
df.drop(Chol_i,axis=0,inplace=True)
df.drop(TG_i,axis=0,inplace=True)
df.drop(HDL_i,axis=0,inplace=True)
df.drop(LDL_i,axis=0,inplace=True)
df.drop(VLDL_i,axis=0,inplace=True)

df = df.reset_index(drop=True)

df.drop('Cr',axis=1,inplace=True)
df.drop('LDL',axis=1,inplace=True)

Y = df['CLASS']
df.drop('CLASS',axis=1,inplace=True)

X_train,X_test,Y_train,Y_test = train_test_split(df, Y, test_size=0.2, random_state=42,stratify=Y)

columns = list(df.columns)
print(columns)
columns.remove('Gender')

ct = make_column_transformer(
    (MinMaxScaler(), columns),
    (OneHotEncoder(handle_unknown='ignore'),['Gender']))

ct.fit(X_train)

model = tf.keras.models.load_model('base\Diabetes_new_07.h5')

def preds(Gender,Age,Urea,HbA1c,Chol,TG,HDL,VLDL,BMI):
  df1 = {
    'Gender':[Gender],
    'AGE':[Age],
    'Urea':[Urea],
    'HbA1c':[HbA1c],
    'Chol':[Chol],
    'TG':[TG],
    'HDL':[HDL],
    'VLDL':[VLDL],
    'BMI':[BMI]
  }

  dfs = pd.DataFrame(df1)
  dfs = ct.transform(dfs)
  res = model.predict(dfs)

  reso=res.argmax(axis=1)
  return reso