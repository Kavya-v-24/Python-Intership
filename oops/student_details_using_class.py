class Student_details:
    def __init__(self,name="",rollno="",marks="",result=""):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        self.result=result
        
    def status(self):
        if self.marks>="marks:35":
            print(" pass")
        else:
            print(" fail")

student1=Student_details("name:kavya ","\nrollno:1\n","marks:95","\nresult:90%")
student2=Student_details("name:sita","\nrollno:2\n","marks:87","\nresult:83%")  
#if we write code with \n we get the each detail in new line
student3=Student_details("name:siva","rollno:7","marks:56","result:45%")
student4=Student_details("name:vijaya","rollno:9","marks:23","result:20%")
student5=Student_details("name:riva","rollno:15","marks:92","result:90%")    
#if we don't write \n we get in same line with space for each detail

enter=input("enter the student no.:")
if enter=="student1":
    print(student1.name,student1.rollno,student1.marks,student1.result)
    student1.status() 
elif enter=="student2":
    print(student2.name,student2.rollno,student2.marks,student2.result)
    student2.status()
elif enter=="student3":
    print(student3.name,student3.rollno,student3.marks,student3.result)
    student3.status()
elif enter=="student4":
    print(student4.name,student4.rollno,student4.marks,student4.result)
    student4.status() 
elif enter=="student5":
    print(student5.name,student5.rollno,student5.marks,student5.result)
    student5.status()
else:
    print("not found")
    
