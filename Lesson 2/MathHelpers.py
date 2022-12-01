__all__ = ['GCD','twoPI','Fraction']

twoPI = 6.283185307179586

def GCD(num1, num2):
    '''
    Determines the Greatest Common Divisor of two numbers
    Args:
        num1(int): First number
        num2(int): Second number
    Returns:
        Greatest common divisor of the two numbers
    '''
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return GCD(num2, num1 % num2)


class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    @property  # decorator for read access to numerator
    def numerator(self):
        return self.__numerator
    
    @numerator.setter
    def numerator(self, value):
        if (value == None) or (type(value) is not int):
            self.__numerator = 0
        else:
            self.__numerator = value
            
    @property  # decorator for read access to denominator
    def denominator(self):
        return self.__denominator
    
    @denominator.setter
    def denominator(self, value):
        if (value == None) or (type(value) is not int):
            self.__denominator = 1
        else:
            if value == 0:
                self.__denominator = 1
            else:
                if value < 0:
                    self.__numerator *= -1  # only apply sign to numerator
                self.__denominator = abs(value)
                
    @numerator.deleter
    def numerator(self):
        # Triggered when 'del(f.numerator)' is called
        self.__numerator = 0  # don't delete, just change to 0

    @denominator.deleter
    def denominator(self):
        self.__denominator = 1  # don't delete, just change to 1
        
    @property  # decorator for read access to value
    def value(self):
        return self.__numerator / self.__denominator
        
    def simplify(self):
        gcd = GCD(abs(self.numerator), self.denominator)
        if gcd > 1:
            self.numerator = int(self.numerator / gcd)
            self.denominator = int(self.denominator / gcd)
            
            
    def __add__(self, other):
        if (other != None) and (type(other) is Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        elif (other != None) and (type(other) is int):
            return self + Fraction(other, 1)
        return self
    
    def __sub__(self, other):
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator * other.denominator)
        elif other != None and type(other) is int:
            return self - Fraction(other, 1)
        return self
     
    def __mul__(self, other):
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif other != None and type(other) is int:
            return self * Fraction(other, 1)
        return self
    
    def __div__(self, other):
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif other != None and type(other) is int:
            return self / Fraction(other, 1)
        return self
    
    def __truediv__(self, other):
        # See: https://stackoverflow.com/questions/7075082/what-is-future-in-python-used-for-and-how-when-to-use-it-and-how-it-works
        if other != None and type(other) is Fraction:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        elif other != None and type(other) is int:
            return self / Fraction(other, 1)
        return self
    
    def __eq__(self, other):
        if other != None and type(other) is Fraction:
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif other != None and type(other) is int:
            return self == Fraction(other, 1)
        return False
    
    def __ne__(self, other):
        return not (self == other)
    
    def __lt__(self, other):
        if other != None and type(other) is Fraction:
            return self.value < other.value
        elif other != None and type(other) is int:
            return self < Fraction(other, 1)
        return False

    def __gt__(self, other):
        # Note: (self > other) == (!(self < other || self == other))
        return not(self < other or self == other)

    def __le__(self, other):
        # Note: (self > other) == (!(self > other))
        return not (self > other)
    
    def __ge__(self, other):
        # Note: (self > other) == (!(self < other))
        return not (self < other)