import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import sklearn
import joblib

df = pd.read_csv('https://raw.githubusercontent.com/Pranavtheking007/Nidan-2.0/main/Student%20Mental%20health.csv')

for label, content in df.items():
    if pd.api.types.is_numeric_dtype(content):
        if pd.isnull(content).sum():
            #Fill missing numeric valuees with median
            df[label] = content.fillna(content.median())

Others = list(df['What is your course?'].unique())

Others.remove('BCS')
Others.remove('Engineering')
Others.remove('BIT')
Others.remove('KOE')

df.replace(to_replace=Others,
           value="Others",
           inplace=True)

df.drop('Marital status',axis=1,inplace=True)
df.drop('Timestamp',axis=1,inplace=True)

Years = list(df['Your current year of Study'].unique())

for i in range(1,5):
  df.replace(to_replace=[f'year {i}', f'Year {i}'],
            value=f"Year {i}",
             inplace=True)

Y = df['Do you have Depression?']
X=df.drop('Do you have Depression?',axis=1)

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

Columns = list(X_train.columns)

Columns.remove('Age')

ct = make_column_transformer(
    (MinMaxScaler(), ['Age']),
    (OneHotEncoder(handle_unknown='ignore'),Columns))

ct.fit(X_train)

model = joblib.load('base\Mental_Student.joblib')


def predictions(Choose_your_gender,age,What_is_your_course,Your_current_year_of_Study,What_is_your_CGPA,Do_you_have_Anxiety,Do_you_have_Panic_attack,Did_you_seek_any_specialist_for_a_treatment):
    preds = {
        'Choose your gender': [Choose_your_gender],
        'Age':[age],
        'What is your course?':[What_is_your_course],
        'Your current year of Study':['Year 4'],
        'What is your CGPA?':[What_is_your_CGPA],
        'Do you have Anxiety?':[Do_you_have_Anxiety],
        'Do you have Panic attack?':[Do_you_have_Panic_attack],
        'Did you seek any specialist for a treatment?':[Did_you_seek_any_specialist_for_a_treatment]
    }

    dfs = pd.DataFrame(preds)
    dfs = ct.transform(dfs)
    res = model.predict(dfs)

    reso=res.argmax(axis=1)
    return reso