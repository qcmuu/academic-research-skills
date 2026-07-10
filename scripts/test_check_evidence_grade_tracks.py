#!/usr/bin/env python3
"""Mutation tests for check_evidence_grade_tracks.py."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
CHECKER = REPO / "scripts" / "check_evidence_grade_tracks.py"

# Paths relative to a fixture repo root that mirror the real layout
MIRROR_PATHS = [
    "deep-research/references/evidence_grade_tracks.md",
    "deep-research/references/source_quality_hierarchy.md",
    "deep-research/templates/evidence_assessment_template.md",
    "deep-research/agents/source_verification_agent.md",
    "academic-paper/references/domain_evidence_profiles.md",
    "shared/social_science_config.md",
    "academic-paper/agents/literature_strategist_agent.md",
    "docs/design/2026-07-10-dual-track-evidence-grading-spec.md",
]


def _clone_surface(tmp: Path) -> Path:
    root = tmp / "repo"
    for rel in MIRROR_PATHS:
        src = REPO / rel
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return root


def _run(cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER)],
        cwd=cwd,
        capture_output=True,
        text=True,
    )


def test_positive_clean_tree_passes(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    # Checker uses Path.cwd() — run from fixture root after copying checker? No:
    # checker path is absolute; it uses cwd for REPO_ROOT. Good.
    r = _run(root)
    assert r.returncode == 0, r.stderr + r.stdout


def test_neg_t1_drop_track_token(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "deep-research/references/evidence_grade_tracks.md"
    p.write_text(p.read_text(encoding="utf-8").replace("ss_qualitative", "SS_QUAL_REMOVED"), encoding="utf-8")
    r = _run(root)
    assert r.returncode == 1
    assert "T1" in r.stderr


def test_neg_t2_reintroduce_weight_label(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "deep-research/references/source_quality_hierarchy.md"
    text = p.read_text(encoding="utf-8")
    p.write_text(text + "\n**Weight**: Highest\n", encoding="utf-8")
    r = _run(root)
    assert r.returncode == 1
    assert "T2" in r.stderr


def test_neg_t3_drop_fitness(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "deep-research/templates/evidence_assessment_template.md"
    p.write_text(p.read_text(encoding="utf-8").replace("Evidence fitness", "EVIDENCE_LEVEL_OLD"), encoding="utf-8")
    r = _run(root)
    assert r.returncode == 1
    assert "T3" in r.stderr


def test_neg_t4_weight_table(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "deep-research/agents/source_verification_agent.md"
    text = p.read_text(encoding="utf-8")
    p.write_text(
        text + "\n| Level | Evidence Type | Weight |\n| I | x | Highest |\n",
        encoding="utf-8",
    )
    r = _run(root)
    assert r.returncode == 1
    assert "T4" in r.stderr


def test_neg_t5_drop_246(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "academic-paper/references/domain_evidence_profiles.md"
    p.write_text(p.read_text(encoding="utf-8").replace("#246", "#xxx"), encoding="utf-8")
    r = _run(root)
    assert r.returncode == 1
    assert "T5" in r.stderr


def test_neg_t6_drop_track_derivation(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    p = root / "academic-paper/agents/literature_strategist_agent.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace("Evidence grade track", "REMOVED")
    text = text.replace("evidence_grade_track", "removed")
    text = text.replace("evidence_grade_tracks.md", "removed.md")
    p.write_text(text, encoding="utf-8")
    r = _run(root)
    assert r.returncode == 1
    assert "T6" in r.stderr


def test_neg_t7_missing_spec(tmp_path: Path) -> None:
    root = _clone_surface(tmp_path)
    (root / "docs/design/2026-07-10-dual-track-evidence-grading-spec.md").unlink()
    r = _run(root)
    assert r.returncode == 1
    assert "T7" in r.stderr


