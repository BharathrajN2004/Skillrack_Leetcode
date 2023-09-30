m="abcdefghijklmnopqrstuvwxyz"
a=int(input().strip())
k=2
for i in range(a):
    print(m[:k])
    if i%2==0:k-=1
    else:k+=3