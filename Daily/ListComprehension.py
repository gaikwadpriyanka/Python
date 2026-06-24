# List Comprehension: To create a new list in simple and oneliner solution
#syntax: [operation for var in sequence/iteration]
# if condititon is optional

# d = [1,2,4,5,35,45,768,900,3,345]
# # Create new list with sqaured numbers
# [num*num for num in d]

# Write a program to take and any number and print its table

num_user = eval(input('Enter the number: '))
print(type(num_user))
table = [num_user*num for num in range(1,11)]
for var in table:
    print(var)


# Nested list Comprehension
# Work with nested elements

list1 = [[1,2,3,],[4,5,6],[7,8,9]]
#convert nested list into noraml list
#convert nested list to set