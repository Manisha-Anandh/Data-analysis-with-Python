#!/usr/bin/env python
# coding: utf-8

# # LIST CREATION AND SOME BASIC OPERATIONS

# BASIC OPERATIONS
# 1. Adding
# 2. Inserting
# 3. Removing
# 4. Modifying
# 5. Accessing
# 6. Sorting
# 7. Reversing elements
# 8. Length of the list
# 9. Maximum value in the list
# 10. Minimum value in the list
# 11. Count of an element
# 12. Clearing the list
# 13. addition
# 14. subtraction
# 15. multiplication
# 16. division

# In[1]:


#List as Lst
Lst = [2,3,4,56,6]
print(Lst)


# In[2]:


#operations on list

Lst.append(2) #adding elements to the end of the list
print('appended element in the list',Lst)

Lst.pop(3) #pops element by index
print('poped element in the list',Lst)

Lst.insert(2,4) #insert element 4 in index 2
print('inserted element in list',Lst)

Lst.extend([12,3]) #extend list by adding elements to the end
print('extended element in list',Lst)

Lst.remove(12) #removes element from the list
print('removed element in list',Lst)

Lst.pop() #removes last element
print('poped last element in list',Lst)

Lst.reverse() #reverse the order of list
print('reversed the order of the list',Lst)

Lst.index(2) #index of the element in list
print('index of element',Lst)

Lst.sort() #arrages list in ascending order
print('sorted list',Lst)

print('slicing the list',Lst[1:4])#slicing

Lst.count(2) #Count of elements
print('count of elements',Lst)

print('length of the list',len(Lst)) #lenght of the list

print('minimum element in the list is',min(Lst)) #minimum value of the list

print('maximum element in the list is',max(Lst)) #maximum value of the list

Lst.clear() #clear elements in the list
print(Lst)

#operations with 2 lists
L1 = [2,3,4,5]
L2 = [3,4,2,5]

print('list addition',L1+L2)


# # DICTIONARY CREATION AND METHODS

# BASIC OPERATIONS
# 1. Creating a dictionary.
# 2. Clearing the dictionary
# 3. Getting all values
# 4. Accessing a value by key
# 5. Accessing by index
# 6. Accessing a key by value
# 7. Updating an existing value
# 8. Removing a key
# 9. Removing a value

# In[3]:


#Dictionary as dict

#clear() method
my_dict = {'1': 'Geeks', '2': 'For', '3': 'Geeks'}
my_dict.clear()
print('Cleared dictionary',my_dict)

#get() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} #gets value of the key
print(d.get('Name'))
print(d.get('Gender'))

#items() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} #access items
print(list(d.items())[1][0])
print(list(d.items())[1][1])

#keys() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} #finds value
print(list(d.keys()))

#values() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'} #finds key
print(list(d.values()))

#update() method
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}

d1.update(d2)
print('updated d1',d1)

#pop() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d.pop('Age')
print('after pop',d)

#popitem() method
d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d.popitem()
print('after popitem',d)


# #  SET CREATION AND SOME BASIC OPERATION

# BASIC OPERATIONS
# 1. Adding
# 2. Removing
# 3. Modifying
# 4. Checking for elements
# 5. Getting the length
# 6. Clearing the set
# 7. Union
# 8. Intersection 
# 9. Difference 
# 

# In[4]:


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Adding multiple elements to the set
my_set.update([7, 8])
print("Set after adding multiple elements:", my_set)

# Removing an element from the set (raises KeyError if the element is not found)
my_set.remove(3)
print("Set after removing the element '3':", my_set)

# Removing an element from the set (does not raise an error if the element is not found)
my_set.discard(4)
print("Set after discarding the element '4':", my_set)

# Modifying elements in the set
# Since sets are unordered and elements cannot be directly modified,
# we will remove an element and add a new one instead.
my_set.discard(5)
my_set.add(10)
print("Set after modifying an element (replacing '5' with '10'):", my_set)

# Checking if an element exists in the set
is_element_in_set = 10 in my_set
print("Is element '10' in the set?", is_element_in_set)

# Checking the length of the set
length_of_set = len(my_set)
print("Length of the set:", length_of_set)

# Subset and Superset
subset_set = {1, 2}
superset_set = {1, 2, 3, 4, 5, 6}
print("Is subset_set a subset of my_set?", subset_set.issubset(my_set))
print("Is my_set a superset of subset_set?", my_set.issuperset(subset_set))

# Disjoint Sets
another_set = {9, 10}
print("Are my_set and another_set disjoint?", my_set.isdisjoint(another_set))

# Adding more elements for further operations
my_set.update({6, 7, 8})
another_set.update({4, 5, 6})

# Set operations

# Union
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# Intersection
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# Difference
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)

# Clearing all elements from the set
my_set.clear()
print("Set after clearing all elements:", my_set)

