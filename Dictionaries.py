# Chapter 9. Dictionaries
# Dictionary is like a set of items with any label without any organization

purse = dict()# Right now, purse is an empty variable of dictionary category
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['money'] = purse['money'] + 8
print(purse)

lst = list()
lst.append(21)
lst.append(3)
print(lst)
print(lst[1])

abc = dict()
abc['age'] = 21
abc['course'] = 146
print(abc)
abc['age'] = 26
print(abc)

# You can make empty dictionary using curly brackets/braces

print('ccc' in abc)

# When we see a new entry, we need to add that new entry in a dictionary, we just simply add 1 in the dictionary under that entry
counts = dict()
names = ['ali', 'asad','ashraf','ali','asad']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

if name in counts:
    x = counts[name]
else:
    counts.get(name, 0)
print(counts)

# Dictionary and Files

counts = dict()
print('Enter a line of text: ')
line = input('')
words = line.split()
print('Words:',words)
print('Counting.........')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts',counts)
# The example above shows how many words are there in a sentence and how many times each word has been repeated in a sentence

length = {'ali': 1, 'andrew': 20, 'jayaram': 32}
for key in length:
    print(key, length[key])
    
print(length.keys())
print(length.values())

for abc,ghi in length.items():
    print(abc,ghi)
    
stuff = dict()
print(stuff.get('candy', -1))