print(2+5)
print("2"+"7")

#operator overloadig

#adding two complex numbers

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self,other):
        return f"{self.real+other.real}+{self.imaginary+other.imaginary}i"
    

c1=ComplexNumber(5,9)
c2=ComplexNumber(8,6)

print(c1+c2)