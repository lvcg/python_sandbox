# Python has functions for creating, reading, updating, and deleting files.

# open file 
myFile = open('myfile.txt', 'w')

#get info 
print('Name: ', myFile,name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#write to file 
myFile.write('I love python')
myFile.close()

# append to file 

myFile = open('myfile.txt', 'a')

# read file 
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)

