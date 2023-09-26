a,b=map(int,input().strip().split())
for i in range(2,a+1):
    if a%i==0 and b%i!=0:print(i,end=" ")