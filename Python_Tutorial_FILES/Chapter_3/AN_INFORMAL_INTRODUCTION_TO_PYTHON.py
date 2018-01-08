#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #"+ str((hexversion)))
print("\nAN INFORMAL INTRODUCTION TO PYTHON\n")

print("2 + 2 = \t\t\t", 2 + 2)
print("50 - 5*6 = \t\t\t", 50 - 5*6)
print("(50 - 5*6) / 4 = \t", ((50 - 5*6) / 4))
print("8 /5 = \t\t\t\t", 8 / 5)
print("17 / 3 = \t\t\t", 17 / 3)
print("17 // 3 = \t\t\t", 17 // 3)
print("17 % 3 = \t\t\t", 17 % 3)
print("5 * 3 + 2 = \t\t", 5 * 3 + 2)
print("17 / 3 = \t\t\t", 17 //3, "with a remainder of ", 17 % 3)

print("5 squared = \t\t", 5 ** 2)
print("2 to power 7 = \t\t", 2 ** 7)

width = 20
height = 5 * 9
print("width x height = \t", width * height)
print("4 x 3.75 - 1 = \t\t", 4 * 3.75 -1)

tax = 12.5 / 100
price = 100.50
print("The price is: \t\t", price)
print("The tax rate is: \t", tax)
print("The tax is: \t\t", price * tax)
print("The total is: \t\t", round(price + price * tax,2))

print('\nspam eggs')
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

s = "First line. \nSecond line."
print(s)
print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
        -h              Display this usage message
        -H              Hostname to connect to
""")

print("3 x um followed by ium ", 3 * "um" + "ium")
print("Py" "thon")

prefix = "Py"
print(prefix + "thon")

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

word = "Python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print("\n")
print(word[-6])
print(word[-5])
print(word[-4])
print(word[-3])
print(word[-2])
print(word[-1])

print("\n")
print(word[0:1])
print(word[0:2])
print(word[0:3])
print(word[0:4])
print(word[0:5])
print(word[0:6])

print("\n")
print(word[0:3])
print(word[3:6])
print(word[0:3] + word[3:6])
print(word[:3] + word[3:])
print(word[:-3] + word[-3:])
print(len(word[:3]))
print('J' + word[1:])
print(word[:2] + "py")

"""
See also:
textseq Strings are examples of sequence types, and support the common operations supported by such types.
string-methods Strings support a large number of methods for basic transformations and searching.
formatstrings Information about string formatting with str.format() .
old-string-formatting The old formatting operations invoked when strings are the left operand of the % operator are
described in more detail here.

"""


squares = [1, 2, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[1])
print(squares[2])
print(squares[3])
print(squares[4])
print(squares[5])

print(squares[-1])
print(squares[-2])
print(squares[-3])
print(squares[-4])
print(squares[-5])
print(squares[-6])

print(squares[:3])
print(squares[3:])
print(squares[:3] + squares[3:])

print(squares[:-3])
print(squares[-3:])
print(squares[:-3] + squares[-3:])

print(squares[:])
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)

cubes.append(216)
cubes.append(7 **3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(len(letters))
letters[2:5] = ['C', 'D', 'E']
print(letters)
print(len(letters))
letters[2:5] = []
print(letters)
print(len(letters))
letters[:] = []
print(letters)
print(len(letters))
















































