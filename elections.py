n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        x=0
        y=a-b+1
        z=a-c+1
    elif b>a and b>c:
        x=b-a+1
        y=0
        z=b-c+1
    elif c>a and c>b:
        x=c-a+1
        y=c-b+1
        z=0
    elif a==b and b==c:
        x=y=z=1
    elif a==b and a>c:
        x=y=1
        z=a-c+1
    elif a==c and a>b:
        x=z=1
        y=a-b+1
    elif b==c and b>a:
        y=z=1
        x=b-a+1
    print(x,y,z)
