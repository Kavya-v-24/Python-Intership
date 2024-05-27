
# arbitury function 

def multiply(*args):
    result=1
    for num in args:
        result*=num
    return result
print(multiply(2,3,4))

#there are 2 types 
#>>*args(arguments) this is used when we don't no the number of inputs
#>>  **kwargs(keyword arguments)

#the above one is example of *args