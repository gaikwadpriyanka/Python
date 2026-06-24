# DICT IS SET OF ELEMENT WITH FORMATE OF KEY VALUE.
#Syntax:{key:value}

#How to create dict
# 1. Empty dict
d = {}
print(d)
print(type(d))

d1 = {1:455,2:'asd',3:343,4:'tyu',5:"Hello"}
print(d1)

# 2. Using built-in functions to create dict
d2 = dict({1:100,2:'rtrt',3:6777,'name':'Garry','age':34})
print(type(d2)) 

############################################################################

#* Methods Of Dict

# # 1.update() : It will add/update the elments in dict
# d1.update({6:878})  # added new key value directly
# print("Print the updated dict: ",d1)

# # update() dict with dict
# d1.update(d2)
# #print('Dictionary after updating dictionary: ',d1)

# #Updating value of existing key
# d1.update({5:'Bye'})
# print(d1)


## 2. setDefault(): It works with key which is not there in the dictionary.If the key is there it 
#                    will not perform any operation

d1.setdefault(6)
print(d1)

d1.setdefault(1)
print(d1)

###################
#Methods to access the dictionary elements

# 1. key- it will give you keys from dict
k =d1.keys()
print("Keys of dict of key method: ",k)


# 2. values- It will give you all the values from dict

v = d1.values()
print("Values from dict: ",v)


# 3. get(): This will return value of specified key

g = d2.get("name")
print("Print the value for key: ",g)


# 4. item(): It return all elements in tuple  formate,each tuple represents key:value pair

item = d1.items()
print("Elements is in Tuple formate: ",item)

### methods to delete the elements from dictionary

# 1. pop(): It will delete key entry from dictionary. Key as parameter required

p = d1.pop(4)
print('Deleted key value: ',p)

# 2. popitem(): It will remove last inserted from dictionary or last entry from dict

popi = d1.popitem()
print("Last entry will deleted from dict: ",popi)

