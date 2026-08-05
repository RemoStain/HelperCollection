# helper_functions

A lightweight collection of reusable Python helper modules for console applications, mathematical operations, exception logging, source-code inspection, input validation, and unit conversion.

> Status: Early development. Some modules and interfaces may change.

## Features

- Safely prompt for and convert console input.
- Build simple numbered console menus.
- Validate email address formatting.
- Log exceptions and tracebacks to local files.
- Inspect Python files for function and method names.
- Print function docstrings from Python modules.
- Perform arithmetic, fraction, root, rounding, and trigonometric operations.
- Convert common mass, pressure, length, energy, and temperature units.

## Requirements

- Python 3.10 or newer
- No third-party dependencies

The package currently uses only modules from the Python standard library.

## Installation

This project does not currently include packaging metadata such as `pyproject.toml` or `setup.py`. Place the `helper_functions` directory inside your project, or beside the script that will import it.

Example structure:

```text
my_project/
├── helper_functions/
│   ├── __init__.py
│   ├── exception_logging.py
│   ├── help_call.py
│   ├── helpers_and_menu.py
│   ├── math_func.py
│   ├── safe_input.py
│   └── unit_converter.py
└── main.py
```

Then import the required module or function:

```python
from helper_functions.safe_input import safe_input
from helper_functions.unit_converter import UnitConverter
```

## Quick Start

### Safe console input

```python
from helper_functions.safe_input import safe_input

age = safe_input(
    expected_type=int,
    message="Enter your age: ",
    default=18,
)

print(age)
```

Boolean input recognizes values such as `true`, `false`, `yes`, `no`, `1`, and `0`.

### Unit conversion

```python
from helper_functions.unit_converter import UnitConverter

kilograms = UnitConverter.lb_to_kg(10)
celsius = UnitConverter.f_to_c(68)

print(kilograms)
print(celsius)
```

### Mathematical helpers

```python
from helper_functions.math_func import add_all, decimal_to_frac, TrigFunctions

print(add_all(2, 4, 6))
print(decimal_to_frac(0.75))
print(TrigFunctions.sin(30, type_=float))
```

Trigonometric functions accept angles in degrees.

### Exception logging

```python
from helper_functions.exception_logging import log_exception

try:
    result = 10 / 0
except Exception as error:
    log_exception(error, verbose=True)
```

Depending on the selected mode, exception details may be written to `traceback.txt` and `log.txt` in the current working directory.

### Inspecting a Python file

```python
from helper_functions.help_call import get_function_names

names = get_function_names("example.py", display=True)
print(names)
```

## Module Reference

### `safe_input.py`

Provides safer conversion of interactive console input.

| Function | Description |
|---|---|
| `safe_input(expected_type, message=None, default=None, is_password=False, feedback=False)` | Prompts for input and converts it to the requested type. Supports hidden password input, default values, boolean parsing, and basic interruption handling. |

### `helpers_and_menu.py`

Contains console and validation helpers.

| Function | Description |
|---|---|
| `_menu(header="Menu", items=[])` | Displays a numbered menu and returns the selected item. |
| `_validate_email(email)` | Checks whether an email address matches the module's expected format. |
| `_cls()` | Clears the terminal using an ANSI escape sequence. |
| `_generate_dashes(n=0, title=False)` | Generates separator text for menus. |
| `_is_truthy(variable=None)` | Returns whether a value is truthy. |
| `_is_falsy(variable=None)` | Returns whether a value is falsy. |

Names beginning with an underscore should be treated as internal APIs and may change.

### `exception_logging.py`

| Function | Description |
|---|---|
| `log_exception(e, verbose=False)` | Logs an exception summary and optionally writes detailed traceback information. |

### `help_call.py`

| Function | Description |
|---|---|
| `get_function_names(filename, display=False)` | Returns functions and class methods discovered in a Python source file. |
| `print_docstring(filename, func_name="get_function_names")` | Loads a function from a file and prints its docstring. |

### `math_func.py`

Provides mathematical constants and utility functions.

#### Arithmetic

- `add_all(*nums, type_=None)`
- `sub_all(*nums, type_=None)`
- `mult_all(*nums, type_=None)`
- `div_all(*nums, floor=False, type_=None)`
- `exp_all(*nums, type_=None)`
- `div_with_modulo(*nums)`

#### Fractions and rounding

- `reduce_fraction(numerator, denominator)`
- `decimal_to_frac(num)`
- `improper_to_proper_frac(numerator, denominator)`
- `proper_to_improper_frac(whole, numerator, denominator)`
- `rounding(num, decimal=0, type_=None, force=False)`

#### Roots and percentages

- `sq_root(num, root=2, type_=None)`
- `root_n(num, x, type_=None)`
- `apply_discount(number, discount)`

#### Constants and trigonometry

- `describe_math_constant(constant)`
- `TrigFunctions.sin(x, type_=None)`
- `TrigFunctions.cos(x, type_=None)`
- `TrigFunctions.tan(x, type_=None)`
- `TrigFunctions.cosecant(x, type_=None)`
- `TrigFunctions.secant(x, type_=None)`
- `TrigFunctions.cotangent(x, type_=None)`
- `TrigFunctions.pythagorean_theorem(a, b, type_=None)`

### `unit_converter.py`

The `UnitConverter` class supplies static conversion methods.

| Category | Methods |
|---|---|
| Mass | `lb_to_kg`, `kg_to_lb` |
| Pressure | `mmhg_to_kpa`, `kpa_to_mmhg` |
| Length | `ft_to_m`, `m_to_ft` |
| Energy | `kcal_to_kj`, `kj_to_kcal` |
| Temperature | `f_to_c`, `c_to_f` |


## Package Exports

The package's `__init__.py` exposes these modules:

```python
from helper_functions import (
    exception_logging,
    helpers_and_menu,
    help_call,
    math_func,
    safe_input,
    unit_converter,
)
```

## Project Structure

```text

helper_functions/
├── requirements-dev.txt
├── README.md
├── .gitignore
│
├── helper_functions/
│   ├── __init__.py
│   ├── exception_logging.py
│   ├── help_call.py
│   ├── helpers_and_menu.py
│   ├── math_func.py
│   ├── safe_input.py
│   └── unit_converter.py
│
└── tests/
    ├── conftest.py
    ├── test_exception_logging.py
    ├── test_help_call.py
    ├── test_helpers_and_menu.py
    ├── test_math_func.py
    ├── test_package.py
    ├── test_safe_input.py
    └── test_unit_converter.py
```

## Current Limitations

- The project is not yet installable through `pip`..
- Console clearing depends on ANSI escape-sequence support.
- Trigonometric calculations use custom approximations and may not match the precision or edge-case handling of Python's `math` module.
- `unit_converter.py` is marked as work in progress.

## Development

When extending the package:

1. Add type hints and a docstring to public functions.
3. Keep imports compatible with package execution.
5. Update this README when a public interface changes.

## License

No license has been specified. Add a `LICENSE` file and replace this section with the selected license terms before distributing the project.
