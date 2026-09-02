## 27 Aug 26


"""
#docstring  used for multiline comments
------------------------------------------------------------
class is a tempalte, blueprint, structure useed for creating an object

class Car:
    #properties
    door =4
    engine=1
    e_name='turbo'

    # behavior-operations
    def drive(self):
        print('Drive the car')

    def drift(self):
        print('Drift the car')

bmw = Car()
print(bmw.e_name)
bmw.drive()
"""

"""
# Objects: It is entity which is physiclly present in memory.Its an instance of class.
"""

# class Human:
#     eyes=2
#     head=1
#     hands=2

#     def walk(self):
#         print('walking')

# we car create n number of objects
# Jhon =Human()
# print(Jhon.eyes,Jhon.head)
# Jhon.walk()

# ravan = Human()
# ravan.head=10
# print('Head:',ravan.head)

# self: It is a reference variable which refers to current object of class. 
# It is used to access the properties and methods of class.

class Human:
    eyes=2
    head=1
    hands=2

    def sample(self):
        print('Hello this is me')
        
    
    def info(self):
        print('Eyes:',self.eyes)
        print('Head:',self.head)
        print('Hands:',self.hands)
        # call sample inside info
        self.sample()

h1= Human()
h1.info()
#h1.sample()

class Test:
    def __init__(self):
        print('Constructor calling....')
t1 = Test()
t2 = Test()

"""
"""

"""
Q. What is Constructor?
- Constructor is nothing but a class calling
- It is used to allocate a memory- to create an object
- In OOP when we call a constructor then it calls __init__() method
# __init__ is a magic method which is also called as
# dunder method --> double underscore in prefix and suffix

"""