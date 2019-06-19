# CHAPTER 6
# String Index Operator
fruit = 'orange'
letter = fruit[2]
print(letter)

w = 4
x = fruit[w - 1]
print(x)
y = len(fruit)
print(y) # len() is a length function, it tells the letter count of a word

# Looping through strings
fruit = 'orange'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index,letter)
    index = index + 1
# Line 13-18 shows the counting of letters through a while loop of any particular word

# Now we will loop the word orange through definite for loop
fruit = 'orange'
for letter in fruit:
    print(letter)
    
# Looping and Counting
word = 'apple'
count = 0
for letter in word:
    if letter == 'p':
        count = count + 1
print(count)

# Slicing Strings
s = 'Monty Python'
print(s[0:5])
print(s[6:12])
print(s[:5])
print(s[6:]) 

# String comparison
if word == 'banana':
    print('All right, bananas.')
if word < 'banana':
    print('Your word, '+word+ ' , comes before banana')
elif word > 'banana':
    print('Your word, '+word+ ' , comes after banana')
else:
    print('All right, bananas.')

# String  Library
greet = 'Hello Ali'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())

print(type(greet))
print(dir(greet))

# Searching for a String
fruit = 'orange'
pos = fruit.find('ng')
print(pos)
ab = fruit.find('o')
print(ab)
cc = fruit.find('s')
print(cc)

# Replacing a String
greet = 'Hello Ali'
rpc = greet.replace('Ali', 'Agatha')
print(rpc)
lpc = rpc.replace('a', 'r')
print(lpc)

#Stripping whitespace
greet = '        Hello Ali      '
print(greet.lstrip())#lstrip() removes the whitespace at the left corner
print(greet.rstrip())#rstrip() removes the whitespace at the right corner
print(greet.strip())#strip() removes the white spaces from both ends

# Prefixes
line = 'Have a wonderful day'
print(line.startswith('Have'))
print(line.startswith('a')) # First word would always be true for prefixes

# Parsing and Extracting
data = 'From asadali08@gmail.com  Retrieved on June 17, 2019'
detect = data.find('@')
print(detect)
locate = data.find(' ',detect)
print(locate)
host = print(data[detect + 1 : locate])
# Search for something and pull that thing out is the basic rule for parsing and extracting