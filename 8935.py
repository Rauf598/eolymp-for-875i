a,b=(map(int, input().spilt()))
L=[]
for i in range(a, b + 1):
    if i%2==1:
        L.append(i)
print(*L)