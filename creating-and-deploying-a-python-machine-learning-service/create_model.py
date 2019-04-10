# https://towardsdatascience.com/creating-and-deploying-a-python-machine-learning-service-a06c341f020f

import pandas as pd
import re
import os
import time

path = os.path.dirname(os.path.realpath(__file__))
file_name = 'labeled_data.csv'
df = pd.read_csv(os.path.join(path, file_name ), usecols=['class', 'tweet'])
# print(df[:10]) eg. 2  !!! RT @mayasolovely: As a  
df['tweet'] = df['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower())) # re.sub(pattern, replacement, input), converting all text to lowercase and removing non-alphabetic characters.
# print(df[:10]) eg. 2   rt mayasolovely as a 
# df['class'] hate speech: 0, offensive language: 1, neither: 2

from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from stop_words import get_stop_words
import nltk

start = time.time()
clf = make_pipeline(
    TfidfVectorizer(stop_words=nltk.corpus.stopwords.words("english")),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf = clf.fit(X=df['tweet'], y=df['class'])

text = "I hate you, please die!"
print(clf.predict_proba([text])[0])
print((time.time() - start))

from sklearn import externals

model_filename = "hatespeech.joblib.z"
externals.joblib.dump((clf), model_filename)
