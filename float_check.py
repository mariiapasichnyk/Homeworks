"""
Check whether the input string contains a float number or not
"""
#import sys

#sys.path.append('C:/Python3/ma_p29/jupyter_files/module_6_modules/homework')
#sys.path.append('C:/Python3/ma_p29/jupyter_files/module_6_modules/homework/ADDITIONAL')


def is_float(str_int):
    if any(char.isalpha() for char in str_int):
        return False
    else:
        return True
