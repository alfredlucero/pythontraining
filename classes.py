from abc import ABCMeta, abstractmethod


class Employee:
    name = "Alfred"
    role = "Software Engineer"
    num_years_experience = 3

    # instance methods using self
    def get_years_experience(self):
        return self.num_years_experience

    def set_years_experience(self, years):
        self.num_years_experience = years

    # static methods that don't use self
    @staticmethod
    def welcomeMessage():
        print("Welcome to the team!")


employee = Employee()
print("Years experience", employee.get_years_experience())
print(employee.num_years_experience)

# Class attribute
Employee.name = "gingin"
employeeTwo = Employee()
print(employee.name == employeeTwo.name)

# Instance attribute re-assigned
employee.name = "pedong"
employeeTwo.name = "ginie"
print(employee.name != employeeTwo.name)

# Checks instance attribute and then class attribute whenever we do class.attribute

# employee.get_years_experience() => Employee.get_years_experience(employee)
# => that's why we have self passed in
employee.set_years_experience(5)
print(employee.get_years_experience())

employee.welcomeMessage()

# Base Class


class Animal:
    # Initialize/constructor
    def __init__(self, name):
        self.name = name


cat = Animal("cat")
print(cat.name)

# Inheritance
# can also do multiple inheritance, order matters if there are same name attributes in base classes
# diamond shape problem with multiple inheritance and order of derived class matters for conflicting method names


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("juno", "corgi")
print(dog.name)
print(dog.breed)

# Public => member_name
# Protected => _member_name
# Private => __member_name

# Overloading operator


class Square:
    def __init__(self, side):
        self.side = side

    def __add__(squareOne, squareTwo):
        return((4 * squareOne.side) + (4 * squareTwo.side))


squareOne = Square(5)
squareTwo = Square(10)

print(squareOne + squareTwo)

# Abstract base class


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0


class NewSquare(Shape):
    side = 4

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    width = 5
    length = 10

    def area(self):
        return self.width * self.length
