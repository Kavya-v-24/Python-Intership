#factorial of numbers

n=int(input("enter the number:"))
fact=1
for i in range (1,n+1):
    fact*=i
print("factorial of ",n,"is:",fact)
