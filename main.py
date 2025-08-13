class Person:
    population=0
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
        Person.population+=1

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    @classmethod
    def get_population(cls):
        return cls.population
    
person1=Person("jack",25)
person2=Person("david",23)

person1.introduce()
print("population:", Person.get_population())

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id=student_id

    def study(self): 
        print(f"{self.name} is studying")
    
    @staticmethod
    def is_adult(age):
     return age >= 18
    
    @classmethod
    def from_string(cls, data_string):
        name, age, student_id = data_string.split(",")
        return cls(name.strip(), int(age), int(student_id))

student1=Student("oliver", 30, 5773)
student1.study() 
student2=Student.from_string("John, 30, 1122")
print(student2)
print(student1.is_adult(16))

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject=subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

teacher1=Teacher("Bin", 40, "python")
teacher1.teach()

    