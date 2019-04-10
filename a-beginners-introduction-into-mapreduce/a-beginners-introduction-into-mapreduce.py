# https://towardsdatascience.com/a-beginners-introduction-into-mapreduce-2c912bb5e6ac
import time
def find_longest_string(list_of_strings):
    longest_string = None
    longest_string_len = 0

    for s in list_of_strings:
        if len(s) > longest_string_len:
            longest_string_len = len(s)
            longest_string = s
    return longest_string


list_of_strings = ['abc', 'python', 'dima']

start = time.time()
print(find_longest_string(list_of_strings))
print((time.time() - start)) 

################
large_list_of_strings = list_of_strings*1000000
start = time.time()
print(find_longest_string(large_list_of_strings))
print((time.time() - start)) 

################
start = time.time()
list_of_string_lens = [len(s) for s in list_of_strings]
list_of_string_lens = zip(list_of_strings, list_of_string_lens)

max_len = max(list_of_string_lens, key=lambda t: t[1])
print(max_len)
print((time.time() - start)) 

##################

mapper = len
def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c

import functools

start = time.time()
mapped = map(mapper, list_of_strings)
mapped = zip(list_of_strings, mapped)

reduced = functools.reduce(reducer, mapped)
print(reduced)
print((time.time() - start))

#####################


def chunks(list_of_strings, size_of_chunk):
    for i in range(0, len(list_of_strings), size_of_chunk):
        yield list_of_strings[i:i+size_of_chunk]

start = time.time()
data_chunks = list(chunks(list_of_strings, 30))

reduced_all = []

for chunk in data_chunks:
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)

    reduced_chunk = functools.reduce(reducer, mapped_chunk)
    reduced_all.append(reduced_chunk)

reduced = functools.reduce(reducer, reduced_all)
print(reduced)
print((time.time() - start))

########################

def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk)
    mapped_chunk = zip(chunk, mapped_chunk)
    return functools.reduce(reducer, mapped_chunk)

start = time.time()
data_chunks = list(chunks(list_of_strings, 30))

mapped = map(chunks_mapper, data_chunks)

reduced = functools.reduce(reducer, mapped)
print(reduced)
print((time.time() - start))


########################
from multiprocessing import Pool
pool = Pool(8)

start = time.time()
data_chunks = list(chunks(large_list_of_strings, 8))

mapped = pool.map(chunks_mapper, data_chunks)

reduced = functools.reduce(reducer, mapped)
print(reduced)
print((time.time() - start))



