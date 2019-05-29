arr = list()
last_element = 0
while not last_element == "end":
    temp_arr = list()
    for i in input().split():
        last_element = i
        if i == "end":
            break
        temp_arr.append(int(i))
    if last_element == "end":
        break
    arr.append(temp_arr)

new_arr = list()

for i in range(len(arr)):
    temp_arr = list()

    for j in range(len(arr[0])):
        sum = 0
        if i + 1 >= len(arr):
            sum += arr[0][j]
        else:
            sum += arr[i + 1][j]
        if j + 1 >= len(arr[i]):
            sum += arr[i][0]
        else:
            sum += arr[i][j + 1]
        sum += arr[i][j - 1]
        sum += arr[i - 1][j]
        temp_arr.append(sum)
    new_arr.append(temp_arr)
for i in range(len(new_arr)):
    for j in range(len(new_arr[0])):
        print(new_arr[i][j], end=" ")
    print()





