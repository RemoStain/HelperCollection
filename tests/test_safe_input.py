from __future__ import annotations

from unittest.mock import Mock

import pytest

from helper_functions import safe_input as module


@pytest.mark.parametrize(
    ("expected_type", "raw", "expected"),
    [
        (int, "42", 42),
        (float, "3.5", 3.5),
        (complex, "2+3j", 2 + 3j),
        (str, "text", "text"),
        (list, "abc", ["a", "b", "c"]),
        (tuple, "ab", ("a", "b")),
        (set, "aba", {"a", "b"}),
        (frozenset, "aba", frozenset({"a", "b"})),
    ],
)
def test_converts_supported_values(monkeypatch, expected_type, raw, expected) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: raw)
    assert module.safe_input(expected_type, "Prompt: ") == expected


@pytest.mark.parametrize("raw", ["true", "TRUE", "1", "yes", "Y"])
def test_boolean_true_values(monkeypatch, raw: str) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: raw)
    assert module.safe_input(bool) is True


@pytest.mark.parametrize("raw", ["false", "FALSE", "0", "no", "N"])
def test_boolean_false_values(monkeypatch, raw: str) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: raw)
    assert module.safe_input(bool) is False


def test_empty_string_uses_default(monkeypatch) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "")
    assert module.safe_input(str, default="Guest") == "Guest"


def test_invalid_value_uses_default_and_prints_message(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "not-an-int")
    assert module.safe_input(int, default=7) == 7
    assert "Using default value: 7" in capsys.readouterr().out


def test_invalid_value_retries_without_default(monkeypatch) -> None:
    responses = iter(["bad", "12"])
    monkeypatch.setattr("builtins.input", lambda _prompt: next(responses))
    assert module.safe_input(int) == 12


def test_feedback_prints_conversion_error(monkeypatch, capsys) -> None:
    monkeypatch.setattr("builtins.input", lambda _prompt: "bad")
    assert module.safe_input(int, default=5, feedback=True) == 5
    assert "Error Trace:" in capsys.readouterr().out


def test_password_input_uses_getpass(monkeypatch) -> None:
    getpass = Mock(return_value="secret")
    ordinary_input = Mock(side_effect=AssertionError("input() should not be called"))
    monkeypatch.setattr(module, "getpass", getpass)
    monkeypatch.setattr("builtins.input", ordinary_input)

    assert module.safe_input(str, "Password: ", is_password=True) == "secret"
    getpass.assert_called_once_with("Password: ")


@pytest.mark.parametrize(
    ("expected_type", "expected"),
    [
        (int, 0),
        (float, 0.0),
        (complex, 0j),
        (bool, False),
        (str, ""),
        (list, []),
        (tuple, ()),
        (set, ()),
        (frozenset, ()),
        (dict, {}),
    ],
)
def test_keyboard_interrupt_returns_zero_equivalent(
    monkeypatch, expected_type, expected
) -> None:
    monkeypatch.setattr(
        "builtins.input", lambda _prompt: (_ for _ in ()).throw(KeyboardInterrupt())
    )
    assert module.safe_input(expected_type) == expected


def test_eof_returns_zero_equivalent(monkeypatch) -> None:
    monkeypatch.setattr(
        "builtins.input", lambda _prompt: (_ for _ in ()).throw(EOFError())
    )
    assert module.safe_input(int) == 0
