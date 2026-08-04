from __future__ import annotations

import math

import pytest

from HelperFunctions import math_func as mf


def test_constant_collections_have_matching_keys() -> None:
    assert mf.math_constant.keys() == mf.math_descriptions.keys()


def test_describe_known_constant() -> None:
    assert "circumference" in mf.describe_math_constant("pi")


def test_describe_unknown_constant_raises() -> None:
    with pytest.raises(ValueError, match="not a listed mathematical constant"):
        mf.describe_math_constant("unknown")


@pytest.mark.parametrize(
    ("function", "values", "expected"),
    [
        (mf.add_all, (1, 2, 3), 6),
        (mf.sub_all, (10, 3, 2), 5),
        (mf.mult_all, (2, 3, 4), 24),
        (mf.div_all, (100.0, 2, 5), 10.0),
        (mf.exp_all, (2, 3, 2), 64),
    ],
)
def test_basic_arithmetic(function, values, expected) -> None:
    assert function(*values) == expected


@pytest.mark.parametrize("function", [mf.add_all, mf.sub_all, mf.mult_all, mf.exp_all])
def test_arithmetic_requiring_values_raises(function) -> None:
    with pytest.raises(ValueError):
        function()


def test_arithmetic_type_override() -> None:
    assert mf.add_all(1.2, 2.7, type_=int) == 3
    assert mf.div_all(5, 2, type_=float) == pytest.approx(2.5)
    assert isinstance(mf.exp_all(2, 3, type_=float), float)


def test_division_floor_option() -> None:
    assert mf.div_all(7.0, 2, floor=True) == 3.0


def test_division_defensive_zero_behaviour() -> None:
    assert mf.div_all() == 0
    assert mf.div_all(0, 5) == 0
    assert mf.div_all(10, 0) == 10


def test_multiplication_by_zero() -> None:
    assert mf.mult_all(10, 0, 3) == 0


@pytest.mark.known_bug
@pytest.mark.xfail(reason="mult_all returns the complete args tuple for one value")
def test_single_value_multiplication_returns_value() -> None:
    assert mf.mult_all(5) == 5


def test_exponent_zero_behaviour() -> None:
    assert mf.exp_all(5, 0) == 1


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [
        (10, 20, (1, 2)),
        (-10, 20, (-1, 2)),
        (10, -20, (-1, 2)),
        (-10, -20, (1, 2)),
        (0, 999, (0, 1)),
    ],
)
def test_reduce_fraction(numerator: int, denominator: int, expected) -> None:
    assert mf.reduce_fraction(numerator, denominator) == expected


def test_reduce_fraction_zero_denominator_raises() -> None:
    with pytest.raises(ZeroDivisionError):
        mf.reduce_fraction(1, 0)


@pytest.mark.parametrize(
    ("number", "expected"),
    [(0.0, (0, 1)), (0.5, (1, 2)), (0.75, (3, 4)), (10.1, (101, 10))],
)
def test_decimal_to_fraction(number: float, expected) -> None:
    assert mf.decimal_to_frac(number) == expected


@pytest.mark.known_bug
@pytest.mark.xfail(reason="scientific notation is not handled by decimal_to_frac")
def test_decimal_to_fraction_scientific_notation() -> None:
    assert mf.decimal_to_frac(1e-05) == (1, 100000)


@pytest.mark.parametrize(
    ("numerator", "denominator", "expected"),
    [(1, 2, (0, 1, 2)), (2, 2, (1, 0, 1)), (21, 2, (10, 1, 2))],
)
def test_improper_to_proper_fraction(numerator, denominator, expected) -> None:
    assert mf.improper_to_proper_frac(numerator, denominator) == expected


def test_improper_fraction_with_zero_denominator() -> None:
    assert mf.improper_to_proper_frac(1, 0) == (0, 0, 0)


def test_proper_to_improper_fraction() -> None:
    assert mf.proper_to_improper_frac(10, 1, 2) == 21
    assert mf.proper_to_improper_frac(0, 1, 2) == (1, 2)
    assert mf.proper_to_improper_frac(1, 1, 0) == (0, 0)


@pytest.mark.parametrize(
    ("number", "decimal", "force", "expected"),
    [
        (1.25, 1, None, 1.2),
        (1.29, 1, "down", 1.2),
        (-1.29, 1, "down", -1.2),
        (-1.21, 1, "truedown", -1.3),
    ],
)
def test_rounding_modes(number, decimal, force, expected) -> None:
    assert mf.rounding(number, decimal, type_=float, force=force) == pytest.approx(expected)


def test_rounding_zero() -> None:
    assert mf.rounding(0.0, 3) == 0


@pytest.mark.parametrize(
    ("function", "args", "expected"),
    [
        (mf.sq_root, (9.0,), 3.0),
        (mf.sq_root, (27.0, 3), 3.0),
        (mf.root_n, (16.0, 4), 2.0),
    ],
)
def test_root_functions(function, args, expected) -> None:
    assert function(*args, type_=float) == pytest.approx(expected)


@pytest.mark.parametrize("function,args", [(mf.sq_root, (4, 0)), (mf.root_n, (4, 0))])
def test_zero_root_raises(function, args) -> None:
    with pytest.raises(ValueError):
        function(*args)


def test_root_of_zero() -> None:
    assert mf.sq_root(0) == 0
    assert mf.root_n(0, 3) == 0


def test_sine_zero() -> None:
    assert mf.TrigFunctions.sin(0, type_=float) == 0.0


@pytest.mark.known_bug
@pytest.mark.xfail(reason="Taylor-series terms use exponentiation instead of factorials")
@pytest.mark.parametrize(("angle", "expected"), [(30, 0.5), (90, 1.0), (-30, -0.5)])
def test_sine_known_angles(angle: float, expected: float) -> None:
    assert mf.TrigFunctions.sin(angle, type_=float) == pytest.approx(expected, abs=1e-8)


def test_cosine_zero() -> None:
    assert mf.TrigFunctions.cos(0, type_=float) == 1.0


@pytest.mark.known_bug
@pytest.mark.xfail(reason="Taylor-series terms use exponentiation instead of factorials")
@pytest.mark.parametrize(("angle", "expected"), [(60, 0.5), (90, 0.0), (180, -1.0)])
def test_cosine_known_angles(angle: float, expected: float) -> None:
    assert mf.TrigFunctions.cos(angle, type_=float) == pytest.approx(expected, abs=1e-7)


@pytest.mark.known_bug
@pytest.mark.xfail(reason="Reciprocal trig functions depend on inaccurate sine and cosine series")
def test_tangent_and_reciprocal_functions() -> None:
    assert mf.TrigFunctions.tan(45, type_=float) == pytest.approx(1.0, abs=1e-8)
    assert mf.TrigFunctions.cosecant(30, type_=float) == pytest.approx(2.0, abs=1e-8)
    assert mf.TrigFunctions.secant(60, type_=float) == pytest.approx(2.0, abs=1e-7)
    assert mf.TrigFunctions.cotangent(45, type_=float) == pytest.approx(1.0, abs=1e-8)


def test_trig_default_type_matches_input() -> None:
    assert isinstance(mf.TrigFunctions.sin(30.0), float)
    assert isinstance(mf.TrigFunctions.sin(30), int)


def test_pythagorean_theorem() -> None:
    assert mf.TrigFunctions.pythagorean_theorem(3.0, 4.0) == pytest.approx(5.0)
    assert mf.TrigFunctions.pythagorean_theorem(3, 4) == 5


def test_div_with_modulo_current_fraction_result() -> None:
    assert mf.div_with_modulo(21, 10) == (21, 10)
    assert mf.div_with_modulo(0, 1) == (0, 0)
    assert mf.div_with_modulo(1, 0) == (0, 0)


def test_apply_discount() -> None:
    assert mf.apply_discount(100, 25) == pytest.approx(75)
    assert mf.apply_discount(100, 0) == 100
    assert mf.apply_discount(100, -10) == 100
