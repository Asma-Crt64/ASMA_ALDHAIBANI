class Person:
    name=""
    age=0
    
    def __init__(self, name, age):  
        self.name = name  
        self.age = age   
    def introduce(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old!.")
        
        
p1=Person("ASMA", 22)

p1.introduce()
