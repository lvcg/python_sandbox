# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict 
person = {
    'first_name': 'John'
    'last_name': 'Doe'
    'age': 30
}

print(person, type(person))

# use constructor
#person2 = dict(first_name='Sara', last_name='Williams')
print(person2, type(person2))

# get value
print(person['first_name'])

print(person.get('last_name'))

# add key/value
person['phone'] = '555-555-5555'

print(person)

# get dict keys
print(person.keys())

# get dict items
print(person.items())

# copy dict 
person2 = person.copy()
person2['city'] = 'Nyc'

# remove item 
del(person['age'])

person.pop('phone')

#Clear 
person.clear()

# get length 
print(len(person2))

#list of  dict 
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kyle', 'age': 25}
]

print(people)

