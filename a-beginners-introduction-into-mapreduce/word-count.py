# https://towardsdatascience.com/a-beginners-introduction-into-mapreduce-2c912bb5e6ac
import re
import time
from collections import Counter
from functools import reduce
from multiprocessing import Pool

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

data = fetch_20newsgroups().data

def clean_word(word):
    return re.sub(r'[^\w\s]','',word).lower()

def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()
        
def find_top_words(data):
    cnt = Counter()
    for text in data:
        tokens_in_text = text.split()
        tokens_in_text = map(clean_word, tokens_in_text)
        tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
        cnt.update(tokens_in_text)
        
    return cnt.most_common(10)

start = time.time()
print(find_top_words(data))
print((time.time() - start))

#####################
def mapper(text):
    tokens_in_text = text.split()
    tokens_in_text = map(clean_word, tokens_in_text)
    tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
    return Counter(tokens_in_text)

def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1

def chunk_mapper(chunk):
    mapped = map(mapper, chunk)
    reduced = reduce(reducer, mapped)
    return reduced

def chunks(list_of_strings, size_of_chunk):
    for i in range(0, len(list_of_strings), size_of_chunk):
        yield list_of_strings[i:i+size_of_chunk]

pool = Pool(4)

start = time.time()
data_chunks = list(chunks(data, 36))

mapped = pool.map(chunk_mapper, data_chunks)

reduced = reduce(reducer, mapped)
print(reduced.most_common(10))
print((time.time() - start))
