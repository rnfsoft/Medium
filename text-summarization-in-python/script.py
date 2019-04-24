import os
from gensim.summarization.summarizer import summarize # Gensim

path = os.path.dirname(os.path.realpath(__file__))
filename = 'adv_alad.txt'

with open(os.path.join(path, filename)) as f:
    story = f.read()
    print(summarize(story)) # Gensim
    




