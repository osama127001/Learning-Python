# almost like the lists but with () brackets


# Tuples declaration
print('\nTuples declaration')
tuple = (1, 2, 3)
anotherTuple = ('hadi', 'osama', 'aamir')
print(max(tuple))
print(tuple[2])
print(anotherTuple)


# iteration
print('\niteration')
for i in tuple:
    print(i)


# Tuples, strings are immutable.
# cant sort a tuple, order remains the same
# it has only 2 methods, count() and index()
# more efficient


# 1 to 1 correspondence
print('\n1 to 1 correspondence')
(x, y) = ('osama', 10)
print(x)
print(y)


# dictionary.items() returns a list of tuples


# Assignment
# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string
# a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Read file
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

# separating hours
words = list()
time = list()
hours = list()
timeSplit = list()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split()
        timeSplit = time[0].split(':')
        hours.append(timeSplit[0])

# making histogram
histogram = dict()
for hour in hours:
    histogram[hour] = histogram.get(hour, 0) + 1

# sorting using tuples
sortedHistogram = list()
for k, v in histogram.items():
    newTuple = (k, v)
    sortedHistogram.append(newTuple)
sortedHistogram = sorted(sortedHistogram)

# Printing histogram
for k, v in sortedHistogram:
    print(k, v)


