import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf

Stroke = pd.read_csv("https://raw.githubusercontent.com/kuchbhi-kunal/nidan/main/healthcare-dataset-stroke-data.csv")

Stroke.drop("id",axis=1,inplace = True)

for label, content in Stroke.items():
    if pd.api.types.is_numeric_dtype(content):
        if pd.isnull(content).sum():
            #Fill missing numeric valuees with median
            Stroke[label] = content.fillna(content.median())

Stroke.drop([3116],inplace = True)

X= Stroke.drop('stroke',axis=1)
Y=Stroke['stroke']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

Numeric = []
for label, content in Stroke.items():
    if pd.api.types.is_numeric_dtype(content):
      Numeric.append(label)

Numeric.remove('stroke')
Numeric.remove('hypertension')
Numeric.remove('heart_disease')

Object = []
for label, content in Stroke.items():
    if not(pd.api.types.is_numeric_dtype(content)):
      Object.append(label)

Object.append('hypertension')
Object.append('heart_disease')

ct = make_column_transformer(
    (MinMaxScaler(), Numeric),
    (OneHotEncoder(handle_unknown='ignore'),Object))

ct.fit(X_train)

X_train_ct = ct.transform(X_train)

print(X_train_ct.shape)

model = tf.keras.models.load_model("base\Stroke_model_hdf5_soft.h5")

def Predictions(gender, age, hypertension, heart_disease, ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status,Model=model,ct=ct):
    Para = {
        'gender':[gender],
        'age':[age],
        'hypertension':[hypertension],
        'heart_disease': [heart_disease],
        'ever_married': [ever_married],
        'work_type':[work_type],
        'Residence_type':[Residence_type],
        'avg_glucose_level':[avg_glucose_level],
        'bmi':[bmi],
        'smoking_status':[smoking_status]
    }



    Paras = pd.DataFrame(Para)

    pred = ct.transform(Paras)

    res = Model.predict(pred)

    Res = res.argmax(axis=1)
    RES1 = res[0,Res[0]]

    return Res,RES1