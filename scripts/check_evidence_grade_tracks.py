#!/usr/bin/env python3
"""Lint dual-track evidence grading documentation surface (social-science-track P0).

Documentation-surface checks only — not runtime grading semantics.
Exit 0 pass / 1 fail.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Callable

REPO_ROOT = Path.cwd()
TRACKS = REPO_ROOT / "deep-research" / "references" / "evidence_grade_tracks.md"
HIERARCHY = REPO_ROOT / "deep-research" / "references" / "source_quality_hierarchy.md"
TEMPLATE = REPO_ROOT / "deep-research" / "templates" / "evidence_assessment_template.md"
SVA = REPO_ROOT / "deep-research" / "agents" / "source_verification_agent.md"
PROFILES = REPO_ROOT / "academic-paper" / "references" / "domain_evidence_profiles.md"
CONFIG = REPO_ROOT / "shared" / "social_science_config.md"
STRATEGIST = REPO_ROOT / "academic-paper" / "agents" / "literature_strategist_agent.md"
SPEC = REPO_ROOT / "docs" / "design" / "2026-07-10-dual-track-evidence-grading-spec.md"

TRACK_ENUM = (
    "ebm_design",
    "ss_quantitative",
    "ss_qualitative",
    "humanities",
    "neutral",
)
PROFILE_KEYS = (
    "social_science_qualitative",
    "social_science_quantitative",
    "communication_mixed",
    "general_social_science",
    "humanities_interpretive",
    "cs_ml",
    "unknown_user_defined",
)


def _read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def check_t1() -> list[str]:
    """Tracks doc exists with enum + profile→track table + clamps."""
    f: list[str] = []
    t = _read(TRACKS)
    if not t:
        return ["T1: evidence_grade_tracks.md missing"]
    for tr in TRACK_ENUM:
        if f"`{tr}`" not in t and tr not in t:
            f.append(f"T1: tracks doc missing track token '{tr}'")
    for pk in PROFILE_KEYS:
        if pk not in t:
            f.append(f"T1: tracks doc missing profile key '{pk}'")
    if "design_level_code" not in t and "Design code" not in t:
        f.append("T1: tracks doc must mention design_level_code / Design code")
    if "Integrity floor" not in t and "integrity floor" not in t.lower():
        f.append("T1: tracks doc missing integrity floor language")
    if "ss_qualitative" in t and "VI" not in t:
        f.append("T1: tracks doc should mention Level VI clamp for qualitative")
    if "Advisory only" not in t and "advisory only" not in t.lower():
        f.append("T1: tracks doc missing advisory-only statement")
    return f


def check_t2() -> list[str]:
    """Hierarchy dual-track pointer; no Weight authority labels; Evidence fitness present."""
    f: list[str] = []
    t = _read(HIERARCHY)
    if not t:
        return ["T2: source_quality_hierarchy.md missing"]
    if "evidence_grade_tracks.md" not in t:
        f.append("T2: hierarchy missing pointer to evidence_grade_tracks.md")
    if "Dual-track" not in t and "dual-track" not in t:
        f.append("T2: hierarchy missing dual-track language")
    if "Evidence fitness" not in t:
        f.append("T2: hierarchy missing 'Evidence fitness' criterion name")
    # Forbidden: authoritative Weight column / labels on levels
    if re.search(r"\*\*Weight\*\*:\s*(Highest|Very High|High|Moderate|Lowest)", t):
        f.append("T2: hierarchy still has **Weight**: strength labels (design codes must not weight)")
    if re.search(r"^\|\s*Level\s*\|\s*Evidence Type\s*\|\s*Weight\s*\|", t, re.M):
        f.append("T2: hierarchy still has Level|Evidence Type|Weight table header")
    return f


def check_t3() -> list[str]:
    """Template has track + design code + evidence fitness fields."""
    f: list[str] = []
    t = _read(TEMPLATE)
    if not t:
        return ["T3: evidence_assessment_template.md missing"]
    for token in (
        "Evidence grade track",
        "Claim class",
        "Design level code",
        "Evidence fitness",
        "design codes only" if False else "descriptive",  # soft
    ):
        if token == "descriptive":
            if "descriptive" not in t.lower():
                f.append("T3: template should state design code is descriptive")
            continue
        if token not in t:
            f.append(f"T3: template missing '{token}'")
    if "NO-TRACK-NEUTRAL" not in t:
        f.append("T3: template missing [NO-TRACK-NEUTRAL] advisory mention")
    return f


def check_t4() -> list[str]:
    """source_verification_agent: no Weight table; points at tracks; track resolution."""
    f: list[str] = []
    t = _read(SVA)
    if not t:
        return ["T4: source_verification_agent.md missing"]
    if "evidence_grade_tracks.md" not in t:
        f.append("T4: source_verification_agent missing evidence_grade_tracks.md reference")
    if "NO-TRACK-NEUTRAL" not in t:
        f.append("T4: source_verification_agent missing [NO-TRACK-NEUTRAL]")
    if re.search(r"\|\s*Level\s*\|\s*Evidence Type\s*\|\s*Weight\s*\|", t):
        f.append("T4: source_verification_agent still has Weight authority table")
    if re.search(r"\|\s*I\s*\|.*\|\s*Highest\s*\|", t):
        f.append("T4: source_verification_agent still maps Level I → Highest weight")
    if "Design code" not in t and "design_level_code" not in t and "Design codes" not in t:
        f.append("T4: source_verification_agent must discuss design codes")
    if "Track resolution" not in t and "track resolution" not in t.lower():
        f.append("T4: source_verification_agent missing track resolution procedure")
    return f


def check_t5() -> list[str]:
    """profiles + config mirror profile→track table; #246 residual note kept for C4."""
    f: list[str] = []
    p = _read(PROFILES)
    c = _read(CONFIG)
    if not p:
        f.append("T5: domain_evidence_profiles.md missing")
    else:
        if "Advisory only" not in p:
            f.append("T5: profiles doc missing Advisory only (also required by #259 C4)")
        if "#246" not in p:
            f.append("T5: profiles doc missing #246 residual mention (also required by #259 C4)")
        if "ss_qualitative" not in p or "EvidenceGradeTrack" not in p:
            f.append("T5: profiles doc missing dual-track derivation table")
        for pk in ("social_science_qualitative", "social_science_quantitative", "unknown_user_defined"):
            if pk not in p:
                f.append(f"T5: profiles doc missing profile '{pk}' in track table region")
    if not c:
        f.append("T5: social_science_config.md missing")
    else:
        if "Evidence grade track" not in c and "evidence_grade_track" not in c:
            f.append("T5: social_science_config.md missing Evidence grade track section")
        if "ss_qualitative" not in c or "ss_quantitative" not in c:
            f.append("T5: social_science_config.md missing ss_* track tokens")
        if "evidence_grade_tracks.md" not in c:
            f.append("T5: social_science_config.md missing pointer to evidence_grade_tracks.md")
    return f


def check_t6() -> list[str]:
    """literature_strategist derives track; no design-code ranking under ss_*."""
    f: list[str] = []
    t = _read(STRATEGIST)
    if not t:
        return ["T6: literature_strategist_agent.md missing"]
    if "evidence_grade_track" not in t and "Evidence grade track" not in t:
        f.append("T6: literature_strategist missing evidence grade track derivation")
    if "evidence_grade_tracks.md" not in t:
        f.append("T6: literature_strategist missing evidence_grade_tracks.md pointer")
    if "design-code" not in t.lower() and "design code" not in t.lower():
        f.append("T6: literature_strategist should forbid design-code ranking under ss_* / humanities")
    return f


def check_t7() -> list[str]:
    """Spec file present with load-bearing invariants."""
    f: list[str] = []
    t = _read(SPEC)
    if not t:
        return ["T7: dual-track evidence grading spec missing"]
    if "EvidenceGradeTrack" not in t:
        f.append("T7: spec missing EvidenceGradeTrack")
    if "Advisory only" not in t and "advisory only" not in t.lower():
        f.append("T7: spec missing advisory-only discipline")
    if "design code" not in t.lower() and "DesignLevelCode" not in t:
        f.append("T7: spec missing design-code / DesignLevelCode distinction")
    return f



CHECKS: list[tuple[str, Callable[[], list[str]]]] = [
    ("T1", check_t1),
    ("T2", check_t2),
    ("T3", check_t3),
    ("T4", check_t4),
    ("T5", check_t5),
    ("T6", check_t6),
    ("T7", check_t7),
]


def main() -> int:
    all_failures: list[str] = []
    for name, fn in CHECKS:
        try:
            all_failures.extend(fn())
        except Exception as exc:  # pragma: no cover
            all_failures.append(f"{name}: check raised {type(exc).__name__}: {exc}")
    if all_failures:
        print("Evidence grade tracks lint FAILED:", file=sys.stderr)
        for x in all_failures:
            print(f"  - {x}", file=sys.stderr)
        return 1
    print("Evidence grade tracks lint OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
