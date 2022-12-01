from People.Employee import *

__all__ = ["Supervisor"]

class Supervisor(Employee):
    def __init__(self, id, firstName, lastName, salary, title):
        super().__init__(id, firstName, lastName, salary)  # calling the base class constructor (Employee)
        self.title = title
        
    def __str__(self):
        return f"{self.title:<20} {super().__str__()}"
    
    def header():
        return f"{'Title':<20} {Employee.header()}"
    
    def printGreeting(self):
        print(f"Hello, {self.title} {self.firstName} {self.lastName}.")