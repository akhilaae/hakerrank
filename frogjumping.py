t=int(input())
if t>=1 and t<=1000:
    for i in range(t):
        a,b,c=map(int,input().split())
        if a>=1 and b>=1 and c>=1 and a<=10**9 and b<=10**9 and c<=10**9:
            if c%2==0:
                print(int((a-b)*c//2))
            else:
                print(int((a-b)*(c//2)+a))
