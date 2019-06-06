import re

file1 = open("dataset_3363_4.txt", "r")
file2 = open("output.txt", "w")
new_line = ""
dic = {}
mean_f = 0
mean_s = 0
mean_t = 0
count = 0
for j in file1.readlines():
    string = [i for i in j.split(';')]
    first = int(string[1])
    second = int(string[2])
    third = int(string[3])
    mean_f+=first
    mean_s+=second
    mean_t+=third
    new_line += str((first + second + third) / 3) + "\n"
    count+=1

new_line+= str(mean_f/count)+" "
new_line+= str(mean_s/count)+" "
new_line+= str(mean_t/count)+"\n"
file2.write(new_line)
file2.close()
