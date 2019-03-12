#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Crypyanalysis.py
"""DOCstring for Crypyanalysis.py.

2nd line of DOCstring
"""


def letter_substitution_encrypt(plain_text):
    """Docstring."""
    cipher_text = []
    f = (list('abcdefghijklmnopqrstuvwxyz/.!'))
    r = (list('abcdefghijklmnopqrstuvwxyz/.!'))
    r.reverse()
    e = dict([(l, n) for l, n in zip(f, r,)])
    print("letter substitution_encrypt")

    for p in plain_text:
        cipher_text.append(e[p])
    # cipher_text = ''.join(cipher_text)
    return cipher_text


def letter_substitution_decrypt(cipher_text):
    """Docstring."""
    plain_text = []
    f = (list('abcdefghijklmnopqrstuvwxyz/.!'))
    r = (list('abcdefghijklmnopqrstuvwxyz/.!'))
    r.reverse()
    d = dict([(l, n) for l, n in zip(r, f,)])
    print("letter substitution_decrypt")

    for c in cipher_text:
        plain_text.append(d[c])
    plain_text = "".join(plain_text)
    return plain_text


def number_substitution_encrypt(plain_text):
    """Docstring."""
    cipher_text = []
    e = dict([(l, n) for l, n in zip(list(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        'abcdefghijklmnopqrstuvwxyz'
        '/.!'),
        [x for x in range(1, 56)])])

    print("number substitution_encrypt")
    for m in plain_text:
        cipher_text.append(e[m])
    return cipher_text


def number_substitution_decrypt(cipher_text):
    """Docstring."""
    plain_text = []
    d = dict([(n, l) for n, l in zip(
        [x for x in range(1, 56)],
        list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             'abcdefghijklmnopqrstuvwxyz'
             '/.!'))])

    print("number substitution_decrypt")
    for c in cipher_text:
        plain_text.append(d[c])
    plain_text = "".join(plain_text)
    return plain_text


print(number_substitution_encrypt('The/spy/who/came/in/from/the/cold'))
print(number_substitution_encrypt('Alec/Leamas'))
print(number_substitution_decrypt([
    20, 34, 31, 53, 45, 42, 51, 53, 49, 34,
    41, 53, 29, 27, 39, 31, 53, 35, 40, 53,
    32, 44, 41, 39, 53, 46, 34, 31, 53, 29,
    41, 38, 30]))
print(number_substitution_decrypt([
    1, 38, 31, 29, 53, 12, 31, 27, 39, 27, 45]))

print(letter_substitution_encrypt("plaintext"))
print(letter_substitution_decrypt([
    'n', 'r', '!', 'u', 'p', 'j', 'y', 'f', 'j']))
