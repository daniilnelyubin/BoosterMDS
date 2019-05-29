arr = [int(i) for i in input().split()]
if len(arr)==1:
    print(arr[0])
else:
    for i in range(len(arr)):
        if i==len(arr)-1:
            print(arr[i-1]+arr[0])
        else:
            print(arr[i-1]+arr[i+1],end=" ")
    




