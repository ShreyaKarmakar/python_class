from People.Person import *

__all__ = ["Student"]

class Student(Person):
    def __init__(self, id, firstName, lastName, gpa):
        super().__init__(id, firstName, lastName)  # calling the base class constructor
        self.gpa = gpa
        
    def __str__(self):
        return f"{super().__str__()} {self.gpa:>7,.3f}"
    
    def header():
        return f"{Person.header()} {'GPA':>7}"