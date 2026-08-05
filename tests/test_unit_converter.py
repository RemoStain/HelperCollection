from __future__ import annotations

import pytest

from helper_functions.unit_converter import UnitConverter


@pytest.mark.parametrize(
    ("forward", "reverse", "value"),
    [
        (UnitConverter.lb_to_kg, UnitConverter.kg_to_lb, 175.5),
        (UnitConverter.mmhg_to_kpa, UnitConverter.kpa_to_mmhg, 120.0),
        (UnitConverter.ft_to_m, UnitConverter.m_to_ft, 6.25),
        (UnitConverter.kcal_to_kj, UnitConverter.kj_to_kcal, 450.0),
        (UnitConverter.f_to_c, UnitConverter.c_to_f, 72.0),
    ],
)
def test_round_trip_conversions(forward, reverse, value: float) -> None:
    assert reverse(forward(value)) == pytest.approx(value)


@pytest.mark.parametrize(
    ("function", "value", "expected"),
    [
        (UnitConverter.lb_to_kg, 1, 0.45359237),
        (UnitConverter.mmhg_to_kpa, 760, 101.3250144354),
        (UnitConverter.ft_to_m, 1, 0.3048),
        (UnitConverter.kcal_to_kj, 1, 4.184),
        (UnitConverter.f_to_c, 32, 0),
        (UnitConverter.c_to_f, 100, 212),
    ],
)
def test_known_conversion_values(function, value: float, expected: float) -> None:
    assert function(value) == pytest.approx(expected)


@pytest.mark.parametrize(
    "function",
    [
        UnitConverter.lb_to_kg,
        UnitConverter.kg_to_lb,
        UnitConverter.mmhg_to_kpa,
        UnitConverter.kpa_to_mmhg,
        UnitConverter.ft_to_m,
        UnitConverter.m_to_ft,
        UnitConverter.kcal_to_kj,
        UnitConverter.kj_to_kcal,
    ],
)
def test_zero_is_preserved(function) -> None:
    assert function(0) == 0
