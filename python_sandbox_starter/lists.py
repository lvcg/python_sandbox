# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# use a constructor 
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# get a value
print(fruits[1])

# get length
print(len(fruits))

# append to list 
fruits.append('Mangos')

print(fruits)

# remove from list 
fruits.remove('Grapes')

print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

print(fruits)

# Remove with pop
fruits.pop(2)

# Reverse list 
fruits.reverse()

# Sort list 
fruits.sort()

# Reverse sort 
fruits.sort(reverse=True)

# Change value
fruits[0] = 'Blueberries'