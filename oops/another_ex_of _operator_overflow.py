class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
        
    def __gt__(self,other):  #gt is to perform greater than function
        if self.money>other.money:
            return True
        else:
            return False
        
p1=Party("sanjay",1000)
p2=Party("surya",2000)

if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")