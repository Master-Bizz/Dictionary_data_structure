set = set()
print(type(set))
set = {12,212,2}
set.discard(12)
print(set)
set.update({21,23})
print(set)
print(set.pop)
set.update(["January"])
a = {23,23,3}
b = {23,4,23}
print(a.union(b))
print(a & b)
print(a - b)
print(a | b)
# ==================================================================
# Dict items are key value pairs enclosed in curly brackets
# Dict is ordered as of python 3.7
# Dict is mutable
# Dict keys are unique, cannot have duplicates
# Elements can be of different data types

'''
Dict Attributes
'''
print(dir(dict))
print(help(dict.pop))
print(help(dict.values))
print(help(dict.get))
'''
Creating Python Dictionary
'''
dict_example = {}
dict_example1 = {'name':'William', 'age':23} # Key then Value = Key Value Pair
dict_example2 = [(1, 'car', 2, 'skates')]
dict_example3 = dict([(1, 'car'),( 2, 'skates')])
print(dict_example1)
print(dict_example2)
print(dict_example3)
print('List converted to Dictionary for example 3')

'''
Access Dictionary Values
'''
student = {'name':'William', 'age':23}
print(student['name'])
print(student['age'])
print(student.get('age'))
print(student.keys())
print(student.values())
print(student.items())
print(student.__str__())

students = [{'name':'William', 'age':23}, {'name':'Hayley', 'age':28}]
print(students[1])
print(students[1]['age'])
for i in range(len(students)):
    print (students[i] ['name'])

'''
Changing Dictionary elements
'''
student3 = {'name':'Pam', 'age':23}
print(student3)
student3["age"] = 32
print(student3)
student3.update({'name': 'June', 'age':34})
print(student3)

student3 = {'name': 'June', 'age':34}
student3.setdefault('name', 'James')
student3.setdefault('subject', 'python')
student3.setdefault('subject', 'moose')
print(student3)

'''
Remove Element From Dictionary
'''
student4 = {'name':'tiam', 'age':29}
student4.pop('age')
print(student4)
student4.update({'name': 'matey', 'age':52})
student4.popitem()
print(student4)

student4.clear()
print(student4)

# del student also works

'''
Dictionary Membership Test
'''
student = {'name':'William', 'age':23}
print('age' in student)
print('ages' in student)
print('ages' not in student)
print('cheese' not in student)
print('name' not in student)



# clear()	      - Remove all items from dictionary
# copy()	      - Returns a shallow copy of dictionary
# fromkeys()	  - Returns a dictionary with the specified keys and value
# get()	        - Returns the value of the specified key
# items()	      - Returns a list containing a tuple for each key value pair
# keys()	      - Returns a list containing the dictionary's keys
# pop()	        - Removes the element with the specified key
# popitem()	    - Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    - Updates the dictionary with the specified key-value pairs
# values()	    - Returns a list of all the values in the dictionary