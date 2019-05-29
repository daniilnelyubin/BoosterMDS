arr = list()
while True:
    arr.append(int(input()))
    if sum(arr)==0:
        sum = 0
        for j in arr:
            sum+=j**2
        print(sum)
        break






