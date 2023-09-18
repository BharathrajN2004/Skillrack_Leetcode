a,b = map(int,input("Enter the values a and b: ").strip().strip())
l=[]
for i in range(2,max(a,b)):
    if a%i==0 or b%i==0:
        if a%1==0 and b%i==0:
            pass
        else:
            l.append(i)
if len(l)==0:
    print("-1")
else:
    print(*l[::-1])