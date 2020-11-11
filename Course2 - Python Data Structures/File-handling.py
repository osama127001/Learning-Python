# file handle gives us the access to read and write etc, its not the actual data.
fileHandle = open('./short_txt', 'r')
print(fileHandle)


# printing content of file
count = 0
for content in fileHandle:
    print(content)
    count = count + 1


# number of lines in a file
print('No. of lines:', count)


# the second way of doing that
fHand = open('./short_txt', 'r')
fileContent = fHand.read()  # stores the entire file in this variable
print('No of Content:', len(fileContent))


# print first 20 characters
fHand = open('./short_txt', 'r')
fileContent = fHand.read()  # stores the entire file in this variable
print('First 20 characters:', fileContent[:20])


# Searching
# Search lines that starts with 'From: '
fHand2 = open('./short_txt')  # if the second parameter has no value, then it reads.
for line in fHand2:
    if line.startswith('From: '):
        line = line.rstrip()  # this line skips the extra \n added
        print('Search From: ', line)
        print('First 20 characters', line[:20])


# Searching
# Search lines containing '@uct.ac.za'
fileHandle = open('./short_txt')
for line in fileHandle:
    line = line.rstrip()
    if '@uct.ac.za' not in line:
        continue
    print('Search @uct.ac.za:', line)


# Program that reads the file using the name given by the user:
fileName = input('Enter the file name: ')
try:
    fileHandle = open(fileName)
except:
    print('Cannot open file!')
    quit()
for line in fileHandle:
    line = line.rstrip()
    if '@uct.ac.za' not in line:
        continue
    print('Search @uct.ac.za:', line)
