# need to install "pip install firefly-python" for testing
# CMD: firefly app.predict --bind 127.0.0.1:5000
# CMD: curl -d "{\"text\": \"Please respect each other.\"}" http://127.0.0.1:5000/predict
# curl location C:\Program Files\Git\mingw64\bin\

from sklearn import externals
import os

file_name = 'hatespeech.joblib.z'
path = os.path.dirname(os.path.realpath(__file__))
model_filename = os.path.join(path, file_name)

clf = externals.joblib.load(model_filename)

def predict(text):
    probas = clf.predict_proba([text])[0]
    return {'hate speech': probas[0], 'offensive language': probas[1], 'neither': probas[2]}

#print (predict("I hate you, please die"))