n = int(input())
f = list(map(int, input().split()))
tf = sum(f)
_counter = 0
for i in range(1,6):
    if (tf+i) % (n+1) != 1:
        _counter +=1

print(_counter)