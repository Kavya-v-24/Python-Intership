
#fib series
n=int(input("Enter the number of terms:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=  b,a+b
    
#last line can be written as a=b and b=a+b it is same as assigning alues to a and b in second line
    
#or
n=int(input("\nEnter the number of terms:"))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b
    