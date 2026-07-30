


def get_function_names(filename:str="help_call.py", display:bool=False):
    """
    Print all the python functions in a given file.
    Defaults to itself if no filename is provided.

    Args:
        filename (str): The path to the python file.
        display (bool): Whether to print the function names or just return them.

    Returns:
        list[str]: A list of function names in the file, including class methods.
    """
    # import inside the function to avoid unnecessary imports if the function is not called
    import re

    # compile regex patterns for function and class definitions
    DEF_RE = re.compile(r"^\s*def\s+([A-Za-z_]\w*)\s*\(")
    CLASS_RE = re.compile(r"^\s*class\s+([A-Za-z_]\w*)\s*(?:[(:]|:)")

    # initialize a stack to keep track of class names and their indentation levels
    class_stack: list[tuple[int, str]] = []
    results: list[str] = []

    # open the file and read it line by line
    with open(filename, "r", encoding="utf-8") as f:
        # iterate through each line in the file, checking for class and function definitions
        for line in f:
            m_class = CLASS_RE.match(line)
            
            # if a class definition is found, update the class stack with the current class name and its indentation level
            if m_class:
                indent_len = len(m_class.group(1).replace("\t", " "))
                class_name = m_class.group(1)

                # pop classes from the stack if their indentation level is greater than or equal to the current class's indentation level
                while class_stack and class_stack[-1][0] >= indent_len:
                    class_stack.pop()

                # push the current class onto the stack
                class_stack.append((indent_len, class_name))

                continue

            # if a function definition is found, determine its name and whether it is a method of a class or a standalone function
            m_def = DEF_RE.match(line)
            if m_def:
                func_name = m_def.group(1)

                # lstrip both tabs and 4 spaces, which means we have to % 4 the class_stack value
                indent_len = len(line[:len(line) - len(line.lstrip("\t").lstrip("    "))].replace("\t", " "))

                # pop classes from the stack if their indentation level is greater than or equal to the current function's indentation level
                while class_stack and ((class_stack[-1][0])%4) >= indent_len:
                    class_stack.pop()

                # if there are classes in the stack, the function is a method of the last class in the stack; otherwise, it is a standalone function
                if class_stack:
                    results.append(f"{class_stack[-1][1]}.{func_name}")
                else:
                    results.append(func_name)

    # if display is True, print the results; finally, return the list of function names
    if display:
        print(f"Function names found in {filename}: ")
        for r in results:
            print(r)
    return results


if __name__ == "__main__":
    print("Display = True")
    _ = get_function_names(display=True)

    print("\nDisplay = False")
    print(f"Printing the returned names: {get_function_names()}")
