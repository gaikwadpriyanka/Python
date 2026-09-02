# 1 Sept 26


# Encapsulation: The process of binding data and methods together and restricting 
# access to some of the object's components.
# It is data hiding
# _ make the attribute protected
#__make the attribute private

"""
class Sample:
    a=100   #public
    _b=200   #protected
    __c=300  #private

# Private variable accesssed only using Name Mangling
s1  = Sample()
print(s1.a)
print(s1._b)
print(s1._Sample__c)


# We can't access private variable directly
# from outside the class, but we can provide public methods to get or set their values.
#  This is a common practice to maintain encapsulation


s1.a = 90
s1._b=80
s1._Sample__c=70

print(s1.a) # it is creating another instance in a memory with new value
print(s1._b)
print(s1._Sample__c) # changing the instace inside class for s1 object 

t1 = Sample()
print(t1.a)
print(t1._b)
print(t1._Sample__c)

# It i create new Object of class Sample and try to access value of varible inside class 
# it will print original value inside the class not changed last value.

"""
"""
class Sample:
    a =100

s=Sample()
s.a=500
print(s.a)  # accessing public attribute using object
print(Sample.a)  # accessing class attribute using class name 

Sample.a = 300
t=Sample()
print(t.a)
"""
"""
class Sample:
    def m1(self):
        print('public')
    def _m2(self):
        print('protected')
    def __m3(self):
        print('private')

s1 = Sample()
s1.m1()
s1._m2()
s1._Sample__m3()
 ------------------------------------------------------------------------------------------
"""

"""
# Overriding: When child class and Parent class contain same method and there is an inheritance
# then method od child override method of Parent

class Sample:
    def m1(self):
        print('Public method')

class Child(Sample):
    def m1(self):
        print('Child class method')
        #super().m1()  # 1st method:- Call the parent class method
        Sample.m1(self)  # 2nd method:- Call the parent class method

c1 = Child()
c1.m1()  # Class the overridden method in child class
------------------------------------------------------------------------------------------
"""

"""
## Multiple Inheritance: When a child class inherits properties and methods from more than
# one parent class, it is called multiple inheritance.

class Father:
    def money(self):
        print('Fathers money')

class Mother:
    def money(self):
        print('Mothers money')
        Father.money(self)   # Call the method from Father class use Class Reference

class Child(Mother,Father):
    pass

c1 = Child()
c1.money()

print(Child.__mro__)  # Displays the method resolution order for the Child class

# Assignemt: Check e.g. of MRO

"""

# Polymorphism: Poly(many) + morphism(Forms) --> Many forms
# operator level polymorphism/Overloading: +,-,*,/,//,%,** etc
# As + opertator is showing different behaviour for different data
# We have 3 different types of Polymorphism:
#1. Operator level polymorphism/Overloading   --possible
#2. Method level polymorphism/Overloading     -- Not possible in python
#3. Constructor level Overloading             -- Not possible in python
