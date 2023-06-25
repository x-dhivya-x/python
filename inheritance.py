class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,rollno,id):
        self.rollno = rollno
        self.id = id
        Person.__init__(self,name,age)
    def stud_info(self):
        print(self.name,self.age,self.rollno,self.id)


obj1=Person("Dhivya",22)
obj2=Student("Hari",25,6105,19)
obj1.display()
obj2.display()
obj2.stud_info()
