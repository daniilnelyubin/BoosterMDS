def modify_list(l):
    for i in range(len(l)-1,-1,-1):
        if not l[i]%2==0:
            l.pop(i)
        else:
            l[i] = l[i]//2

