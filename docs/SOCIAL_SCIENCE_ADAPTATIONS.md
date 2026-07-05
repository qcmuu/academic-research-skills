# Social Science Adaptations — Change Log

> This branch (`social-science-track`) adapts the ARS suite to better serve **social sciences**:
> sociology / anthropology, political science & public administration, economics & management,
> and communication / journalism. Chinese social-science ecology (CNKI / GB/T 7714 / CSSCI) is a
> secondary priority.
>
> **Strategy: layer, don't overwrite.** New profiles and reference files are preferred over edits
> to upstream agent prose, so this branch stays rebase-friendly against the active upstream
> (v3.15.0+). Where an upstream file MUST be edited, the entry below is tagged `[EDIT]` and notes
> the upstream line anchors at the time of edit; new files are tagged `[NEW]`.
>
> The central config that downstream stages reference is [`shared/social_science_config.md`](../shared/social_science_config.md).

## Target disciplines & defaults

| Discipline cluster | Paradigm lean | Default evidence profile | Default citation |
|---|---|---|---|
| Sociology (qualitative strand) / Anthropology | Interpretive | `social_science_qualitative` | APA 7 / Chicago Notes |
| Sociology (quantitative) / Economics / Management | Positivist, causal-inference | `social_science_quantitative` | APA 7 / Harvard |
| Political science & public admin | Mixed | per-method | APSA / Chicago |
| Communication / journalism | Mixed, applied | `communication_mixed` | APA 7 |

## Stage status

| Stage | Scope | Status |
|---|---|---|
| 0 | Branch + config hub + this log | ✅ done |
| 1 | Domain evidence profile refinement | ✅ done |
| 2 | Reference content (journals, methods, EQUATOR, theory) | ✅ done |
| 3 | Database search protocols (SSRN/JSTOR/WoS/Scopus) | ⏳ pending |
| 4 | Citation formats (APSA / Harvard / GB/T 7714) | ⏳ pending |
| 5 | Bias tools (MMAT/CASP/JBI/CERQual) + qualitative synthesis | ⏳ pending |
| 6 | Reflexivity / positionality advisory agent | ⏳ pending |
| 7 | Reviewer discipline calibration | ⏳ pending |
| 8 | Chinese social-science ecology (CNKI / CSSCI) | ⏳ pending |

## Change ledger

Format: `[STAGE] [NEW|EDIT] path — what changed`.

### Stage 0
- `[NEW] docs/SOCIAL_SCIENCE_ADAPTATIONS.md` — this file.
- `[NEW] shared/social_science_config.md` — central config hub for downstream stages.

### Stage 1 — Domain evidence profile refinement (4 → 7 ship-ready enum)
- `[EDIT] academic-paper/references/domain_evidence_profiles.md` — table 4→7 rows: added `social_science_qualitative`, `social_science_quantitative`, `communication_mixed`; retained `general_social_science` as coarse fallback; updated carry-forward folds.
- `[EDIT] scripts/check_domain_evidence_profile.py` — `SHIP_ENUM` 4→7; C2 error message + C3 keyword de-hardcoded from "4".
- `[EDIT] academic-paper/agents/intake_agent.md` Step 12 — choice menu 4→7 + social-science default-suggestion guidance.
- `[EDIT] academic-paper/agents/literature_strategist_agent.md` — profile→discipline map (7 rows); resolution block "4 enum"→"7 enum"; pseudocode comment; decision-tree admit-path annotations; corpus-ratio loosen prose — all three new profiles covered.
- **Verified:** `python scripts/check_domain_evidence_profile.py` → OK; `pytest scripts/test_check_domain_evidence_profile.py` → 24 passed.

### Stage 2 — Reference content expansion (pure overlay, zero coupling)
- `[EDIT] academic-paper-reviewer/references/top_journals_by_field.md` — expanded Sociology + Political Science; added Anthropology, Economics, Communication/Journalism sections.
- `[EDIT] deep-research/references/methodology_patterns.md` — added Pattern 11 (Ethnography), 12 (Grounded Theory), 13 (Action Research), 14 (Discourse/Content Analysis), 15 (QCA); extended decision tree.
- `[EDIT] deep-research/references/equator_reporting_guidelines.md` — added SRQR (5a), ENTREQ (5b), CHEERS 2022 (5c) condensed checklists.
- `[EDIT] deep-research/agents/research_architect_agent.md` — expanded Reporting Standards table (SRQR/ENTREQ/CHEERS/GRAMMS); added §9 Theoretical Framework Selection (10 candidate perspectives + coherence rule).
- **Verified:** `check_domain_evidence_profile.py` OK; `check_v3_6_7_pattern_protection.py` OK (research_architect not a pattern-protected agent; edits are additive).
