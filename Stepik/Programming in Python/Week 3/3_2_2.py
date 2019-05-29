# put your python code here

arr  = [i for i in input().split()]
d = {}
for i in arr:
    i = i.lower()
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for key in d.keys():
    print(str(key)+" "+str(d[key]))
    


