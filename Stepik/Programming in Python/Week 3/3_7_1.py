n = int(input())
dic = {}

for i in range(n):
    string = input().split(";")
    first_team_score = int(string[1])
    second_team_score = int(string[3])
    if string[0] not in dic:
        dic[string[0]]=[0,0,0,0,0]
    if string[2] not in dic:
        dic[string[2]]=[0,0,0,0,0]
        
    first_score = 0
    second_score = 0
    
    if first_team_score>second_team_score:
        dic[string[0]][0]+=1
        dic[string[0]][1]+=1
        dic[string[0]][4]+=3
        dic[string[2]][0]+=1
        dic[string[2]][3]+=1
        
    elif first_team_score==second_team_score:
        dic[string[0]][0]+=1
        dic[string[0]][2]+=1
        dic[string[0]][4]+=1
        dic[string[2]][0]+=1
        dic[string[2]][2]+=1
        dic[string[2]][4]+=1
    else:
        dic[string[2]][0]+=1
        dic[string[2]][1]+=1
        dic[string[2]][4]+=3
        dic[string[0]][0]+=1
        dic[string[0]][3]+=1
for i in dic.keys():
    print(i+":",end="")
    for j in dic[i]:
        print(j,end=" ")
    print()
    
    
    
        




