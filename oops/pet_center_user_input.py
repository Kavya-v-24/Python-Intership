class Pet_center:
    def __init__(self,name="",features="",breed=""):
        self.pet_name=name
        self.pet_features=features
        self.pet_breed=breed
        
    def details(self):
        self.pet_name=input()
        if (self.pet_name=="dog"):
            print("pet_name:Dog \nfeatures:mammal with sharp teeth ,friendly ,good sense of smell \nbreed:lab \ncost:45,000 ")
        elif(self.pet_name=="cat"):
            print("pet_name:cat \nfeartures:strong, sharp teeth, night vision, flexible body\nbreed:street cat \ncost:10,000")
        elif(self.pet_name=="birds"):
            print("pet_name:parrot \nfeatures:fly ,high metabolic rate\ncost:2,500")
        elif(self.pet_name=="fish"):
            print("pet_name:golden fish\ncost:500 per each fish ")
        else:
            print("we don't have that pet")
            
            

x=Pet_center()
x.details()
        