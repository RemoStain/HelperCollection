from HelperFunctions.safe_input import safe_input


"""
Available functions:
    _is_falsy(): bool
    _is_truthy(): bool
    _cls(): None
    _generate_dashes(): str
    _menu(): str | None
    _apply_discount(): float
    _validate_email(): bool
"""


def _is_falsy(variable=None) -> bool:
    """
    Helper
    Check if the argument is None, or Falsey

    Args:
        variable: Value to check.

    Returns:
        bool: Is the value None or Falsy (True) or not (False)
    """
    if not variable:
        return True
    else:
        return False

def _is_truthy(variable=None) -> bool:
    """
    Helper
    Check if the argument is True or Truthy

    Args:
        variable: Value to check.

    Returns:
        bool: Is the value Truthy (True) or not (False).
    """
    if variable:
        return True
    else:
        return False


def _cls() -> None:
    """
    Helper
    Clear the console screen.

    Returns:
        None
    """
    print("\033[H\033[J", end="")
    return


def _generate_dashes(n: int = 0, title: bool = False) -> str:
    """
    Helper
    Generate a string of dashes based on the input number.

    Args:
        n (int): The number of dashes to generate.
        title (bool): A toggle that switches the dash generation for titles or drink names.

    Returns:
        str: A string of dashes.
    """
    if title:
        # for titles, allow as many dashes as desired
        dashes = "-" * n
    else:
        possible_dashes = [
            "-----------",
            "----------",
            "---------",
            "--------",
            "-------",
            "------",
            "-----",
            "----",
            "---",
            "--",
            "-",
        ]
        # the number and dashes should add up to 12 characters
        nn = len(str(n))
        dashes = possible_dashes[nn - 1]
    return dashes


def _menu(header: str = "Menu", items: list = []) -> str | None:
    """
    Display a menu of items and return the selected item.

    Args:
        header (str): The header of the menu.
        items (list): A list of items to display in the menu.

    Returns:
        str | None: The selected item, or None if the user chooses to exit.
    """

    option = 1
    header_padding = "------------"
    d = _generate_dashes(len(header_padding), True)
    print(f"{d} {header} {d}\n")

    # Special Case: if len is 1 then display it and return that option
    if len(items) == 1:
        print(f"Only 1 option available: {items[0]}")
        c = 1

    else:
        for i in items:
            # generate dashes based on the length of the option number
            dashes = _generate_dashes(option)
            # print the option number, dashes, and item
            print(f"{option} {dashes} {i}")
            # increment the option number for the next item
            option = option + 1
        print()
        c = safe_input(int, "Choose an option: ")

    # if within list range, return the 0-indexed item
    if c >= 1 and c <= len(items):
        return items[(c - 1)]

    # if less than 1, return None for further logic (usually a retry)
    # also works as an exit key
    elif c < 1:
        return None

    # recursive loop until a valid answer is given
    else:
        _cls()
        name = _menu(header=header, items=items)
        return name


def _apply_discount(number:float=0, discount:float=None):
    """
    Helper
    Apply a discount percentage to a starting number.

    Args:
        number (float): The number to apply discount to.
        discount (float): The discount as a positive percentage.

    Returns:
        float: The discounted value
    """
    if discount <= 0:
        return number
    return number - (number * (discount / 100))


def _validate_email(email:str="") -> bool:
    """
    Helper
    Check if email is valid.

    Args:
        email (str): The string to check.

    Returns:
        bool: Is the string a valid email.
    """
    return "@" in email and "." in email
