# # 1.add(value): It si used to add element

# s1 = set()             # Create empty set

# s = {1,3,5,6,8,"qwe",2,2,2,'rtt',8,9,9,}
# s.add(1)
# s.add('ert')
# s.add(12)
# print(s)


# # 2. Update(value): It is uded to add update element.
# #  This method need to itertable object as arguments

# print(s)
# l  = [1,2,3,4,5]
# s.update(l)
# print("After add list in set", s)

# 3. Discard(): To remove specific element from the set. This method does not return removed element from set to display also

# set3 = {3,4,6,8,9,11,2,3,4,5,6,6,78}
# set3.discard(4)
# print(set3)

# 4. POP(): It remove random elements from set. It will return deleted element.
# set2 = {3,4,5,5,'w34',4,999.32435,4556,88,12,6}
# s =set2.pop()
# print(s)
# print("Set after deleting element",set2)

# 5. Remove(): This method used to delete element from set.It doest not return delted element from set

set3 = {6576.2,6,7,9,0,12}
print(id(set3))
# g = set3.remove(7)
# print(g)
# print(set3)

# 6. copy(): It is used to copy of set.
set4 = {4,5,2,3,3,7,8,9,0}
print(id(set4))
set4 = set3.copy()
print(set4)
print(id(set4))