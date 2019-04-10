# cd d:/app/images
# docker build . -t hatespeechdetect
# docker run -p 3000:5000 -d hatespeechdetect
# curl -d "{\"text\": \"Please respect each other.\"}" http://192.168.99.100:3000/predict  ip address from docker-machine ip default

FROM python:3.6
RUN pip install scikit-learn==0.20.2  firefly-python==0.1.15
COPY app.py hatespeech.joblib.z ./
CMD firefly app.predict --bind 0.0.0.0:${}
EXPOSE 5000
