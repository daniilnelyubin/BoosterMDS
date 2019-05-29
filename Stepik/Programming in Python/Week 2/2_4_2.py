string = input()
count = 0
last = 0
if len(string)==1:
    print(string+"1")
for i in range(1,len(string)):
    if string[last]==string[i]: 
        count+=1
    else:
        count+=1
        print(string[last]+str(count),end="")
        last = i
        count = 0
    if i==len(string)-1:
        count+=1
        print(string[i]+str(count),end="")




