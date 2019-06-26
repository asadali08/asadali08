# A list is a kind of a collection
# Collection allows us to put many values in a single variable

friends = ['Ali','Dharam','Hasib']
CarryOn = ['socks','shirt','pants','shoes']
print(friends[0])
fruit = 'Orange'
print(fruit[5])
x = fruit.lower()
print(x)
y = print(fruit.upper())
friends[2] = 'Nathaniel' # This is the specific example of mutable lists
print(friends)
print(len(friends))
print(range(3))
print(range(len(friends)))
for i in range(len(friends)):
    friend = friends[i]
    print('Happy Holiday',friend)# Line 17 - 19 is an example of a counted loop
    
t = [1,3,5,6,7,14,25]
print(t[1:5])
print(t[:3])
print(t[4:])
print(t[:])

# Building a list from scratch
thing = list() # Let's start from an empty list
thing.append('book')
thing.append(100)
print(thing)
thing.append('browine')
print(thing)

print(7 in t)
print(20 in t)
print(20 not in t)

friends.sort() #Sort function organizes the list in an ascending order
print(friends)

total = 0
count = 0
while True:
    inp = input('Enter your number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
    
avg = total/count
print('The average is',avg)

numList = list()
while True:
    ent = input('Enter your number: ')
    if ent == 'ok':
        break
    val = float(ent)
    numList.append(val)
    
average = sum(numList)/len(numList)
print(average)

abc = 'I me myself'
ghi = print(len(abc))
stuff = abc.split()# Function split creates a list out an assigned string
print(stuff)
print(len(stuff))

# Strings and Lists are sort of best friends

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order. 
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst.sort(fh)
for line in fh:
    words = line.rstrip().split()
    for element in words:
        if element in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)

