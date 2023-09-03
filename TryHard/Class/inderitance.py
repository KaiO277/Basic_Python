class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)    
        self.gra = year

x = Student("kaio", 21, 2023)
print(x.gra)            