from __future__ import annotations

import helper_functions


def test_package_exports_expected_modules() -> None:
    assert helper_functions.__all__ == [
        "exception_logging",
        "helpers_and_menu",
        "help_call",
        "math_func",
        "safe_input",
        "unit_converter",
        # "complex_math",
    ]


def test_exported_modules_are_importable_attributes() -> None:
    for name in helper_functions.__all__:
        assert getattr(helper_functions, name).__name__.endswith(name)
