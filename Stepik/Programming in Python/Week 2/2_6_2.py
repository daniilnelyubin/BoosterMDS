n = int(input())
count = 0
current_num = 1
while count<n:
    for i in range(current_num):
        print(current_num,end=" ")
        count+=1
        if count>=n:
            break
    current_num+=1




