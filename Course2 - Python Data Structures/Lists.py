# Lists
print('\nLists')
print([1, 2, 3])
print([1, [1, 2], 3])
print(['hadi', 'osama'])


# Looping in lists
print('\nLooping in lists')
myList = [1, 2, 4]
for i in myList:
    print(10*i)


# Strings are immutable, cannot change 'osama' to 'Osama' by name[0]='O'
# Lists are mutable


# range() function
print('\nrange() function')
print(range(4))


# test code, (We have access to i as compared to 'for x in y' way)
print('\ntest code, (We have access to i as compared to |for x in y| way)')
myList = [1, 2, 3]
for i in range(len(myList)):
    print(i, myList[i])


# Concatenation of Lists
print('\nConcatenation of Lists')
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)


# Slicing
print('\nSlicing')
print(list3[1:3])
print(list3[:4])
print(list3[3:])
print(list3[:])


# Making a new list
print('\nMaking a new list')
newList = list()
print(newList)
newList.append(1)
newList.append('test')
newList.append(5)
print(newList)


# Searching list
print('\nSearching list')
print(5 in newList)
print(8 in newList)
print('test' not in newList)

# Sorting
print('\nSorting')
names = ['osama', 'aamir', 'hadi']
names.sort()
print(names)

# Splitting strings into lists
print('\nSplitting strings into lists')
sentence = 'my name is osama khan'
splitSentence = sentence.split()
print(splitSentence)
sentence = 'my;name;is;osama;khan'
splitSentence = sentence.split(';')
print(splitSentence)


# Assignment 1
# Q: Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
# the split() method. The program should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list. When the program completes, sort and print the
# resulting words in alphabetical order.
fName = input("Enter file name: ")
fh = open(fName)
lst = list()
arr = list()
for line in fh:
    if not arr:
        arr = line.split()
    else:
        tempArr = line.split()
        for word in tempArr:
            if word not in arr: arr.append(word)
        arr.sort()
print(arr)


# Assignment 2
# Q: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the
# following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the
# line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the
# sample output to see how to print the count.
fName = input("Enter file name: ")
if len(fName) < 1:
    fName = "mbox-short.txt"

fh = open(fName)
count = 0

arr = list()
for line in fh:
    if line.startswith("From "):
        count = count + 1
        arr = line.split()
        print(arr[1])

print("There were", count, "lines in the file with From as the first word")

