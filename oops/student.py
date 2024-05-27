class Student:
    def __init__(self, name, roll_number, password):
        self.name = name  # public attribute
        self._roll_number = roll_number  # protected attribute
        self.__password = password  # private attribute

    def display_details(self):
        print("name:", self.name)
        print("roll number:", self._roll_number)
        print("password:", self.__password)

    def get_password(self):
        return self.__password

# the above def get_password is to print the private attribute, without calling afunction we can't access the private attributes

    def set_password(self,new_password):
        self.__password=new_password
#the above def function is used to set a new password

#Both get and set comes under encapsulation

student = Student("alice", "A001", "secure_password")
print("name(public):", student.name)
print("roll number(protected):", student._roll_number)
print("password(private):", student.get_password())

#student.display_details() can also be used to print the details instead of so many print statements ,but we will not get the words in braces that are in print statement(i.e public,protected,ect)
student.display_details()
