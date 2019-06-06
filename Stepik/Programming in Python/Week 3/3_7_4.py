# put your python code here
n = int(input())
x,y = 0,0

for i in range(n):
    line = input().split()
    direction = line[0]
    steps = int(line[1])
    if direction == "север":
        y+=steps
    if direction == "запад":
        x-=steps
    if direction == "юг":
        y-=steps
    if direction == "восток":
        x+=steps
        
print(x,y)



