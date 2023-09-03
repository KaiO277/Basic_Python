class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name, self.age}"
    
    def my_func(kai):
        print("Hi "+kai.name)

x = Person("nghia", 21)

print(x)
print(x.my_func())


