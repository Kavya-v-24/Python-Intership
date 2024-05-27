#logical operator to check if its both divisible by 2 and 3
num=int(input("enter the number"))
if(num%2==0 and num%3==0): #checks whether both executes or not
    print("yes")
else:
    print("no")
    
 #logical operator to check if its either divisible by 2 and 3  
digit=int(input("enter the number"))
if(digit%2==0 or digit%3==0): #checks either any one will execute or not
    print("yes")
else:
    print("no")
    