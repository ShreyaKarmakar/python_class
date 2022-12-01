__all__ = ['Person']

class Person(object):
    personCount = 0 
        
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        Person.personCount += 1   # Note: must use the "Person." handle
    
    def printGreeting(self):
        print(f"Hello, {self.firstName} {self.lastName}.")
        
    def __str__(self): 
        return f"{self.id:<9} {self.lastName:<15} {self.firstName:<15}"
    
    def header():
        return f"{'ID':<9} {'Last Name':<15} {'First Name':<15}"