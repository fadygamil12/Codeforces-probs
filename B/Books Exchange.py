n = int(input())
for i in range(n):
    f = int(input())
    a = list(map(int, input().split()))
    s = []
    def daysc(id , days , kid):
            days += 1 
            if a[id-1] == kid:
                k = days
                return k 
            else:
                return daysc(a[id-1] , days, kid)
    
    for j in range(len(a)):
        s.append(daysc(j+1,0,j+1))
    print(*s)
