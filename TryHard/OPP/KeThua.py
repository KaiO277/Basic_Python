class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

s1 = Student("Nghia", 21)

print(s1.name," ",s1.age)