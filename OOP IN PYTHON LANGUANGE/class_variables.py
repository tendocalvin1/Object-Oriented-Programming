# class_variables = Shared among all instances of a class
#                   Defined outside the class
#                   Allow you to share data among all objects created from that class.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1 = Student("Spongebob", 30)
student2 = Student("Patrick",35)
       
        