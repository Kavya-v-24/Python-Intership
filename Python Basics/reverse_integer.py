#reverse the number
num=int(input("enter the number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("reversed number:",rev)

#or this method can be used for reversing the strings

the_number=input("enter the number")
reversed=the_number[::-1]
print("reversed number:",reversed)