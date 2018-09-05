#!/usr/bin/env python3

import sys

# libpath

try:
    if (sys.version_info.major <= 2) and (sys.version_info.minor < 7):
        raise Exception("You must run Syncplay with Python 2.7!")
    if (sys.version_info.major >= 3) and (sys.version_info.minor < 4):
        raise Exception("You must run Syncplay with Python 3.4 or newer!")
except AttributeError:
    import warnings
    warnings.warn("You must run Syncplay with Python 2.7 or 3.4 or newer!")

from syncplay.clientManager import SyncplayClientManager
from syncplay.utils import blackholeStdoutForFrozenWindow

if __name__ == '__main__':
    blackholeStdoutForFrozenWindow()
    SyncplayClientManager().run()
