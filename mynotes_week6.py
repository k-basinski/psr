# Notes

# Remind everybody that assignments have deadlines. Assignment 3 is due today.

# There's no class next week



# Discuss this:
l = list(range(20))
l[::-1][:10]


# List comprehensions are an alternative to for loops

l = [n for n in range(100)]
l

[n*2 for n in range(10)]

l = [n*3-1 for n in range(10, 30)]
k = [n+1 for n in l]
[l[i] + k[i] for i in range(len(l))]

[n for n in range(20)]
[n for n in range(20) if n % 2 == 0]
[n for n in range(20) if n % 2 == 0 if n % 3 == 0]
[n if n%2 == 0 else n/2 for n in range(20)]

# bad mf-cker
matrix = [[i for i in range(10)] for j in range(5)]
matrix

# give me a single item
matrix[3][2]


# tuples

# tuples are like lists but unmutable
t = (1, 4, 5, 7)

# you can make them out of range objects
t = tuple(range(10))
t

# access tuple item the same as a list item
t[1]
t[2]
t[-1]

# slices work
t[:3:-1]

# after they're created, you cannot change them
t[1] = 123

# they're very handy in expressions such as these
(x, y, z) = (1, 2, 3)
x
y
z

# they're also used in function definitions, for loops and many other places




# dicts
a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['apple']

# values can be added like so
a['plum'] = 'fruit'
a

# keys are unique, setting the same key overwrites it
a['cake'] = 'delicious'
a

# of course dict items can be any type
a['banana'] = ['fruit', 'dessert']

# dict constructor
b = dict(apple='fruit', beetroot='vegetable')
b

# look out, doesn't work with spaces
c = dict(sour grape='bad fruit')

# dicts are ordered as of Python 3.7
for e in a:
    print(e)

# you can create a dict by zipping two lists
keys = ['one', 'two', 'three']
vals = [4, 5, 6]
dict(zip(keys, vals))

# access only keys
a.keys()

# make it a list
list(a.keys())

# access only values
a.values()