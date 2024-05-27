attempts=3
while attempts>0:
    user_input=input()
    
    if (user_input=="kavya"):
        print("enter password")
        
    else:
        print("try again")
    attempts-=1
print(" account locked")