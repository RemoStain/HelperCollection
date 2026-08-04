from __future__ import annotations

import sys
from pathlib import Path

import pytest


PACKAGE_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PACKAGE_DIR.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def sample_module(tmp_path: Path) -> Path:
    path = tmp_path / "sample_module.py"
    path.write_text(
        '"""Fixture module."""\n\n'
        'def standalone():\n'
        '    """Standalone documentation."""\n'
        '    return "standalone"\n\n'
        'class Example:\n'
        '    def method(self):\n'
        '        """Method documentation."""\n'
        '        return "method"\n',
        encoding="utf-8",
    )
    return path
