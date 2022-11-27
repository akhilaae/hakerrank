n=int(input())
t_rank=1
e,g,m,h=map(int,input().split())
t_sum=e+g+m+h
for i in range(n-1):
  if n>=1 and n<=1000:
    a,b,c,d=map(int,input().split()) 
    sum=a+b+c+d
    if sum>t_sum:
      t_rank+=1
  else:
    print("invalid input")
print(t_rank)
