L1=[12,34,56,34,66,33]
key=int(input("enter the number:"))
for i in L1:
    if i==key:
        print("keyword at index",L1.index(key))
    