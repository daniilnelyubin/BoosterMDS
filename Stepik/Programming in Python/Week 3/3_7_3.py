# put your python code here

d = int(input())
dic = list()
for i in range(d):
    dic.append(input())
l = int(input())
set_of_list = set(dic)
dic_out = {}
for i in range(l):
    string = input().split()
    for j in string:
        in_dic = False
        for k in set_of_list:
            if k.lower()==j.lower():
                in_dic = True
                break
        if not in_dic and j not in dic_out:
            dic_out[j] = 1
            print(j)
            
    



