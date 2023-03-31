#Regular EDA(Exploratory Data Analysis) & Plotting Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import tensorflow as tf
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/Pranavtheking007/Nidan-2.0/main/heart.csv')

df.drop('fbs',axis=1,inplace=True)

thal_i = []
y=0

for i in df['thal']:
  if i == 0:
    thal_i.append(y)

  y+=1

restecg_i = []
y=0

for i in df['restecg']:
  if i == 2:
    restecg_i.append(y)

  y+=1

chol_i = []
y=0

for i in df['chol']:
  if i>500:
    chol_i.append(y)

  y+=1

df.drop(thal_i,axis=0,inplace=True)
df.drop(restecg_i,axis=0,inplace=True)
df.drop(chol_i,axis=0,inplace=True)

Y = df['target']
df.drop('target',axis=1,inplace=True)

X_train,X_test,Y_train,Y_test = train_test_split(df, Y, test_size=0.2, random_state=42,stratify=df['ca'])

ct = make_column_transformer(
    (MinMaxScaler(), ['slope','ca','thal','exang','restecg','cp','sex']),
    (OneHotEncoder(handle_unknown='ignore'),['age','chol','trestbps','thalach','oldpeak']))

ct.fit(X_train)

model = tf.keras.models.load_model("base\Heart_Disease.h5")

def predictions(cp,ca,sex,age,trestbps,thal,fbs,restecg,thalach,exang,oldpeak,slope,chol,Model=model,CT=ct):
  pred = {
    'cp':[cp],
    'ca':[ca],
    'sex':[0],
    'age':[age],
    'trestbps':[trestbps],
    'thal':[thal],
    'fbs':[fbs],
    'restecg':[restecg],
    'thalach':[thalach],
    'exang':[0],
    'oldpeak':[oldpeak],
    'slope':[slope],
    'chol':[chol]
  }

  dfs = pd.DataFrame(pred)
  dfs_ct = CT.transform(dfs)
  print('Its a small small world')

  res = Model.predict(dfs_ct)
  reso=res.argmax(axis=1)
  return reso