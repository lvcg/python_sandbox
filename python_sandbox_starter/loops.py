# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Anna', 'Mike']

#simple for loop 
for person in people:
    print(f'Current Person: {person}')

# Break loop 
for person in people:
    if person == 'Anna':
        break 
    print(f'Current Person: {person}')

# Continue
for person in people:
    if person == 'Anna':
        continue
    print(f'Current Person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range (0, 21):
    print(f'Number: {i}')


# While loops execute a set of statements as long as a condition is true.
count = 0 
while count <= 10:
    print(f'Count: {count}')
    count += 1