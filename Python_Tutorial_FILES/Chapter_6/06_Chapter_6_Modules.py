#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# template.py
"""DOCstring for 06_Chapter_6_Modules.py .

2nd line of DOCstring
"""

import logging
from platform import python_version
from sys import hexversion
import fibo


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_06.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("06_Chapter_6_Modules.py RUN / START")

print("The Python Version is:", python_version(), " #" + str((hexversion)))
print("\nModules\n")
print("fibo.__name__ =", fibo.__name__)
print("fibo.fib(100) =", fibo.fib(100))

f = fibo.fib2(1000)
print("f = ", f)
print("fibo.result =", fibo.result)
