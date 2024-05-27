#sum of natural numbers

n=int(input("enter the number:"))
sum=0
for i in range (1,n+1):
    sum+=i
print("sum of first ",n,"natural numbers:",sum)
