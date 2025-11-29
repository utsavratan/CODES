class Person1:
    def __init__(self, name, age):  
        self.name = name  
        self.age = age
    def introduce(self):  
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")
person1 = Person1("Utsav", 18)  
person1.introduce()