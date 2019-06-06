file = open("dataset_3380_5.txt", "r")
dic = {}
for line in file.readlines():
    string = line.split()
    if string[0] not in dic:
        dic[string[0]] = [int(string[2]), 1]
    else:
        dic[string[0]][0] += int(string[2])
        dic[string[0]][1] += 1
for i in range(1,12):
    if str(i) not in dic:
        print(str(i) + " -")
    else:
        print(str(i) + " " + str(dic[str(i)][0] / dic[str(i)][1]))
