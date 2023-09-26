a,b,c=map(int,input().strip().split())
if c%2==0: print((a-b)*(c//2))
else: print((a*((c+1)//2))-(b*(c//2)))