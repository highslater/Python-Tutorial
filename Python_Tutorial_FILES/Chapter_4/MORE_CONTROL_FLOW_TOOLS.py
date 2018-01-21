#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #"+ str((hexversion)))
print("\nMORE CONTROL FLOW TOOLS\n")

# x = int(input("Please enter an integer."))
x = 42
print("You have entered: ", x)

if x < 0:
    print(x, " was changed to zero")
    x = 0
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

"""
There can be zero or more elif parts, and the else part is optional. The keyword ‘elif ‘ is short for ‘else if’,
and is useful to avoid excessive indentation. An if ... elif ... elif ... sequence is a substitute for the switch
or case statements found in other languages.

"""

# Measure some Strings
words = ['cat', 'window', 'defenestrate']
big_words = []
for w in words[:]:
    if len(w) > 6:
        big_words.insert(0, w)
    print(w, len(w), end = " ***\n")
print("words = ", words)
print("big words = ", big_words)

for i in range(5):
    print(i, end = ",")

print()

for i in range(5, 10):
    print(i, end = ",")

print()

for i in range(0, 10, 3):
    print(i, end = ",")

print()

for i in range(-10, -100, -30):
    print(i, end = ",")

print()

a = ['Mary', 'had', 'a', 'little', 'lamb']
print(a, len(a))

sentenceWords = []                      # the sentence as a list of lists
sentenceLetters = []                    # the sentence as a list of letters
for i in range(len(a)):
    letters = []                        # the list of letters for sentenceWords
    print(i, a[i], len(a[i]))
    for j in range(len(a[i])):
        letters.insert(j, a[i][j])      # build a list of letters for sentenceWords
        sentenceLetters.append(a[i][j]) # add letters to sentenceLetters
        print(a[i][j], end = "  ")
    sentenceWords.append(letters)       # add letters to sentenceWords
    print()
    print(letters)
print(sentenceWords)
print(sentenceLetters)

"""
It is convenient to use the enumerate() function, see Looping Techniques.
"""

print(range(10))
print(list(range(10)))

w1 = range(10)
print(w1)

w2 = list(range(10))
print(w2)

w3 = list("vegetable")
print(w3)

print()


sWords = []
sLetters = []
for i in range(len(a)):
    sWords.append(list(a[i]))
    for j in range(len(a[i])):
        sLetters.append(a[i][j])
print(sWords, len(sWords))
print(sLetters, len(sLetters))

print()

l = "Mary had a little lamb"
l = list(l.replace(" ", ""))
print(l, len(l))

print()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, ' * ', n//x)
            break
    else:
        print(n, 'is a prime number')

print()

for num in range(2, 10):
    if num % 2 == 0:
        print('found an even number', num)
        continue
    print('found a number', num)



# while True:
    # pass
        # Process finished with exit code 0 is not seen when this is uncommented

class MyEmptyClass:
    pass

def initlog(*args):
    pass


def fib(n):     # Write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end = " ")
        a, b = b, a + b
    print()

fib(2000)

print(fib(0))

f = fib

f(2000)


def fib2(n):     # Return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)


def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise valueError('invalid user response')
        print(reminder)

# ask_ok('do you really want to quit ?')

# ask_ok('OK to overwrite the file ?', 2)

# ask_ok('OK to overwrite the file ?', 2, 'Only yes or no')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

print()
print(f(75, [150]))
print(f(37.5, [150]))

L = []
print(f(99))

def f(a, L= None):
    if L == None:
        L = []

    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))

print()
print(f(75, [150]))
print(f(37.5, [150]))
print(f(99))













































