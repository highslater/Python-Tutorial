#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# template.py
"""DOCstring for 06_Chapter_6_Modules.py .

2nd line of DOCstring
"""

import logging
from platform import python_version
from sys import hexversion
import importlib
import fibo

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_06.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("06_Chapter_6_Modules.py RUN / START")

print("\nThe Python Version is:", python_version(), " #" + str((hexversion)))
print("Modules/06_Chapter_6_Modules.py")
print("06_Chapter_6_Modules.py name =", __name__)
print("fibo.py name =", fibo.__name__, "\n")

print("06_Chapter_6_Modules.py issued command 'importlib.reload(fibo)'")
importlib.reload(fibo)

print("", "*" * 90, "\n")
print("", "fibo.fib(10000) =")
fibo.fib(10000)
print("\n", "*" * 90)

f = fibo.fib2(100)
print("f = ", f)
