from People.Person import *

__all__ = ["Employee"]

class Employee(Person):
    def __init__(self, id, firstName, lastName, salary):
        super().__init__(id, firstName, lastName) # call base class init (constructor)
        self.salary = salary  # only have to directly set salary here
        
    def __str__(self):  
        #return f"{self.id:<9} {self.lastName:<15} {self.firstName:<15} ${self.salary:>12,.2f}"
        return f"{super().__str__()} ${self.salary:>12,.2f}"
    
    def header():
        return f"{Person.header()}  {'Salary':>12}"