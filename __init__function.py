class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def say_hi(self):
        print("Hello my name is", self.firstname, self.lastname)

p1 = Person("Rynelyn", "Bool")
p1.say_hi()