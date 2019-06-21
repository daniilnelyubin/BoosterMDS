import re
import numpy as np
import scipy.spatial.distance

file = open("data/sentences.txt", 'r')
words = dict()
idx = 0
count_of_sentences = 0
for j, line in enumerate(file.readlines()):
    for i, word in enumerate(re.split(r'[^a-z]', line)):
        word = word.lower()
        if not word == "" and word not in words:
            words[word] = idx
        idx += 1
    count_of_sentences += 1
file.close()
file = open("data/sentences.txt", 'r')
array = np.zeros((count_of_sentences, idx))

for j, line in enumerate(file.readlines()):
    for i, word in enumerate(re.split(r'[^a-z]', line)):
        word = word.lower()
        if not word == "":
            index = words[word]
            array[j,index] += 1
first = array[0]
line = ""
min =2
min_= 2
idx_min = -1
idx_min_ = -1
for idx,sentense in enumerate(array[1:]):
    cosinus =  scipy.spatial.distance.cosine(first,sentense)
    if cosinus<min:
        idx_min_ = idx_min
        idx_min = idx
        min_ = min
        min=cosinus
print(idx_min,idx_min_)
