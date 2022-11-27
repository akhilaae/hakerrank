n=int(input())
f=0
for i in range(1,int((n/2)+1)):
  if (n-i)%i==0:
    f+=1
print(f)
