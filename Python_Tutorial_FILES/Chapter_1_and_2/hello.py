#!/usr/bin/env python3

from platform import python_version
print("The Python Version is:", python_version())

import sys
print("The Python version is: %s.%s.%s "  % sys.version_info[:3])
print (sys.version)
print (sys.version_info)
print(sys.hexversion)

print()
print("Hello World!")

'''
j@jbox ~/Desktop/NFS_Share/Programming/Python/Python-Tutorial/Python_Tutorial_FILES $ ./hello.py
The Python Version is: 3.5.2
The Python version is: 3.5.2 
3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609]
sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0)
50660080

Hello World!
'''