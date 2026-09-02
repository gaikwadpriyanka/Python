## 31 Sept 26


"""
With __init__ method we can create constructor in python. 
Constructor is a special method which is called when an object of class is created. 
It is used to initialize the data members of class.
It is called automatically when an object of class is created.


class Bank:
    def __init__(self,name,ifsc,place):
        #print('Constructor metthod called')
        print('Bank Details:',name,ifsc,place)


#Bank()  #  Here we are calling constructor of class Bank.
b1 =Bank('SBI','SBI89898','Pune')
"""

"""
class Bank:
    def credit(self,amt,balance=0):
        # to access updated balance in other method make it as debit
        self.balance = balance
        print('Balnce in Credit Rs. ',self.balance)
        print(' Amt Credited Rs:',amt)
        self.balance +=amt

    def debit(self,amt,balance=0):
        print('Intial amount Rs: ',self.balance)
        self.balance -=amt    # deduction from main balance
        print('Amount after deduction of Rs: ',amt,'is Rs: ',self.balance)
        

b1 = Bank()
#b1.credit(1000,500)
b1.credit(3000,1000)
b1.debit(1500,1000)
b1.credit(1000)
"""

# Pillars of OOps:
# 1.Inheritance
# 2.Encapsulation 
# 3.Polymorphism

# Inheritance: It is a process of acquiring properties and methods of parent class into child class.
"""
class RBI:         # parent class
    headqurter = 'Mumbai'
    def rules(self):
        print('RBI Rules')

class SBI(RBI):      # child class 
    def policies(self):
        print('SBI Policies')


s1 = SBI()
s1.policies()
s1.rules()
print(s1.headqurter)  # we can access variable of parent class in child class

"""

# Types of Inheritance:
#1. Simple
#2. Multiple
#3. Multilevel
#4. Hierarchical
#5. Hybrid

#Iq. Difference between multiple and multilevel inheritance?


#1 Multiple Inheritance: When a child class inherits properties and methods from more than
#  one parent class, it is called multiple inheritance.
"""
class Grandpa:
    def bike(self):
        print('Grandpa bike')

class Father(Grandpa):
    def car(self):
        print('Fathers car')

class Mother(Father):
    def money(self):
        print('Mothers money')

class child(Mother):
    pass

c1 = child()
c1.money()
c1.car()
c1.bike()  
            """

class Grandpa:
    def bike(self):
        print('Grandpa bike')
    def money(self):
        print('Grandpa money')    

class Father(Grandpa):
    def car(self):
        print('Fathers car')

    def money(self):
        print('Fathers money')

class Mother(Father):
    def money(self):
        print('Mothers money')
        super().money()          # calling money method of parent(father) 

class child(Mother):
    pass

c1 = child()
c1.money()
