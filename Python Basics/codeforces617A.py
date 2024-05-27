#An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.
#Input:The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.
#Outputp:rint the minimum number of steps that elephant needs to make to get from point 0 to point x.
#Examples
#input:5
#output:1
#input:12
#output:3

# for problem statement   type codeforces617A in google

distance=int(input("enter the distance :"))
if (distance<5):
    print("the steps required to reach the distance is 1")
elif (distance%5==0):
    print("the steps required to reach the distance is",distance/5)
else:
    print("the steps required to reach the distance is",distance//5+1)