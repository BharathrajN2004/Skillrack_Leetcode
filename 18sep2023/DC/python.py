a,b = map(int,input("Enter the values a and b: ").strip().split())
l=[]
for i in range(2,max(a,b)+1):
    if a%i==0 or b%i==0:
        if a%i==0 and b%i==0:
            pass
        else:
            l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l[::-1])
