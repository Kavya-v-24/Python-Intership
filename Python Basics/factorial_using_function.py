#factorial

def factorial(n):
    if n<0:
        return "negative number"
    elif n==0:
        return 1
    else:
        factorial=1
        for i in range(1,n+1):
            factorial*=i
        return(factorial)
result=factorial(0)
print(result)
        
  
#prime number    
        
        
        
        
        
        
        
        
   