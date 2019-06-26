# TUPLES
#Tuples are the limited but efficient versions of the lists
#They are another kind of sequences but they start with parenthesis
from builtins import sorted

x = ('Asad','Ashraf','Ali')
print(x[2])
y = (1,13,-1)
print(y)
print(max(y) - min(y))
for iter in y:
    print(iter)
#Tuples are immutable, meaning that they cannot be altered

a = list()
print(dir(a))
# Programmers cannot alter tuples easily because they are efficient compared to lists
z = tuple()
print(dir(z))

(x,y) = (2,'ok')
print(x)
print(y)

#The items method would return a list of tuple shown below
d = dict()
d['jacek'] = 3
d['nate'] = 10
for k,v in d.items():
    print(k,v)
# Now
tups = d.items()
print(tups)
#Tups would give the key and the value as an output shown above

# Tuples are comparable
s = (0,2,3) < (1,2000,3)
print(s)
t = ('Ali','Jackson') < ('Ali','Harrison')
print(t)

# Tuples can be a major factor if a programmer wants to obtain a sorted version of a dictionary
# It also sorts keys and values
e = {'a':10, 'c':1, 'b':22}
print(e.items())
f = sorted(e.items())
print(f)

tmp = list()
for k,v in e.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp,reverse=True)
print(tmp)

print(sorted([(v,k) for k,v in e.items()]))

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)