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
| 3 | Database search protocols (SSRN/JSTOR/WoS/Scopus) | ✅ done |
| 4 | Citation formats (APSA / Harvard / GB/T 7714) | ✅ done |
| 5 | Bias tools (MMAT/CASP/JBI/CERQual) + qualitative synthesis | ✅ done |
| 6 | Reflexivity / positionality advisory agent | ⏸ deferred (high-coupling; optional) |
| 7 | Reviewer discipline calibration (7a DiD/IV/RDD + 7b Dim3 + 7c qual) | ✅ done |
| 8 | Chinese social-science ecology (CNKI / CSSCI) | ⏸ deferred (low priority) |

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

### Stage 3 — Database search protocols (pure overlay)
- `[NEW] deep-research/references/social_science_database_protocols.md` — WoS SSCI, Scopus, SSRN, JSTOR, EconLit, NBER, ProQuest (SocAbs/WPSA/CommAbstracts) query syntax + per-discipline selection table.
- `[EDIT] deep-research/agents/bibliography_agent.md` — +Step 2.0 discipline-driven database selection; default ARS layer demoted to supplementary for social sciences.

### Stage 5 — Bias tools + qualitative synthesis (remove Cochrane-only tilt)
- `[EDIT] deep-research/agents/risk_of_bias_agent.md` — description/role + +MMAT 2018 (5 categories) + CASP Qualitative (10 items) + JBI + CERQual; Step 1 decision tree rewritten for study-design→instrument routing.
- `[EDIT] deep-research/agents/meta_analysis_agent.md` — +Qualitative Evidence Synthesis section (meta-ethnography / thematic / framework / mixed-methods); decision flowchart routes qualitative corpora to QES methods.

### Stage 4 — Citation formats +3 (APSA / Harvard / GB/T 7714)
- `[EDIT] academic-paper/references/citation_format_switcher.md` — comparison matrix +3 cols; +APSA/Harvard/GB-T-7714 per-format blocks.
- `[NEW] academic-paper/references/gbt7714_style_guide.md` — full GB/T 7714-2015 rules (dual system, CN-vs-Western authors, doc-type tags, bilingual conventions, error table).
- `[EDIT] academic-paper/agents/formatter_agent.md` — From→To matrix 5×5→8×8; Format-Specific Features +3 cols.
- `[EDIT] academic-paper/SKILL.md` — frontmatter description 5→8 formats; 4 prose surfaces updated.
- `[EDIT] academic-paper/references/mode_selection_guide.md` — +3 trigger phrases.

### Stage 7 — Reviewer discipline calibration (7a + 7b + 7c)
- `[EDIT] academic-paper-reviewer/references/statistical_reporting_standards.md` (7a) — +§2.8 causal-inference checklists: DiD (parallel-trends, staggered-timing), IV/2SLS (relevance F>10, exclusion, LATE), RDD (McCrary, CCT bandwidth, sharp/fuzzy), ITS (level+slope, autocorr).
- `[EDIT] academic-paper-reviewer/references/quality_rubrics.md` (7b) — Dimension 3 Evidence Sufficiency split into discipline-conditional columns (quantitative default vs qualitative/interpretive); eliminates the suite's worst quant-baked-in scoring.
- `[EDIT] academic-paper-reviewer/agents/methodology_reviewer_agent.md` (7c) — +qualitative sub-discipline refinements table (ethnography / grounded theory / discourse / interview / narrative) + quantitative causal-inference refinement.
- `[UNCHANGED] review_criteria_framework.md` — Dimension 3 already method-neutral; no drift (issue #396 safe).

### Verification
- All 7 core CI lints green: domain-evidence, v3.6.7 pattern-protection, v3.9.2 phase-boundary, v3.10 #134 write-scope, spec-consistency, rubric-weight, 215-field-norm.
- `pytest scripts/test_check_domain_evidence_profile.py` → 24 passed.
- Agent classification unchanged (23 Bucket A + 16 Bucket B/C/D) — no new agent file added, so write-scope manifest + phase-boundary lint untouched.

### Deferred (optional follow-up)
- **Stage 6** — reflexivity/positionality advisory agent. High-coupling: requires bumping `BUCKET_BCD_AGENTS` 16→17 in two Python lints (`check_v3_9_2_phase_boundary.py`, `check_v3_10_134_write_scope.py`) + orchestrator dispatch prose + SKILL.md Agent Team table. The reflexivity concern is already surfaced via CASP item 6 (Stage 5) and SRQR (Stage 2), so the gap is advisory-only, not missing.
- **Stage 8** — Chinese social-science ecology (CNKI protocol + CSSCI journal list + Chinese writing conventions). GB/T 7714 citation (Stage 4) already covers the most impactful gap; CNKI/CSSCI are additive.
