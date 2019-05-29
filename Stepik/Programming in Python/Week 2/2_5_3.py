string = input().split()
was_arr = list()
for i in string:
    if string.count(i)>1 and i not in was_arr:
        was_arr.append(i)
        print(i,end=" ")





