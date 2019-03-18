#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# template.py
"""DOCstring for fibo.py .

2nd line of DOCstring
"""

import logging
from platform import python_version
from sys import hexversion


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_fibo.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("fibo.py RUN / START")

# ====== Executable Statements ======

print("The Python Version is:", python_version(), " #" + str((hexversion)))
print("Modules/fibo.py")
print("fibo.py name =", __name__)


# ====== Function Definitions ======

def fib(n):
    """Write fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=', ')
        a, b = b, a + b
    print()


def fib2(n):
    """Return fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
