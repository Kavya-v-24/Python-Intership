#problem1 print the number
x=input("enter the number:")
print(x)

#problem 2 artimetic operators
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
add=a+b
dif=a-b
product= a*b
div=a/b
print("sum of a and b:",add)
print("difference between a and b:",dif)
print("product  of a and b:",product)
print("div of a and b:",div)

#problem3 comparision operator
x=input("enter value of x:")
y=input("enter value of y:")
if (x>y):
    print(x,"is greater")
elif(y>x):
    print(y,"is greater")
else:
    print("Both are equal")

#problem5 sting manipulation   
s=input("enter a string:")
print(len(s))         #prints length of the string
s=s.upper()           #converting string into uppercase
print(s)

#problem6 conditional operator
i=int(input("enter a number:"))
if (i>0):
    print(i,"is positive number")
elif(i<0):
    print(i,"is negative number")
else:
    print("tne number is 0")

#problem8 lists
fruits=["apple","banana","cherry"]
print(fruits)
fruits.append("orange")
print(fruits)

#problem 9 tuples
tup=(10,"hello",True)
print(tup)
#tup[0]=20
#print(tup)
lis=list(tup)
lis[0]=20
print(lis)

#problem10 dictionary
#create a dic where the keys are fruits and values are their colors and add new key_alue pair
dic={"apple":"red","banana":"yellow","grapes":"green"}
print(dic)
dic.update({"orange":"orange"})
print(dic)