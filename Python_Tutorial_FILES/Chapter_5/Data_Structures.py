#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Data-Structures.py
"""DOCstring for Data_Structures.py.

2nd line of DOCstring
"""

from platform import python_version
from sys import hexversion
from collections import deque
from math import pi

print("The Python Version is:", python_version(), " #" + str((hexversion)))
print("\nData Structures\n")

string = "string"
integer = 1
tpl = (1, 2)
lst = []
dic = {}
set_ = set()

integers = [0, 1, 2, 3, 0, 1, 0, 0, 1, 4]
stack = [3, 4, 5]
queue = [5, 4, 3, 2, 1, 0]


def dir_list(s, x):
    """Docstring."""
    print("*****", s.swapcase(), "Methods are:")
    print("-" * 80)
    for i in dir(x):
        if not i.startswith("_"):
            if i == dir(x)[-1]:
                print("", i, end="\n\n\n")
            else:
                print("", i, end=",  ")


def list_out(s, l):
    """Doctstring."""
    if len(l) == 0:
        print("There is no DATA.")
    else:
        listed = []
        for i in l:
            if i not in listed:
                print(s + ".count(", i, ")= ", l.count(i))
                listed.append(i)


dir_list('list', lst)

integers_copy = integers.copy()
print(type(integers_copy), "integers_copy= ", integers_copy)
integers_copy.reverse()
print(type(integers_copy), "integers_copy.reverse()= ", integers_copy)
integers_copy.sort()
print(type(integers_copy), "integers_copy.sort()= ", integers_copy)
integers_copy.sort(reverse=True)
print(type(integers_copy), "integers_copy.sort(reverse=True)= ", integers_copy)

print("Shallow copy integers = ", integers_copy)
print("Original integers still = ", integers)

print("Shallow copy integers.index(4) = ", integers_copy.index(4))
print("Original integers.index(4) = ", integers.index(4))
list_out("integers_copy", integers_copy)

integers_copy.insert(len(integers_copy), 42)
print("Shallow copy integers.insert(len(integers_copy), 42) = ",
      integers_copy)

integers_copy.insert(len(integers_copy), 47)
print("Shallow copy integers.insert(len(integers_copy), 47) = ",
      integers_copy)
list_out("integers_copy", integers_copy)

integers_copy.pop()
print("Shallow copy integers.pop() = ", integers_copy)
list_out("integers_copy", integers_copy)

integers_copy.remove(42)
print("Shallow copy integers.remove(42) = ", integers_copy)
list_out("integers_copy", integers_copy)

integers_copy.extend([56, 57])
print("Shallow copy integers.extend([56, 57]) = ", integers_copy)
list_out("integers_copy", integers_copy)

integers_copy.clear()
print("Shallow copy integers.clear() = ", integers_copy)
list_out("integers_copy", integers_copy)

print("\nstack = ", stack)
list_out("stack", stack)

stack.append(6)
stack.append(7)

print("\nstack = ", stack)
print("stack.pop()", stack.pop())
print("stack = ", stack)
print("stack.pop()", stack.pop())
print("stack = ", stack)
print("stack.pop()", stack.pop())
print("stack = ", stack)
print("stack.pop()", stack.pop())
print("stack = ", stack)
print("stack.pop()", stack.pop())
print("stack = ", stack)

try:
    print("\ntrying stack.pop() on an empty list.")
    print("stack.pop()", stack.pop())
    print("stack = ", stack)
except IndexError:
    print("""
            Traceback (most recent call last):
                File "./Data_Structures.py", line 123, in <module>
                    print("stack.pop()", stack.pop())
            IndexError: pop from empty list \n\n""")

print("queue = ", queue)
print("queue.insert(0, 6)", queue.insert(0, 6))
print("queue.insert(0, 7)", queue.insert(0, 7))
print("queue.insert(0, 8)", queue.insert(0, 8))
print("queue.insert(0, 9)", queue.insert(0, 9))
print("queue.insert(0, 10)", queue.insert(0, 10))
print("queue = ", queue)
print("queue.pop(0)", queue.pop(0))
print("queue.pop(0)", queue.pop(0))
print("queue.pop(0)", queue.pop(0))
print("queue.pop(0)", queue.pop(0))
print("queue.pop(0)", queue.pop(0))
print("queue = ", queue)
print()

queue = deque([0, 1, 2, 3, 4, 5])
print("queue = ", queue)

queue.append(6)
print("queue = ", queue)
queue.append(7)
print("queue = ", queue)
queue.append(8)
print("queue = ", queue)
queue.append(9)
print("queue = ", queue)
queue.append(10)
print("queue = ", queue)
x = len(queue)
for i in range(x):
    print(queue.popleft(), end=", ")
print()

squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

squares2 = list(map(lambda x: x ** 2, range(11)))
print(squares2)

squares3 = [x ** 2 for x in range(12)]
print(squares3)


def squares(r):
    """Squares."""
    return ([x ** 2 for x in range(r + 1)])


def cubes(r):
    """Cubes."""
    return ([x ** 3 for x in range(r + 1)])

print(squares(12))
print(cubes(10))
print()


def extract(s):
    """Docstring."""
    return [x for x in dir(s) if not x.startswith('_')]


l = extract([])
t = extract(())
d = extract({})
s = extract(set())
st = extract(string)
intgr = extract(integer)
m = ["List", "Tuple", "Dictionary", "Set", "String", "Integer"]

for a, b in ((l, m[0]), (t, m[1]), (d, m[2]),
             (s, m[3]), (st, m[4]), (intgr, m[5])):
    print("\n", b, "Methods")
    print("", "*" * 20)
    f = a[0][0]
    # [print('', i, end=" ") for i in d if i[0] == first]
    for i in a:
        if i[0] == f:
            print('', i, end=" ")
        else:
            print("\n", i, end=" ")
            f = i[0]
    print()
print()


print("Extraction")

extracted = ([extract(x) for x in ([], (), {}, set(), " ", 1)])
m = ["List", "Tuple", "Dictionary", "Set", "String", "Integer"]

for e in extracted:
    f = e[0][0]

    for i in e:
        if i[0] == f:
            print('', i, end=" ")
        else:
            print("\n", i, end=" ")
            f = i[0]
    print("\n")


list_1 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c']]
print("List_1 = ", list_1)


list_2 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if x != 2]
print("List_2 = ", list_2)


list_3 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if y != 'b']
print("List_3 = ", list_3)


list_4 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if x != 2 and y != 'b']
print("List_4 = ", list_4)


list_5 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if x != 2 or y != 'b']
print("List_5 = ", list_5)


list_6 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if x == 2 and y == 'b']
print("List_6 = ", list_6)


list_7 = [(x, y) for x in [1, 2, 3]
          for y in ['a', 'b', 'c'] if x == 2 or y == 'b']
print("List_7 = ", list_7)

vec1 = [-4, -2, 0, 2, 4]
vec3 = [x for x in vec1 if x >= 0]
vec2 = [x * 2 for x in vec1]
vec4 = [x for x in vec2 if x >= 0]
vec5 = [abs(x) for x in vec1]
vec6 = [abs(x) for x in vec2]
vec7 = [(x).bit_length() for x in vec1]
vec8 = [(x).to_bytes(2, 'little') for x in vec5]

print(vec1)
print(vec2)
print(vec3)
print(vec4)
print(vec5)
print(vec6)
print(vec7)
print(vec8)

tup_1 = [(x, x ** 2, x ** 3) for x in range(6)]
print(tup_1)

vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for elem in vector for num in elem]
print(vector)
print(flat)


def flatten(v):
    """Docstring."""
    return [n for e in v for n in e]


print(flatten(vector))

pie = [str(round(pi, i)) for i in range(6)]
print(pie)

matrix3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix4 = [[row[i] for row in matrix3] for i in range(4)]
matrix_Zip = list(zip(*matrix3))

print(matrix3)
print(matrix4)
print(matrix_Zip)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

for i in range(6):
    del a[0]
    print(a)

del a
print('''
print(a)
        Traceback (most recent call last):
        File "./Data_Structures.py", line 319, in <module>
            print(a)
        NameError: name 'a' is not defined
        ''')
t = (12345, 54321, 'Hello!')
print(t)

for i in range(len(t)):
    print(t[i])

u = t, (1, 2, 3, 4, 5)
print(u)

for i in range(len(u)):
    print(u[i])

print(flatten(u))

v = ([1, 2, 3], [3, 2, 1])
print(v)
v[0][1] = 'two'
v[1][1] = 'two'
print(v)

print('''
v[0] = [1, 2, 3]
                Traceback (most recent call last):
                File "./Data_Structures.py", line 347, in <module>
                    v[0] = [1, 2, 3]
                TypeError: 'tuple' object does not support item assignment''')
empty = ()
singleton = ('hello',)
print(len(empty))
print(len(singleton))

n1, n2, greeting = t
print(n1)
print(n2)
print(greeting)

s1 = set()
s2 = {1, 2, 3, 3, 3}
d1 = {}

print(type(s1), s1)
print(type(s2), s2)
print(type(d1), d1)

print(1 in s2)
print(4 in s2)

a = set('abracadabra')
b = set('alacazam')

print(a, b)
print(a)
print(b)
print(a - b)
print(b - a)
print(a | b)
print(b | a)
print(a & b)
print(b & a)
print(a ^ b)
print(b ^ a)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

passwords = {
    'facebook': "FaCeBoOk",
    'twitter': "TwItTeR",
    'reddit': "ReDdIt",
    'tumblr': "TuMbLr"
}

print(passwords)
print(passwords['facebook'])
print(passwords['twitter'])
print(passwords['reddit'])
print(passwords['tumblr'])

del passwords['tumblr']
print(passwords)
print(list(passwords.keys()))
print(sorted(passwords.keys()))
print('reddit' in passwords)
print('tumblr' in passwords)
print('reddit' not in passwords)
print('tumblr' not in passwords)

square = {x: x ** 2 for x in range(1, 11)}
cube = {x: x ** 3 for x in range(1, 11)}

print(square)
print(cube)
print(square[3])
print(cube[3])

simple = dict(a=1, b=2, c=3, d=4)
print(simple)

for k, v in passwords.items():
    print(k, " = ", v, end="\n")

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


def substitution_encrypt(message):
    """Docstring."""
    mes = []
    e = dict([(l, n) for l, n in zip(list(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'abcdefghijklmnopqrstuvwxyz/.!'),
        [x for x in range(1, 56)])])

    print("substitution_encrypt")
    for m in message:
        mes.append(e[m])
    return mes


def substitution_decrypt(ciphertext):
    """Docstring."""
    mes = []
    d = dict([(n, l) for n, l in zip(
        [x for x in range(1, 56)],
        list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             'abcdefghijklmnopqrstuvwxyz/.!'))])

    print("substitution_decrypt")
    for c in ciphertext:
        mes.append(d[c])
    return "".join(mes)


print(substitution_encrypt('The/spy/who/came/in/from/the/cold'))
print(substitution_decrypt([1, 38, 31, 29, 53, 12, 31, 27, 39, 27, 45]))
