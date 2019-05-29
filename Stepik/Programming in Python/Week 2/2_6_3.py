arr = [int(i) for i in input().split()]
x = int(input())

arr_of_index = list()
for counter,value in enumerate(arr):
    if value==x:
        arr_of_index.append(counter)
if len(arr_of_index)==0:
    print("Отсутствует")
else:
    for i in arr_of_index:
        print(i,end=" ")




