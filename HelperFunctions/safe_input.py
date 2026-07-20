from getpass import getpass
from types import NoneType
def safe_input(expected_type:type, message:str=None, default=None, is_password:bool=False, feedback:bool=False):
    """
    Prompt the user for input and safely convert it to the given type.
    If default is not set, the program will loop until a valid response is given.
    This looping behavior will be turned off if the default is set to a value other than None.
    If an exception occurs, the types zero equivalent will be returned (except in ValueError where default is returned).

    Args:
        expected_type (type): The type to convert the input into (e.g., int, float, str, bool).
        message (str, optional): Custom message to display instead of the default.
        default (any, optional): Default value to return if conversion fails.
        is_password (bool, optional): If True, input will be hidden (for passwords).
        feedback (bool, optional): If True, errors will print more details.
        
    Returns:
        The converted value of the correct type.
    """

    zero_eq = {
        int: 0,
        float: 0.0,
        complex: 0 + 0j,
        bool: False,
        str: "",
        list: [],
        tuple: (),
        set: (),
        frozenset: (),
        dict: {},
        NoneType: None
        }


    while True:
        try:
            prompt = (
                message
                if message is not None
                else f"Enter a(n) ({expected_type.__name__}): "
            )
            if is_password:
                user_input = getpass(prompt)
            else:
                user_input = input(prompt)

            # Special handling for bool
            if expected_type is bool:
                lowered = user_input.strip().lower()
                if lowered in ("true", "1", "yes", "y"):
                    return True
                elif lowered in ("false", "0", "no", "n"):
                    return False
                else:
                    raise ValueError("Invalid boolean input")

            if expected_type is str:
                if user_input == "" and default is not None:
                    return default

            # Attempt conversion for other types
            return expected_type(user_input)

        except ValueError as ve:
            if feedback:
                print(f"Error Trace: {ve}")

            if default is not None:
                print(f"Invalid input. Using default value: {default}")
                return default
            else:
                print(f"Invalid input. Please enter a valid {expected_type.__name__}.")
                return safe_input(expected_type=expected_type, message=message, default=default, is_password=is_password)
                


        except KeyboardInterrupt as kie:
            print("\nKeyboard interrupt detected. Aborting input.")
            if feedback:
                print(f"Error Trace: {kie}")

            return zero_eq[expected_type]
        except EOFError as eofe:
            if feedback:
                print(f"Error Trace: {eofe}")

            print("\nEnd of input detected (Ctrl+D).")
            return zero_eq[expected_type]

if __name__ == "__main__":
    # Example usage
    age = safe_input(int, "Enter your age: ", default=18)
    print(f"Your age is: {age}")
    height = safe_input(float, "Enter your height in meters: ", default=1.75)
    print(f"Your height is: {height} meters")
    name = safe_input(str, "Enter your name: ", default="Guest")
    print(f"Hello, {name}!")
    wants_newsletter = safe_input(bool, "Do you want to subscribe to the newsletter? (yes/no): ", default=False)
    print(f"Newsletter subscription: {wants_newsletter}")
    password = safe_input(str, "Enter your password: ", is_password=True)
    print(f"Your password is: {'*' * len(password) if password else 'None'}")

    # Example errors
    val_error = safe_input(int, "Enter a Float: ", default=10, feedback=True)


    keyinterrupt_error = safe_input(bool, "Press ctrl + c", feedback=True)
    print(keyinterrupt_error)

    eof_error = safe_input(str, "Enter ctrl + d", feedback=True)
    print(eof_error)