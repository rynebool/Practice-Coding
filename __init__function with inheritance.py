class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def say_hi(self):
        print("Hello my first name is", self.firstname)

    def say_hi2(self):
        print("Hello my last name is", self.lastname)

    def say_hi3(self):
        print("Hello my fullname is", self.firstname +"",self.lastname)

class Full(Person):
    def __init__(self, fname, lname):
         super().__init__(fname, lname)
         

p1 = Person("Rynelyn", "Bool")
p1.say_hi()
p1.say_hi2()
p1.say_hi3()


