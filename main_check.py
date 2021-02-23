#import sys
import float_check as flt


#sys.path.append('C:/Python3/ma_p29/jupyter_files/module_6_modules/homework')
#sys.path.append('C:/Python3/ma_p29/jupyter_files/module_6_modules/homework/ADDITIONAL')


def check_is_float(check_fun):
    assert check_fun("345")
    assert check_fun("+23")
    assert check_fun("-231")
    assert not check_fun("-23y1")
    assert not check_fun("abc")


if __name__ == "__main__":
    try:
        check_is_float(flt.is_float)
        print(f"Success!")
    except Exception:
        print(f"Something wrong!")
