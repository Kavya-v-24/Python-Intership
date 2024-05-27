class Pet_center:
    def __init__(self,name,features,legs):
        self.pet_name=name
        self.pet_features=features
        self.pet_legs=legs
        
    def sound(self):
        if(self.pet_name=="Dog"):
            print(f"{self.pet_name} barks")
        elif(self.pet_name=="cat"):
            print(f"{self.pet_name} sounds meow")
        else:
            print(f"{self.pet_name} don't no sound")
            
    def category(self):
        if(self.pet_legs==4 or self.pet_legs==2 ):
            
          
            print(f"{self.pet_name} walks")
       
        else:
            print(f"{self.pet_name} swims")
            
            
Dog=Pet_center("Dog","\nmammal with sharp teeth \nfriendly \ngood sense of smell",4)
cat=Pet_center("cat","\nstrong \nsharp teeth \nnight vision \nflexible body",4)
fish=Pet_center("Fish","\nbreath with gills",0)
birds=Pet_center("parrot","fly ",2)

print(Dog.pet_name,Dog.pet_features)
Dog.sound()
cat.sound()
birds.sound()
Dog.category()
birds.category()
fish.category()   
     
        
    