from __future__ import annotations

from pathlib import Path

import pytest

from helper_functions import help_call


def test_get_function_names_finds_functions_and_methods(sample_module: Path) -> None:
    assert help_call.get_function_names(str(sample_module)) == [
        "standalone",
        "Example.method",
    ]


def test_get_function_names_display_output(sample_module: Path, capsys) -> None:
    names = help_call.get_function_names(str(sample_module), display=True)
    output = capsys.readouterr().out
    assert names == ["standalone", "Example.method"]
    assert f"Function names found in {sample_module}:" in output
    assert "standalone" in output
    assert "Example.method" in output


def test_get_function_names_missing_file_raises(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        help_call.get_function_names(str(tmp_path / "missing.py"))


def test_load_func_loads_named_function(sample_module: Path) -> None:
    loaded = help_call.load_func(
        path_=str(sample_module),
        filename=sample_module.stem,
        func_name="standalone",
    )
    assert loaded() == "standalone"


def test_print_docstring(sample_module: Path, capsys) -> None:
    help_call.print_docstring(str(sample_module), "standalone")
    assert capsys.readouterr().out.strip() == "Standalone documentation."
