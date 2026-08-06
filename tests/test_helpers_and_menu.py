from __future__ import annotations

from unittest.mock import Mock

import pytest

from helper_functions import helpers_and_menu as helpers


@pytest.mark.parametrize("value", [None, False, 0, 0.0, "", [], {}, set()])
def test_is_falsy(value) -> None:
    assert helpers.is_falsy(value) is True
    assert helpers.is_truthy(value) is False


@pytest.mark.parametrize("value", [True, 1, -1, "value", [0], {"x": 0}])
def test_is_truthy(value) -> None:
    assert helpers.is_truthy(value) is True
    assert helpers.is_falsy(value) is False


def test_cls_prints_ansi_clear_sequence(capsys) -> None:
    assert helpers.cls() is None
    assert capsys.readouterr().out == "\x1b[H\x1b[J"


@pytest.mark.parametrize(
    ("number", "expected"),
    [(1, "-----------"), (9, "-----------"), (10, "----------"), (999, "---------"), (999999999999, "An error occurred: too many items"), (1.4, "---------")],
)
def test_generate_dashes_for_menu_numbers(number: int, expected: str) -> None:
    assert helpers.generate_dashes(number) == expected


def test_generate_dashes_for_title() -> None:
    assert helpers.generate_dashes(5, title=True) == "-----"


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("person@example.com", True),
        ("a@b.co", True),
        ("person.example.com", False),
        ("person@example", False),
        ("", False),
    ],
)
def test_validate_email(email: str, expected: bool) -> None:
    assert helpers.validate_email(email) is expected


def test_menu_returns_only_item_without_prompt(monkeypatch, capsys) -> None:
    prompt = Mock(side_effect=AssertionError("safe_input should not be called"))
    monkeypatch.setattr(helpers, "safe_input", prompt)
    assert helpers.menu("Choose", ["only"]) == "only"
    assert "Only 1 option available: only" in capsys.readouterr().out


def test_menu_returns_selected_item(monkeypatch) -> None:
    monkeypatch.setattr(helpers, "safe_input", lambda *_args, **_kwargs: 2)
    assert helpers.menu("Choose", ["first", "second", "third"]) == "second"


def test_menu_returns_none_for_exit_value(monkeypatch) -> None:
    monkeypatch.setattr(helpers, "safe_input", lambda *_args, **_kwargs: 0)
    assert helpers.menu(items=["first", "second", "third"]) is None


def test_menu_retries_after_out_of_range_choice(monkeypatch) -> None:
    responses = iter([99, 1])
    monkeypatch.setattr(helpers, "safe_input", lambda *_args, **_kwargs: next(responses))
    clear = Mock()
    monkeypatch.setattr(helpers, "cls", clear)
    assert helpers.menu(items=["first", "second", "third"]) == "first"
    clear.assert_called_once_with()
