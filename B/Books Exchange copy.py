n = int(input())
for i in range(n):
    f = int(input())
    a = list(map(int, input().split()))
    s = 
    day = 0 
    ap = [1:len(a):1]
    while len(s) != len(a):
        day+=1
        for j in range(len(a)):
            ap[a[j]]=ap[j]
            if ap[a[j]]== j+1:
                

