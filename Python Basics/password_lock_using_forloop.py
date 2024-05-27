try:
    while True:

       attempts=3
       for attempts in range(1,4):
         user_input=input()
    
         if (user_input=="kavya"):
          print("enter password")
          break
          
         else:
           print("try again")
         attempts-=1
         print(" account locked")
       print("lock opened")
except KeyboardInterrupt:
    print("Interrupted by user")