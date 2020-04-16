# python modules.py
# import module_name
# module_name.method_name()
# from module_name import method_name
# method_name()
# i.e. csv, logging, urllib.request, json
import time
import sys
from sample_modules import say_hello

print(time.asctime())
print(time.timezone)

# See contents of module
print(dir(time))

# Returns search path for modules
print(sys.path)

# Using other module function
say_hello()
