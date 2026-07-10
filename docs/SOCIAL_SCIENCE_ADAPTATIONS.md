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
| 6 | Reflexivity / positionality advisory agent | ✅ done |
| 7 | Reviewer discipline calibration (7a DiD/IV/RDD + 7b Dim3 + 7c qual) | ✅ done |
| 8 | Chinese social-science ecology (CNKI / CSSCI) | ✅ done |
| 9 | Dual-track evidence grading (P0) | ✅ done |
| 9b | P1: Identification Audit + multi-claim track rules | ✅ done |

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

### Stage 6 — Reflexivity / positionality advisory agent (high-coupling, completed)
- `[NEW] academic-pipeline/agents/reflexivity_agent.md` — Bucket C advisory observer; checks positionality / researcher-effect / cultural-sensitivity / power-asymmetry / member-checking; profile-gated intensity (full for qualitative, light for positivist); `measures: reflexivity_positionality`, `blocking: false`.
- `[NEW] shared/reflexivity_rubric.md` — 5-dimension rubric operationalizing SRQR reflexivity items + CASP item 6; frontmatter `rubric_version: 1.0`.
- `[EDIT] scripts/check_v3_9_2_phase_boundary.py` — `BUCKET_BCD_AGENTS` 16→17 (+reflexivity_agent in Bucket C); count assertion + header comment.
- `[EDIT] scripts/check_v3_10_134_write_scope.py` — `BUCKET_BCD_AGENT_FILES` 16→17; count assertion + I1 docstring (16→17 / 39→40).
- `[EDIT] scripts/test_check_v3_9_2_phase_boundary.py` — hardcoded 16/39 → 17/40 (3 sites).
- `[EDIT] academic-pipeline/agents/pipeline_orchestrator_agent.md` — step-3 dispatch now invokes both observers; IRON RULE covers both; +full "Reflexivity & Positionality Observer" section mirroring the collaboration-depth one (when / how / cross-model consent / non-blocking guarantees / distinction).
- `[EDIT] academic-pipeline/SKILL.md` — Agent Team 5→6; Mode A dispatch list; Bucket C roster; agent-file table.
- **Verified:** phase-boundary + write-scope + spec-consistency + domain-evidence lints green (17 B/C/D); 50 related tests pass. The `check_collaboration_depth_rubric` test failure on Windows is a pre-existing path-separator issue in an untouched file (shared/ vs shared\), unrelated to this change.

### Stage 8 — Chinese social-science ecology (low priority, completed)
- `[NEW] deep-research/references/cnki_protocol.md` — CNKI search strategy: CSSCI vs 北大核心 vs CSTPCD index subsetting; field syntax (SU=/TI=/KY=); Chinese synonym expansion; citation chaining; no-DOI coverage-gap handling (`obtained_via: cnki_institutional` exemption).
- `[EDIT] academic-paper-reviewer/references/top_journals_by_field.md` — +Mainland China (CSSCI) section: 社会学/人口学, 政治学/公管, 新闻传播学, 经济学/管理学, 综合/跨学科 first-tier CSSCI venues.
- `[NEW] academic-paper/references/chinese_writing_conventions.md` — title/abstract/keyword norms; 一二三 section numbering (vs English 1.2.3.); 基金项目 funding format with full funder names; 作者简介 first-page footnote; 中图分类号 + 文献标识码; bilingual handling; localization-error flag table.
- `[EDIT] deep-research/agents/bibliography_agent.md` — +Chinese-language social-science row (CNKI scoped to CSSCI) + no-DOI caveat.

### Stage 9 — Dual-track evidence grading (P0 residual of #246)
- `[NEW] docs/design/2026-07-10-dual-track-evidence-grading-spec.md` — schema + document design (tracks, clamps, carriers, out-of-scope).
- `[NEW] deep-research/references/evidence_grade_tracks.md` — canonical track vocabulary + profile→track table + gold standards + aggregation clamps.
- `[EDIT] deep-research/references/source_quality_hierarchy.md` — design-code-only pyramid; Evidence fitness criterion; dual-track pointer; **Field-Specific Adjustments table block byte-preserved** (#259 C6 pin).
- `[EDIT] deep-research/templates/evidence_assessment_template.md` — track / claim_class / design code vs fitness split.
- `[EDIT] deep-research/agents/source_verification_agent.md` — remove Weight-as-authority table; track resolution; dual-track matrix.
- `[EDIT] academic-paper/agents/literature_strategist_agent.md` — derive track after profile; no design-code ranking under ss_* / humanities.
- `[EDIT] academic-paper/references/domain_evidence_profiles.md` — replace stale “#246 not implemented” with dual-track derivation table; keep Advisory only + #246 mention for C4.
- `[EDIT] shared/social_science_config.md` — §8 Evidence grade track resolution.
- `[NEW] scripts/check_evidence_grade_tracks.py` + tests — surface lint for tracks doc, mirrored tables, no Weight authority table, template fitness fields.
- **Verified:** `check_domain_evidence_profile.py` OK (C6 pin held); `check_evidence_grade_tracks.py` OK.

### Stage 9b — P1 Identification Audit + multi-claim track application
- `[NEW] shared/templates/identification_audit_card.md` — estimand/variation/assumptions/diagnostics/threat map; verdicts ready | needs design repair | not causal yet; full + short form; advisory only.
- `[EDIT] deep-research/references/evidence_grade_tracks.md` — §9 multi-claim_class rules + worked DiD+vignette example; §10 Identification Audit hook; invariants 9–10.
- `[EDIT] academic-paper-reviewer/agents/methodology_reviewer_agent.md` — emit full ID audit for causal_effect / DiD-IV-RDD-class designs; multi-claim boundary; refs table.
- `[EDIT] deep-research/agents/source_verification_agent.md` — multi-claim cards; short-form ID audit; forbidden cross-claim fitness inflation.
- `[EDIT] deep-research/templates/evidence_assessment_template.md` — multi-claim note + ID short-form block.
- `[EDIT] scripts/check_evidence_grade_tracks.py` — T8 (ID card + methodology wiring), T9 (multi-claim surface); mutation tests extended.
- `[EDIT] shared/social_science_config.md` — P1 add-ons pointer.
- **Verified:** `check_evidence_grade_tracks.py` OK; dual-track + domain-evidence mutation suites green.

### Final verification (stages 0–9b)
- Core CI lints green including domain-evidence (C6 FSA pin unchanged) + evidence-grade-tracks (T1–T9).
- Agent classification unchanged (no new agent).
- Pre-existing unrelated Windows path-separator failure in collaboration-depth rubric test may still surface on win32.
