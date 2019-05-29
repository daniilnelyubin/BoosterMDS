a = int(input())
b = int(input())

if a<b:
    i=1
    while not a*i%b==0:
        i+=1
    print(a*i)
else:
    i=1
    while not b*i%a==0:
        i+=1
    print(b*i)
