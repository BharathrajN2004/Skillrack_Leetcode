a, b = map(int, input().strip().split())
k = []
for i in range(a):
    l = list(map(int, input().strip().split()))
    if i == 0 or i == a-1:
        for p in l:
            k.append(p)
    else:
        k.append(l[0])
        k.append(l[b-1])
for i in k:
    if i % 2 != 0:
        print("NO")
        exit(0)
print("YES")
