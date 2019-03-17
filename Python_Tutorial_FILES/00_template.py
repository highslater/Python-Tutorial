#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# template.py
"""DOCstring for 00_template.py.

2nd line of DOCstring
"""

import logging
from platform import python_version
from sys import hexversion


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_00.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("00_template.pyRUN / START")


print("The Python Version is:", python_version(), " #" + str((hexversion)))
print("\nData Structures\n")
