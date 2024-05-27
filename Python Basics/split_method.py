#split the input/srtings

user_list=input("Enter the  elements with space:").split( " ")
print("user list:",user_list)

#we can split only strings but not integers
#for ex:  int(input()).split(" ") will through an error
#we can add coma(,) or space(" ") in split