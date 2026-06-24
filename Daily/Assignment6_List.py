# # Create an empty list

l = []

# # Add element in list in normal way
# '''a[0]=1
# a[1] = 2 it throw error index realated
# '''

# l.append(2)
# print(l)

# Add try to str,list, tuple ,set,dict

s = 'Hello World'
list_a = [2,3,4,'Hi',889,32244]
tuple_b=(29,56,45,78)
set_c={8,4,5,6,0,33,45}
Dict_d = {"1":"Germany","2":'Munich',"3":"Feriham"}


# Add object in the list as it is
#1.list_a.append(s) will add whole string  as single elment in list
# list_a.append(s)
# print(list_a)
# list_a.append(tuple_b)
# print(list_a)
# list_a.append(set_c)
# print(list_a)
# list_a.append(Dict_d)
# print(list_a)


#2. list_a.extend(s) will add each charachter from string as a single elemnt in list
list_a.extend(s)
list_a.extend(tuple_b)
list_a.extend(set_c)

print('Output Extent method',list_a)

# for dictionary we ahve follow some rule
# first bind the dict inside the list using extend method
# e.g list_a.extend([Dict_d])
# Result: It will add Dict as list in list as single elemnt with key and value


#############################

# l.append(s)
# print(l[0])
# l[1]= list_a
# print(l)




