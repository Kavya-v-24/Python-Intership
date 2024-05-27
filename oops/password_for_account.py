class User:
    def __init__(self,username,password="12345678"):
        self._username=username
        self.__password=password
    def check_password(self,password):
        return self.__password==password
    def change_password(self,new_password):
        self.__password=new_password
        print("password changed sucessfully")
    def get_username(self):
        return self._username
username=input("enter your name:")
user=User(username)   
password=input("enter password:")
if user.check_password(password):
    print("welcome,{}!".format(user.get_username()))
else:
    print("password incorrect")
    change_option=input("do you want to change your password?(yes/no):").lower()
    if change_option=="yes":
        new_password=input("enter your new password")
        user.change_password(new_password)
    else:
        print("thank you")