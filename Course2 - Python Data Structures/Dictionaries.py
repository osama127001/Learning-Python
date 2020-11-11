# its just like json
# key value pairs
# baby-database


# Making a new dictionary
# it is just like a key value pair, key is a string and value can be aanything
print('\nMaking a new dictionary')
myDict = dict()
myDict['name'] = 'osama'
myDict['age'] = 22
myDict['graduated'] = True
myDict['courses'] = ['python', 'MEAN Stack']
print(myDict)
print(myDict['courses'])
print('name' in myDict)


# dictionary content is mutable.


# get() function on dictionary
print('\nget() function on dictionary')
age = myDict.get('age', 0)
print(age)
power = myDict.get('power', 0)  # 0 means that return 0 if there is on key named 'power'
print(power)


# iterating through a dictionary
print('\niterating through a dictionary')
for key in myDict:
    print(key, myDict[key])


# converting dictionaries to lists
print('\nconverting dictionaries to lists')
print(list(myDict))
print(myDict.keys())
print(myDict.values())
print(myDict.items())  # tuples


# iterating through dictionary using 2 iteration variables
print('\niterating through dictionary using 2 iteration variables')
for key, value in myDict.items():
    print(key, value)


# Assignment
# Q: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

# Reading file
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# extracting usernames
users = list()
for line in handle:
    if line.startswith('From: '):
        words = line.split()
        users.append(words[1])

# Creating Histogram
histogram = dict()
for user in users:
    histogram[user] = histogram.get(user, 0) + 1

# Extracting username with maximum number of emails
bigUser = None
bigCount = None
for word, count in histogram.items():
    if bigCount is None or count > bigCount:
        bigUser = word
        bigCount = count

# result
print(bigUser, bigCount)


