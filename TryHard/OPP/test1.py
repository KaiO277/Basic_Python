class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"    

p1 = Person("Nghĩa", 21)

print(p1.name, " ", p1.age)
print(p1)