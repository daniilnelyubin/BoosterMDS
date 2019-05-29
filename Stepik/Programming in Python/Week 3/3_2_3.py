# Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
d = {}
for i in range(n):
    x = int(input())
    if x not in d:
        d[x] = f(x)
        print(d[x])
    else:
        print(d[x])
    




