
from . import *

def exception_logging_test():
    exception_logging.tests()
    return

def helpers_menu_test():
    helpers_and_menu.tests()
    return

def help_call_test():
    help_call.tests()
    return

def math_func_test():
    math_func.tests()
    return

def safe_input_test():
    safe_input.tests()
    return

def unit_converter_test():
    unit_converter.tests()
    return

def main(exceptions_too:bool=False):
    if exceptions_too:
        exception_logging_test()
        print("-----")

    # bypasses input req.
    helpers_menu_test()
    print("-----")

    help_call_test()
    print("-----")

    math_func_test()
    print("-----")

    # safe_input_test()
    # print("-----")

    unit_converter_test()
    print()

    print("Tests Complete!")


if __name__ == "__main__":
    main()