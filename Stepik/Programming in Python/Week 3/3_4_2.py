import re

file1 = open("dataset_3363_3.txt", "r")
file2 = open("output.txt", "w")
new_line = ""
dic = {}
for j in file1.readlines():
    arr = [i for i in j.split()]
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
max_key = arr[0]
max_value = dic[arr[0]]
for i in dic.keys():
    if dic[i] > dic[max_key]:
        max_value = dic[i]
        max_key = i

file2.write(str(str(max_value) + " " + str(max_key)))
file2.close()
