# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Liv'
age = 41

# Concatenate
#print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
#print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings
#print(f'Hello, my name is {name} and I am {age}')

# String Methods
 s = 'hello world'

 # Capitalize string
 print(s.capitalize())

 # make all uppercase
 print(s.upper())

 # make lowercase
 print(s.lower())

 # swap case
 print(s.swapcase())

 # get length
 print(len(s))

 # replace
 print(s.replace('world', 'everyone'))

 # count
 sub = 'h'
 print(s.count(sub))

 # starts with
 print(s.startswith('hello'))

 #ends with
 print(s.endwith('d'))

 #split into a list 
 print(s.split())

 # find position
 print(s.find('r'))

 # is all alphanumeric
 print(s.isalnum())

 # is all alphabetic
 print(s.isalpha())

 #is all numeric
 print(s.isnumeric())
