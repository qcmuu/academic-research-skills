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
| 1 | Domain evidence profile refinement | ⏳ pending |
| 2 | Reference content (journals, methods, EQUATOR, theory) | ⏳ pending |
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
