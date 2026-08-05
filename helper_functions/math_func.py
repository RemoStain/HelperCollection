# all done without math import


math_constant = {
    # math constants
    "pi": 3.141592653589793,  # pi
    "e": 2.718281828459045,  # euler's number
    "phi": 1.618033988749895,  # golden ratio
    "sqrt2": 1.4142135623730951,  # square root of 2
    "sqrt3": 1.7320508075688772,  # square root of 3
    "sqrt5": 2.23606797749979,  # square root of 5
    "ln2": 0.693147180559945,  # natural logarithm of 2
    "ln10": 2.302585092994046,  # natural logarithm of 10
    "log2e": 1.442695040888963,  # log base 2 of e
    "log10e": 0.434294481903252,  # log base 10 of e

    # physical constants
    "gravitational": 9.80665,  # gravitational acceleration in m/s^2
    "elementary_charge": 1.602176634e-19,  # elementary charge in coulombs
    "planck": 6.62607015e-34,  # Planck's constant in J*s
    "light": 299792458,  # speed of light in m/s
    "e_mass": 9.10938356e-31,  # electron mass in kg

    #chemical constants
    "avogadro": 6.02214076e23,  # Avogadro's number
    "Molar_gas_constant": 8.314462618,  # Molar gas constant in J/(mol*K)
    "Molar_mass_c12": 0.012,  # Molar mass of carbon-12 in kg/mol
    "faradays_constant": 96485.33212,  # Faraday's constant in C/mol

}

math_descriptions = {
    # math constants
    "pi": "The ratio of a circle's circumference to its diameter.",
    "e": "Euler's number, the base of natural logarithms.",
    "phi": "The golden ratio, an irrational number that appears in many natural phenomena.",
    "sqrt2": "The square root of 2, the length of the diagonal of a square with side length 1.",
    "sqrt3": "The square root of 3, the length of the diagonal of a cube with side length 1.",
    "sqrt5": "The square root of 5, the length of the diagonal of a pentagon with side length 1.",
    "ln2": "The natural logarithm of 2, the power to which e must be raised to get 2.",
    "ln10": "The natural logarithm of 10, the power to which e must be raised to get 10.",
    "log2e": "The logarithm base 2 of e, the power to which 2 must be raised to get e.",
    "log10e": "The logarithm base 10 of e, the power to which 10 must be raised to get e.",

    # physical constants
    "gravitational": "The acceleration due to gravity on Earth, approximately 9.81 m/s^2.",
    "elementary_charge": "The elementary charge, the electric charge carried by a single proton. Symbol: \u0065",
    "planck": "Planck's constant, a fundamental constant in quantum mechanics. Symbol: \u0068",
    "light": "The speed of light in a vacuum, a fundamental constant in physics. Symbol: \u0063",
    "e_mass": "The mass of an electron, a fundamental particle in physics. Symbol: \u006D",

    # chemical constants
    "avogadro": "Avogadro's number, the number of atoms or molecules in one mole of a substance.",
    "Molar_gas_constant": "The molar gas constant, a physical constant that relates the energy scale to the temperature scale in ideal gases.",
    "Molar_mass_c12": "The molar mass of carbon-12, a standard for defining the mole and atomic mass unit.",
    "faradays_constant": "Faraday's constant, the total electric charge carried by one mole of electrons. Symbol: \u0066",
    }

# describe math constants
def describe_math_constant(constant: str) -> str:
    """
    Describe a mathematical constant.
    Args:
        constant: str: The name of the mathematical constant.
    Returns:
        str: A description of the mathematical constant.
    """
    if constant not in math_descriptions:
        raise ValueError(f"{constant} is not a listed mathematical constant.")
    return math_descriptions[constant]


# ----- Basic Math Functions -----
# add as many numbers as are given
def add_all(*nums: int | float, type_: type = None) -> int | float:
    """
    Add as many numbers as are given and return the sum as the type of the first number.

    Args:
        *nums: int | float: The numbers to add.
        type_: type: The type to return the sum as. If None, the type of the first number is used.

    Returns:
        int | float: The sum of the numbers as the specified type.
    """
    if not nums:
        raise ValueError("add_all() needs at least one number.")
    if type_ is None:
        type_ = type(nums[0])
    t = sum(nums)
    return type_(t)


# subtract as many numbers as given
def sub_all(*nums: int | float, type_: type = None) -> int | float:
    """
    Subtract as many numbers as are given and return the difference as the type of the first number.

    Args:
        *nums: int | float: The numbers to subtract.
        type_: type: The type to return the difference as. If None, the type of the first number is used.

    Returns:
        int | float: The difference of the numbers as the specified type.
    """
    if not nums:
        raise ValueError("sub_all() needs at least one number.")

    if type_ is None:
        type_ = type(nums[0])

    t = nums[0]
    for n in nums[1:]:
        t -= n
    return type_(t)


# multiply as many numbers as given
def mult_all(*nums: int | float, type_: type = None) -> int | float:
    """
    Multiply as many numbers as are given and return the product as the type of the first number.

    Args:
        *nums: int | float: The numbers to multiply.
        type_: type: The type to return the product as. If None, the type of the first number is used.

    Returns:
        int | float: The product of the numbers as the specified type.
    """
    if not nums:
        raise ValueError("mult_all() needs at least one number.")
    if type_ is None:
        type_ = type(nums[0])

    if 0 in nums:
        return 0
    if len(nums) == 1:
        return type_(nums[0])
    t = nums[0]
    for n in nums[1:]:
        t *= n
    return type_(t)


# div as many numbers as given
def div_all(
    *nums: int | float, type_: type = None, floor: bool = False
) -> int | float | None:
    """
    Divide as many numbers as are given and return the quotient as the type of the first number.

    Args:
        *nums: int | float: The numbers to divide.
        type_: type: The type to return the quotient as. If None, the type of the first number is used.
        floor: bool: If True, the result will be floored to an integer.

    Returns:
        int | float: The quotient of the numbers as the specified type.
    """
    if not nums:
        # raise ValueError("div_all() needs at least one number.")
        return 0
    if type_ is None:
        type_ = type(nums[0])

    if float(nums[0]) == 0.0:
        return nums[0]
    if 0 in nums[1:]:
        # raise ValueError("Cannot divide by zero.")
        return nums[0]

    t = type_(nums[0])
    for n in nums[1:]:
        t /= n

    if floor:
        t = int(t)
    return type_(t)


# Exponentiate as many numbers as given, in the order given
def exp_all(*nums: int | float, type_: type = None) -> int | float:
    """
    Exponentiate as many numbers as are given and return the result as the type of the first number.

    Args:
        *nums: int | float: The numbers to exponentiate.
        type_: type: The type to return the result as. If None, the type of the first number is used.

    Returns:
        int | float: The result of exponentiating the numbers as the specified type.
    """
    if not nums:
        raise ValueError("exp_all() needs at least one number.")
    if type_ is None:
        type_ = type(nums[0])
    t = nums[0]

    # if any of the nums are 0, the result is 1
    if 0 in nums:
        return type_(1)

    for n in nums[1:]:
        t **= n
    return type_(t)


# factorial of an integer, returns int
def factorial(num: int) -> int:
    """
    Calculate the factorial of a non-negative, non-zero integer.

    Args:
        num: int: The integer to calculate the factorial of.

    Returns:
        int: The factorial of the integer.
    """
    if num < 0:
        raise ValueError("factorial() does not support negative numbers.")

    result = 1

    for value in range(2, num + 1):
        result *= value

    return result


# ----- Fractions Functions -----
# simplify fractions
def reduce_fraction(numerator: int, denominator: int):
    """
    Reduce a fraction to its simplest form and return the result as a tuple of (numerator, denominator).

    Args:
        numerator: int: The numerator of the fraction.
        denominator: int: The denominator of the fraction.

    Returns:
        tuple[int, int]: The reduced fraction as a tuple of (numerator, denominator).
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if numerator == 0:
        return (0, 1)

    # Handle negative signs properly
    sign = -1 if (numerator < 0) ^ (denominator < 0) else 1
    n, d = abs(numerator), abs(denominator)

    common_divisor = gcd(n, d)
    return (sign * (n // common_divisor), d // common_divisor)


# decimal into frac using the reduce_fraction function
def decimal_to_frac(num: float) -> tuple[int, int]:
    """
    Convert a decimal number to a fraction and return the result as a tuple of (numerator, denominator).
    Cannot handle scientific notation, only decimal numbers.

    Args:
        num: float: The decimal number to convert.

    Returns:
        tuple[int, int]: The fraction as a tuple of (numerator, denominator).
    """
    if not num:
        return (0, 1)
    # convert decimal to fraction
    # get the number of decimal places
    decimal_places = str(num)[::-1].find(".")
    denominator = 10**decimal_places
    numerator = int(num * denominator)
    return reduce_fraction(numerator, denominator)


#improper fraction to proper fraction as tuple of whole, num, and denom
def improper_to_proper_frac(numerator:float = 0, denominator:float = 1):
    whole = 0
    if not denominator:
        return 0, 0, 0
    if numerator < denominator:
        return whole, numerator, denominator
    if numerator == denominator:
        return 1, 0, 1

    temp_n = numerator
    while True:
        temp_n -= denominator
        
        whole += 1

        numerator = temp_n

        if temp_n < denominator:
            break

    return whole, numerator, denominator


# proper to improper as tuple of num, and denom,
def proper_to_improper_frac(whole:int=0, numerator:float = 0, denominator:float = 1):
    if not denominator:
        return 0, 0
    if not whole:
        return numerator, denominator
    new_numerator = (whole * denominator) + numerator

    return new_numerator



# ----- Rounding Functions -----
# round to given decimal and retain type ---> option to force round up or down
def rounding(
    num: int | float, decimal: int = 0, type_: int | float = None, force: str = None
) -> int | float:
    """
    Round a number to a given decimal and retain the type of the number.

    Args:
        num: int | float: The number to round.
        decimal: int: The number of decimal places to round to.
        type_: type: The type to return the rounded number as. If None, the type of the number is used.
        force: str:
            If "up", the number will be rounded up.
            If "down", the number will be rounded down towards 0.
            If "truedown", the number will be rounded down towards -infinity.
            If None, the number will be rounded normally.

    Returns:
        int | float: The rounded number as the specified type.
    """
    if not num:
        # raise ValueError("div_all() needs at least one number.")
        return 0
    if type_ is None:
        type_ = type(num)

    if force == "up":
        rounded_num = -(-round(num, decimal) // 1)

    # down is towards 0
    elif force == "down":
        # p is power
        p = 10**decimal
        rounded_num = int(num * p) / p

    # truedown is towards -infinity
    elif force == "truedown":
        p = 10**decimal
        rounded_num = (num // (1 / p)) / p

    else:
        rounded_num = round(num, decimal)

    return type_(rounded_num)


# ----- Root Functions -----
# root
def sq_root(num: int | float, root: int | float = 2, type_: type = None) -> int | float:
    """
    Calculate the root of a number and return the result as the type of the number.

    Args:
        num: int | float: The number to calculate the root of.
        root: int | float: The root to calculate. Default is 2 (square root).
        type_: type: The type to return the result as. If None, the type of the number is used.

    Returns:
        int | float: The root of the number as the specified type.
    """
    if not num:
        # raise ValueError("div_all() needs at least one number.")
        return 0
    if type_ is None:
        type_ = type(num)
    if root == 0:
        raise ValueError("Cannot calculate root of zero.")
    t = num ** (1 / root)
    return type_(t)


# root x of num
def root_n(num: int | float, x: int | float, type_: type = None) -> int | float:
    """
    Calculate the x-th root of a number and return the result as the type of the number.

    Args:
        num: int | float: The number to calculate the root of.
        x: int | float: The root to calculate.
        type_: type: The type to return the result as. If None, the type of the number is used.

    Returns:
        int | float: The x-th root of the number as the specified type.
    """
    if not num:
        # raise ValueError("div_all() needs at least one number.")
        return 0
    if type_ is None:
        type_ = type(num)
    if x == 0:
        raise ValueError("Cannot calculate root of zero.")
    t = num ** (1 / x)
    return type_(t)


# ----- Trig Functions -----
# contain all the trig functions in one class so it can self reference
class TrigFunctions:
    """
    A class containing trigonometric functions.

    Methods:
        sin(x: float, type_: type | None = None) -> float:
            Calculate the sine of an angle in degrees.
        cosecant(x: int | float, type_: type | None = None) -> int | float:
            Calculate the cosecant of an angle in degrees.
        cos(x: int | float, type_: type | None = None) -> int | float:
            Calculate the cosine of an angle in degrees.
        secant(x: int | float, type_: type | None = None) -> int | float:
            Calculate the secant of an angle in degrees.
        tan(x: int | float, type_: type | None = None) -> int | float:
            Calculate the tangent of an angle in degrees.
        cotangent(x: int | float, type_: type | None = None) -> int | float:
            Calculate the cotangent of an angle in degrees.

    All angles are in degrees, and the output type can be specified. If no type is specified, the output type will match the input type.
    """

    @staticmethod
    def _resolve_type(x: float, type_: type | None) -> type:
        """
        Resolve the output type based on the input value and the specified type.

        Args:
            x: float: The input value.
            type_: type | None: The specified type. If None, the type of the input is used.

        Returns:
            type: The resolved output type.
        """
        return type(x) if type_ is None else type_

    @staticmethod
    def _to_radians(x: float) -> float:
        """
        Convert degrees to radians.

        Args:
            x: float: The angle in degrees.

        Returns:
            float: The angle in radians.
        """
        return x * (math_constant["pi"] / 180)

    @staticmethod
    def _sin_radians(x: int | float) -> float:
        term = float(x)
        result = term

        for n in range(1, 10):
            term *= -(x * x) / ((2 * n) * (2 * n + 1))
            result += term

        return result

    @staticmethod
    def _cos_radians(x: int | float) -> float:
        term = 1.0
        result = term

        for n in range(1, 10):
            term *= -(x * x) / ((2 * n - 1) * (2 * n))
            result += term

        return result

    @staticmethod
    def sin(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the sine of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The sine of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)

        return output_type(TrigFunctions._sin_radians(radians))

    @staticmethod
    def cosecant(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the cosecant of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The cosecant of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)
        sin_x = TrigFunctions._sin_radians(radians)

        return output_type(1 / sin_x)

    @staticmethod
    def cos(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the cosine of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The cosine of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)

        return output_type(TrigFunctions._cos_radians(radians))

    @staticmethod
    def secant(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the secant of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The secant of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)
        cos_x = TrigFunctions._cos_radians(radians)

        return output_type(1 / cos_x)

    @staticmethod
    def tan(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the tangent of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The tangent of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)

        sin_x = TrigFunctions._sin_radians(radians)
        cos_x = TrigFunctions._cos_radians(radians)

        return output_type(sin_x / cos_x)

    @staticmethod
    def cotangent(x: float, type_: type | None = None) -> int | float:
        """
        Calculate the cotangent of an angle in degrees.

        Args:
            x: float: The angle in degrees.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The cotangent of the angle as the specified type.
        """
        output_type = TrigFunctions._resolve_type(x, type_)
        radians = TrigFunctions._to_radians(x)

        sin_x = TrigFunctions._sin_radians(radians)
        cos_x = TrigFunctions._cos_radians(radians)

        return output_type(cos_x / sin_x)


    # ----- Pythagorean Theorem -----
    def pythagorean_theorem(a: float, b: float, type_: type | None = None) -> int | float:
        """
        Calculate the hypotenuse of a right triangle given the lengths of the other two sides.

        Args:
            a: float: The length of one side.
            b: float: The length of the other side.
            type_: type | None: The type to return the result as. If None, the type of the input is used.

        Returns:
            int | float: The length of the hypotenuse as the specified type.
        """
        output_type = TrigFunctions._resolve_type(a, type_)
        c_squared = a**2 + b**2
        c = c_squared**0.5
        return output_type(c)


# ----- Misc Functions -----
# Divide and return result as int with remainder
def div_with_modulo(*nums:float) -> tuple[int, int]:

    if not nums:
        return 0 
    if nums[0] == 0:
        return 0, 0
    if 0 in nums[1:]:
        return 0, 0

    div_result = div_all(*nums, type_ = float)

    whole_num, remainder = decimal_to_frac(div_result)


    return whole_num, remainder


# applying discounts
def apply_discount(number:float=0, discount:float=None) -> float:
    """
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

