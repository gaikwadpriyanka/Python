#Packing and Unpacking for Tuple

# Packing: Combine seperated elements as one entity.

# a=100
# b="Hello"
# c=300
# nums = a,b,c
# print("Packing Elemnts: ",nums)



# # Unpacking: It is process of seperating the individuals object and store it is seperate variable.

# num1,num2,num3= nums
# print("Unpacking the elemnts: ",num1,num2,num3)
 

# #Tuple unpacking with Asterisk(*)
# #Operator is used in tuple unpacking to grab multiple items into list
# # This is just useful to extract just a few specific elements and collect the rest together

# tup1 = (1,2,3,4,5,6,7)
# x,*y,z = tup1
# print("Using * operator- ",x,y,z)

# y,*p =tup1
# print(type(y))
# print(p)
# print(y)




# Packing Unpacking with List:
# a=100
# b="Hello"
# c=300

# ## Packing:
# l = [a,b,c]
# print("List elements after direct packing: ",l)


# num =a,b,c
# l1 = list(num)
# print("List elemnts after packing using typecasing: ",l1)

## Unpacking:

list1 = [500,600,700]
x,y,z = list1
print("Elemnts after unpacking: ",x,y,z)

# Unpacking using * operator using middle 

tup1 = [2,5,6,3,"hi",90,4,5,5]
s,*d,j = tup1
print("Unpacked elements")
print(s)
print(d)
print(j)


# Unpacking using * by last elment:

tup1 = [2,5,6,3,"hi",90,4,5,5]
s,d,*j = tup1
print("Unpacked elements")
print(s)
print(d)
print(j)

# Unpacking using nested:

tup2 = [12,["Hi","Germany"],5445,]
a,(d),e  = tup2
print(a)
print(d)
print(e)

d,*m,y=tup2
print(s)
print(m)
print(y)


# Packing Unpacking with Set:

#UnPacking:

s1 = {2,3,4,5}
a,*b,c,d=s1
print(a)
print(b)
print(c)
print(d)