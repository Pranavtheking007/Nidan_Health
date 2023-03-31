#Regular EDA(Exploratory Data Analysis) & Plotting Libraries
import pandas as pd
import numpy as np
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

df = pd.read_csv('https://raw.githubusercontent.com/Pranavtheking007/Nidan-2.0/main/mental-heath-in-tech-2016_20161114.csv')

columns = []

for i in df.columns:
  columns.append(i)

empty = pd.DataFrame(df.isna().sum())

empty_col = []

for i in range(len(columns)):
  if empty.iloc[i][0]/1432 > 0.5:
    empty_col.append(columns[i])

df.drop(empty_col,axis=1,inplace=True)

Male = ['Male','male','Male ','M','m','man','Cis male','Male.','male 9:1 female, roughly','Male (cis)','nb masculine','Man','Sex is male','cis male','Malr','Dude',"I'm a man why didn't you make this a drop down question. You should of asked sex? And I would of answered yes please. Seriously how much text can this take? ",'mail','M|','Male/genderqueer','male ','Cis Male','cisdude','cis man','MALE']

df.replace(to_replace=Male,
           value="Male",
           inplace=True)

Female = ['Female','female','I identify as female.','female ','woman','fm','f','Cis female ','Genderfluid (born female)','Female or Multi-Gender Femme','woman','female/woman','Cisgender Female','genderqueer woman','fem','Female (props for making this a freeform field, though)',' Female','Cis-woman','Transgender woman','Female','Female assigned at birth ','F','Woman','Female ','female-bodied; no feelings about gender']

df.replace(to_replace=Female,
            value="Female",
           inplace=True)

Trans = ['Bigender','Transitioned, M2F','Other/Transfeminine','mtf','Nonbinary','Unicorn','Male (trans, FtM)','AFAB']

df.replace(to_replace=Trans,
            value="TransGender",
           inplace=True)

Others = list(df['What is your gender?'].unique())
Others.remove('Male')
Others.remove('Female')
Others.remove('TransGender')

df.replace(to_replace=Others,
            value="Not disclosing",
           inplace=True)

df.drop('Do you have previous employers?',axis=1,inplace=True)
df.drop('Have your previous employers provided mental health benefits?',axis=1,inplace=True)
df.drop('Were you aware of the options for mental health care provided by your previous employers?',axis=1,inplace=True)
df.drop('Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?',axis=1,inplace=True)
df.drop('Did your previous employers provide resources to learn more about mental health issues and how to seek help?',axis=1,inplace=True)
df.drop('Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?',axis=1,inplace=True)
df.drop('Do you think that discussing a mental health disorder with previous employers would have negative consequences?',axis=1,inplace=True)
df.drop('Do you think that discussing a physical health issue with previous employers would have negative consequences?',axis=1,inplace=True)
df.drop('Would you have been willing to discuss a mental health issue with your previous co-workers?',axis=1,inplace=True)
df.drop('Would you have been willing to discuss a mental health issue with your direct supervisor(s)?',axis=1,inplace=True)
df.drop('Did you feel that your previous employers took mental health as seriously as physical health?',axis=1,inplace=True)
df.drop('Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces?',axis=1,inplace=True)
df.drop('If you have a mental health issue, do you feel that it interferes with your work when being treated effectively?',axis=1,inplace=True)
df.drop('What US state or territory do you live in?',axis=1,inplace=True)
df.drop('What country do you work in?',axis=1,inplace=True)
df.drop('What US state or territory do you work in?',axis=1,inplace=True)
df.drop('Which of the following best describes your work position?',axis=1,inplace=True)
df.drop('Is your employer primarily a tech company/organization?',axis=1,inplace=True)

Update=[]
for i in df['Are you self-employed?']:
  if i == 1:
    Update.append('Yes')
  if i == 0:
    Update.append('No')

df['Are you self-employed?'] = Update

nltk.download('punkt')
nltk.download('stopwords')

featurizer = TfidfVectorizer(
    stop_words = stopwords.words('english'),
    norm='l1'
)

X = featurizer.fit_transform(df['Why or why not?'])

def get_sentence_score(tfidf_row):
  # Return the non-zero values
  x = tfidf_row[tfidf_row!=0]
  return x.mean()

scores = np.zeros(len(df['Why or why not?']))
for i in range(len(df['Why or why not?'])):
  score = get_sentence_score(X[i,:])
  scores[i] = score

df['Why or why not?'] = scores

Y = featurizer.fit_transform(df['Why or why not?.1'])

scores1 = np.zeros(len(df['Why or why not?.1']))
for i in range(len(df['Why or why not?.1'])):
  score1 = get_sentence_score(Y[i,:])
  scores1[i] = score1

df['Why or why not?.1'] = scores1
df.drop('Do you have previous employers?',axis=1,inplace=True)

cols=[]

for i in df['Have you ever sought treatment for a mental health issue from a mental health professional?']:
  if i == 0:
    cols.append("No")
  else:
    cols.append("Yes")

df['Have you ever sought treatment for a mental health issue from a mental health professional?'] = cols
columns = list(df.columns)
columns.remove('Why or why not?')
columns.remove('Why or why not?.1')
columns.remove('What is your age?')

Country=dict(df["What country do you live in?"].value_counts())

Countries = []
for x, y in Country.items():
  if(y<7):
    Countries.append(x)

country_i = []
for i in range(0,len(Countries)):
  country_i.append(df[df['What country do you live in?'] == f"{Countries[i]}"].index.tolist())

Country_index = []

for i in country_i:
  for j in i:
    Country_index.append(j)

Country_index

df.drop(Country_index,axis=0,inplace=True)

Age=dict(df["What is your age?"].value_counts())

Ages = []
for x, y in Age.items():
  if(y<7):
    Ages.append(x)

Age_i = []
for i in range(0,len(Ages)):
  Age_i.append(df[df['What is your age?'] == Ages[i]].index.tolist())

Age_index = []

for i in Age_i:
  for j in i:
    Age_index.append(j)

Age_index

A = set(Age_index)
B = set(Country_index)
C=A-B
C=list(C)

df.drop(C,axis=0,inplace=True)

ct = make_column_transformer(
    (MinMaxScaler(), ['Why or why not?','Why or why not?.1','What is your age?']),
    (OneHotEncoder(handle_unknown='ignore'),columns))

ct.fit(df)