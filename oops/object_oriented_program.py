#example of object oriented program

class Bike:
    def __init__(self,name,cc):
        self.bike_name=name
        self.bike_cc=cc
        
    def sound(self):
        
         if self.bike_cc>370:
            
             print(f"{self.bike_name} is loud")
         else:
            
           print(f"{self.bike_name}is  sounds normal")
        
Duke=Bike("RC390",390)
RE=Bike("classic350",350)

print(Duke.bike_name)
print(RE.bike_name)
Duke.sound()
RE.sound()
print(Duke.bike_cc)