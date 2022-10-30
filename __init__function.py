class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def say_hi(self):
        print("Hello my name is", self.firstname, self.lastname)

p1 = Person("Rynelyn", "Bool")
p2 = Person("Michael", "Reyes")
p3 = Person("Stephanie","Andal")
p1.say_hi()
p2.say_hi()
p3.say_hi()