first = int(input())
second = int(input())
first_ = int(input())
second_ = int(input())
print(str(" "),end="\t")
for i in range(first_,second_+1):
    print(str(i),end="\t")
print(end='\n')  
for i in range(first,second+1):
    print(str(i),end="")
    for j in range(first_,second_+1):
        print("\t"+ str(i*j),end="")
    print()
        




