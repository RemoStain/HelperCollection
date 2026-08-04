from __future__ import annotations

import HelperFunctions


def test_package_exports_expected_modules() -> None:
    assert HelperFunctions.__all__ == [
        "exception_logging",
        "helpers_and_menu",
        "help_call",
        "math_func",
        "safe_input",
        "unit_converter",
    ]


def test_exported_modules_are_importable_attributes() -> None:
    for name in HelperFunctions.__all__:
        assert getattr(HelperFunctions, name).__name__.endswith(name)
