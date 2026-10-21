"""Repo-root pytest configuration.

Adds platform-capability helpers so the POSIX-oriented test suite can run on
Windows checkouts without silently turning environment limitations into
false failures. Tests that genuinely require a POSIX primitive (symlink
creation, ``/bin/sh`` launchers, ``os.geteuid``, direct execution of a
``.py`` file) skip with an explicit reason instead of erroring.
"""

from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest


def _probe_symlink() -> bool:
    """Return True if this process may create filesystem symlinks."""
    if not hasattr(os, "symlink"):
        return False
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "target.txt"
        link = Path(tmp) / "link.txt"
        target.write_text("x", encoding="utf-8")
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            return False
        return True


def _probe_posix_shell() -> bool:
    """Return True if a POSIX shell interpreter is available by path."""
    return os.name != "nt" and Path("/bin/sh").exists()


CAN_SYMLINK = _probe_symlink()
CAN_RUN_POSIX_SHELL = _probe_posix_shell()


def _default_text_io_to_utf8() -> None:
    """Make bare `read_text()` / `write_text()` default to UTF-8 in tests.

    The fixture corpus (agent prompts, schemas, changelogs) contains em
    dashes, curly quotes and CJK. On a POSIX host the locale codec is UTF-8
    and bare calls work; on a Windows box with a GBK ANSI code page they
    raise `UnicodeDecodeError` and the suite reports dozens of failures that
    are entirely environmental. CI is UTF-8, so pinning the test-side default
    to UTF-8 makes local runs measure the same thing CI measures.

    Only the *default* is changed: any call that passes `encoding=` keeps its
    own choice, and production modules are untouched (they already specify
    UTF-8 explicitly where it matters).
    """
    if sys.getdefaultencoding() == "utf-8" and _locale_is_utf8():
        return

    original_read = Path.read_text
    original_write = Path.write_text

    def read_text(self, encoding=None, errors=None, *args, **kwargs):
        return original_read(
            self, encoding=encoding or "utf-8", errors=errors, *args, **kwargs
        )

    def write_text(self, data, encoding=None, errors=None, *args, **kwargs):
        return original_write(
            self, data, encoding=encoding or "utf-8", errors=errors, *args, **kwargs
        )

    Path.read_text = read_text
    Path.write_text = write_text


def _patch_subprocess_text_defaults() -> None:
    """Default `text=True` subprocess calls to UTF-8 on both pipes.

    Many assertions compare child stdout against UTF-8 fixture text (em
    dashes, CJK). Without this, a GBK host decodes the child's bytes with
    GBK and raises `UnicodeDecodeError` inside subprocess' reader thread,
    which surfaces as a confusing `None` stdout rather than a decode error.
    An explicit `encoding=` argument on a call still takes precedence.
    """
    import subprocess

    original_run = subprocess.run
    original_popen = subprocess.Popen

    def _apply(kwargs):
        if kwargs.get("text") or kwargs.get("universal_newlines"):
            kwargs.setdefault("encoding", "utf-8")
        return kwargs

    def run(*args, **kwargs):
        return original_run(*args, **_apply(kwargs))

    class Popen(original_popen):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **_apply(kwargs))

    subprocess.run = run
    subprocess.Popen = Popen


def _locale_is_utf8() -> bool:
    import locale

    try:
        return locale.getencoding().lower().replace("-", "").startswith("utf8")
    except AttributeError:  # Python < 3.11
        return locale.getpreferredencoding(False).lower().replace("-", "").startswith("utf8")


def pytest_configure(config: pytest.Config) -> None:
    _default_text_io_to_utf8()
    # Several tests pipe non-UTF-8-safe text (U+2028, CJK) into a child
    # interpreter. Children inherit the parent's environment, and on Windows
    # that means a GBK code page for stdin/stdout. CI runs on Linux where the
    # child default is already UTF-8, so asking children for UTF-8 mode makes
    # the local run measure the same contract CI measures.
    os.environ["PYTHONUTF8"] = "1"
    os.environ["PYTHONIOENCODING"] = "utf-8"

    # Subprocess calls in the suite mostly pass `text=True` without an
    # encoding, so they decode child output with the parent's locale codec.
    # Pin those defaults too; `encoding=` on an individual call still wins.
    if _locale_is_utf8():
        return
    _patch_subprocess_text_defaults()
    config.addinivalue_line(
        "markers",
        "requires_symlink: test needs filesystem symlink support "
        "(Developer Mode / seCreateSymbolicLinkPrivilege on Windows)",
    )
    config.addinivalue_line(
        "markers",
        "requires_posix_shell: test needs /bin/sh (POSIX host)",
    )


requires_symlink = pytest.mark.skipif(
    not CAN_SYMLINK,
    reason="host cannot create filesystem symlinks (Windows without "
    "Developer Mode / symlink privilege)",
)

requires_posix_shell = pytest.mark.skipif(
    not CAN_RUN_POSIX_SHELL,
    reason="test exercises a POSIX shell launcher; /bin/sh is unavailable",
)
