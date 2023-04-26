# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
 # create tuple 
 fruits = ('Apples', 'Oranges', 'Grapes')
 fruits2 = tuple (('Apples', 'Oranges', 'Grapes'))

 print(fruits, fruits2)

# Single value needs trailing comma 
fruits2 = ('Apples',)

# get value
print(fruits[1])

# delete tuple
del fruits

print(fruits2)

# get length
print(len(fruits))





# A Set is a collection which is unordered and unindexed. No duplicate members.

# create set
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

print(fruits_set)

# Remove from set 
fruits_set.remove('Grape')

print(fruits_set)

# Clear set 
fruits_set.clear()

# delete
del fruits_set