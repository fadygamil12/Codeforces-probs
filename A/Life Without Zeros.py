a = int(input())
b = int(input())
c = a+b
ast = str(a)
bst = str(b)
cst = str(c)
astm = ""
bstm = ""
cstm = ""
for i in range(len(ast)):
    if ast[i] != "0":
        astm += ast[i]
for i in range(len(bst)):
    if bst[i] != "0":
        bstm += bst[i]
for i in range(len(cst)):
    if cst[i] != "0":
        cstm += cst[i]
am = int(astm)
bm = int(bstm)
cm = int(cstm)

if am+bm == cm:
    print("YES")
else:
    print("NO")