from __future__ import annotations

import logging
from pathlib import Path
from unittest.mock import Mock

from HelperFunctions import exception_logging


def _captured_exception() -> Exception:
    try:
        raise ValueError("broken value")
    except ValueError as error:
        return error


def test_non_verbose_logs_summary_only(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)
    error_log = Mock()
    monkeypatch.setattr(logging, "error", error_log)
    monkeypatch.setattr(exception_logging.time, "strftime", lambda _fmt: "2026-08-04 08:00:00")

    exception_logging.log_exception(_captured_exception(), verbose=False)

    error_log.assert_called_once()
    arguments = error_log.call_args.args
    assert "2026-08-04 08:00:00" in arguments[0]
    assert arguments[1] == "ValueError"
    assert arguments[2] == ("broken value",)
    assert not (tmp_path / "log.txt").exists()


def test_verbose_writes_explanation_file(monkeypatch, tmp_path: Path, capsys) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(logging, "error", Mock())
    monkeypatch.setattr(exception_logging.time, "strftime", lambda _fmt: "2026-08-04 08:00:00")
    monkeypatch.setattr(exception_logging.traceback, "format_exc", lambda: "TRACEBACK TEXT")

    exception_logging.log_exception(_captured_exception(), verbose=True)

    log_text = (tmp_path / "log.txt").read_text(encoding="utf-8")
    assert "2026-08-04 08:00:00" in log_text
    assert "ValueError" in log_text
    assert "broken value" in log_text
    assert "TRACEBACK TEXT" in log_text
    assert "Exception logged to log.txt" in capsys.readouterr().out
