w,h,k=map(int,input().split())
f=0
for i in range(0,k):
    f=f+((2*(w+h-8*i))-4)
print(f)
