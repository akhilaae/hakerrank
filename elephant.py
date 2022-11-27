x=int(input())
min=0
if x<=5:
  min=1
elif x>5 and x%5==0:
  min=(x//5)
elif x>5 and x%5!=0:
  min=(x//5)+1
print(min)
