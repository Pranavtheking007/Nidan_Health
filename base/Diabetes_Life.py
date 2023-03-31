#Regular EDA(Exploratory Data Analysis) & Plotting Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import tensorflow as tf

dia = pd.read_csv("https://raw.githubusercontent.com/kuchbhi-kunal/nidan/main/diabetes_binary_5050split_health_indicators_BRFSS2015.csv")
dia.drop("Education",axis=1,inplace=True)
dia.drop("Fruits",axis=1,inplace=True)
dia.drop("AnyHealthcare",axis=1,inplace=True)
dia.drop("NoDocbcCost",axis=1,inplace=True)
dia.drop("MentHlth",axis=1,inplace=True)
dia.drop("CholCheck",axis=1,inplace=True)

X = dia.drop("Diabetes_binary",axis=1)
Y = dia["Diabetes_binary"]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42,stratify=Y)

print(X_train.columns)
#Create a Column Trnasformer
ct = make_column_transformer(
    (MinMaxScaler(), ['BMI', 'Income','PhysHlth','Age','GenHlth']),
    (OneHotEncoder(handle_unknown='ignore'),['HighBP','HighChol','Smoker','Stroke','HeartDiseaseorAttack','PhysActivity','Veggies','HvyAlcoholConsump','DiffWalk','Sex']))

ct.fit(X_train)

model = tf.keras.models.load_model('base\Diabetes_model_Binary_hdf5.h5')

def prediction(BMI,Age,sex,Income,PhysHlth,GenHlth,HighBP,HighChol,Smoker,Stroke,HeartDisease,PhysActivity,Veggies,HeavyAlcoholConsump,DiffWalk):
    preds = {
        'BMI':[BMI],
        'Age':[Age],
        'Sex':[sex],
        'Income':[Income],
        'PhysHlth':[PhysHlth],
        'GenHlth':[GenHlth],
        'HighBP':[HighBP],
        'HighChol':[HighChol],
        'Smoker':[Smoker],
        'Stroke':[Stroke],
        'HeartDiseaseorAttack':[HeartDisease],
        'PhysActivity':[PhysActivity],
        'Veggies':[Veggies],
        'HvyAlcoholConsump':[HeavyAlcoholConsump],
        'DiffWalk':[DiffWalk]
    }

    df1 = pd.DataFrame(preds)
    df_01 = ct.transform(df1)

    res = model.predict(df_01)
    reso=res.argmax(axis=1)
    return reso