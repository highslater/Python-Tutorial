#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# hello.py

"""Doc String for hello.py."""

from platform import python_version
import sys

print("The Python Version is:", python_version())
print("The Python version is: %s.%s.%s " % sys.version_info[:3])
print (sys.version)
print (sys.version_info)
print("sys.hexversion", sys.hexversion)
print("\nHello World!\n")
