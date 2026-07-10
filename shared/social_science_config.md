# Social Science Configuration Hub

> Central reference for the `social-science-track` branch. Downstream agents and reference files
> point here for the canonical list of supported social-science disciplines, their paradigm leans,
> preferred databases, and default citation styles. This file is **advisory config**, not a runtime
> contract — agents read it to calibrate; it does not override scholar decisions or hard gates.
>
> See [`docs/SOCIAL_SCIENCE_ADAPTATIONS.md`](../docs/SOCIAL_SCIENCE_ADAPTATIONS.md) for the full
> change log and stage plan.

## 1. Supported discipline clusters

| Cluster | Covers | Paradigm lean | Typical methods |
|---|---|---|---|
| Sociology (qualitative) | Sociological ethnography, interview studies, grounded theory, conversation analysis | Interpretive / critical | Ethnography, in-depth interviews, grounded theory, discourse analysis |
| Sociology (quantitative) | Survey sociology, social network analysis, demography | Positivist | Survey, SNA, quantitative content analysis |
| Anthropology | Cultural/social anthropology, ethnography, fieldwork | Interpretive | Long-term fieldwork, participant observation, life history |
| Political science & public admin | Comparative politics, IR, public policy, PA, political theory | Mixed | Comparative case study, process tracing, QCA, formal modeling, quasi-experiment |
| Economics & management | Micro/macro econ, finance, OB, strategy, marketing | Positivist, causal-inference | Econometrics, DiD/IV/RDD, structural models, field experiments |
| Communication / journalism | Media studies, journalism studies, political communication | Mixed | Content analysis, survey, audience research, digital trace analysis |

## 2. Evidence profile → discipline mapping

Drives Stage 1's `domain_evidence_profiles.md` extension. Default when ambiguous:
`social_science_qualitative` for interpretive work, `social_science_quantitative` for causal-inference work.

| Discipline cluster | Default profile | Notes |
|---|---|---|
| Sociology (qualitative), Anthropology | `social_science_qualitative` | Fieldnotes, archives, policy texts admissible; recency not a quality signal |
| Sociology (quantitative), Economics & management | `social_science_quantitative` | Working papers (SSRN/NBER) admissible; quasi-experimental design is the norm |
| Political science & public admin | `social_science_quantitative` or `social_science_qualitative` (method-driven) | Formal theory + QCA strands may lean qualitative |
| Communication / journalism | `communication_mixed` | Industry reports, news archives, media corpora admissible |

## 3. Preferred databases by discipline

Drives Stage 3's search protocols and `bibliography_agent`'s database selection.

| Cluster | Primary | Secondary |
|---|---|---|
| Sociology / Anthropology / Communication | Web of Science (SSCI), Scopus | JSTOR, ProQuest, Google Scholar |
| Political science | Web of Science (SSCI), Scopus | SSRN, Worldwide Political Science Abstracts |
| Economics & management | EconLit, SSRN, NBER | Web of Science (SSCI), Scopus, RePEc |
| Cross-disciplinary CN | CNKI (CSSCI subset) | 万方, 维普 |

> The default ARS stack (Semantic Scholar, OpenAlex, Crossref, arXiv) remains useful as a
> **supplementary** layer, but for social sciences it is rarely sufficient on its own — arXiv in
> particular has near-zero coverage of sociology/anthropology/communication.

## 4. Default citation styles

Drives Stage 4's `citation_format_switcher.md` extension.

| Cluster | Default | Alternates |
|---|---|---|
| Sociology, Psychology, Communication, Education | APA 7.0 | — |
| Political science | APSA | Chicago Author-Date |
| Economics & management | Chicago Author-Date | APA 7.0 |
| Anthropology | Chicago Notes & Bibliography | MLA |
| Chinese-language venues | GB/T 7714-2015 | APA 7.0 (for bilingual) |

## 5. Bias / quality-appraisal tool selection

Drives Stage 5's `risk_of_bias_agent` extension. The existing RoB 2 / ROBINS-I (Cochrane medical
paradigm) are retained for health-policy overlap, but social-science studies typically need:

| Study type | Tool |
|---|---|
| Qualitative (interview, ethnography, grounded theory) | CASP Qualitative Checklist; JBI QARI |
| Mixed methods | MMAT 2018 (covers 5 categories in one instrument) |
| Quantitative non-randomized (survey, quasi-experiment) | MMAT 2018 quantitative arm; ROBINS-I for causal claims |
| Quantitative descriptive (survey, content analysis) | JBI Prevalence / Exposure studies checklist |
| Qualitative evidence synthesis (synthesis of syntheses) | CERQual (confidence in qualitative evidence) |

## 6. Reporting guidelines (EQUATOR extension for social science)

Drives Stage 2's `equator_reporting_guidelines.md` extension.

| Design | Guideline |
|---|---|
| Qualitative interview/focus group | COREQ (already listed); SRQR (Standards for Reporting Qualitative Research) |
| Qualitative data extraction in synthesis | ENTREQ (Enhancing Transparency in Reporting the Synthesis of Qualitative Research) |
| Economic evaluation | CHEERS 2022 |
| Scoping review | PRISMA-ScR (already listed) |
| Mixed methods | GRAMMS (already listed) |

## 7. Reflexivity & positionality (Stage 6)

For interpretive / qualitative / critical work, the manuscript should carry a **positionality
statement** and demonstrate **reflexivity**. The `reflexivity_agent` (advisory, Bucket C) checks
for: declared standpoint, cultural sensitivity, power-asymmetry handling, member checking /
respondent validation, and researcher-effect disclosure. This is a social-science norm that the
upstream suite does not currently surface.

## 8. Evidence grade track resolution (dual-track P0)

Drives how admitted sources are **graded** (claim-fitness), not which sources are **admitted**
(#259). Canonical vocabulary: [`deep-research/references/evidence_grade_tracks.md`](../deep-research/references/evidence_grade_tracks.md).
Spec: [`docs/design/2026-07-10-dual-track-evidence-grading-spec.md`](../docs/design/2026-07-10-dual-track-evidence-grading-spec.md).

| Domain Evidence Profile (effective) | EvidenceGradeTrack | Notes |
|---|---|---|
| `social_science_qualitative` | `ss_qualitative` | Trustworthiness / method–claim fit; Level VI may be Overall A |
| `social_science_quantitative` | `ss_quantitative` | Identification quality for causal claims; not RCT-required |
| `communication_mixed` | strand-split; undivided → `ss_quantitative` + `[TRACK-MIXED-DEFAULT]` | Qual strand uses `ss_qualitative` |
| `general_social_science` | method-driven; unknown → `neutral` + `[TRACK-COARSE-PROFILE]` | Prefer refined profiles when possible |
| `humanities_interpretive` | `humanities` | Primary-source grounding |
| `cs_ml` | `ebm_design` | Reproducibility-emphasized |
| `unknown_user_defined` / absent | `neutral` | Pre-dual-track behavior; grading emits `[NO-TRACK-NEUTRAL]` |

**Consumers:** `source_verification_agent` (primary grader); `literature_strategist_agent` (attach track label; no design-code ranking under ss_* / humanities). **Non-consumers for blocking:** integrity gates, citation_existence policy, reflexivity_agent.

**P1 add-ons (still advisory):**
- **Multi-claim grading** — one assessment card per `claim_class` (`evidence_grade_tracks.md` §9); optional `[CLAIM-TRACK-OVERRIDE]`.
- **Identification Audit** — for `causal_effect` under `ss_quantitative`: template `shared/templates/identification_audit_card.md`; full card via `methodology_reviewer_agent`, short form via `source_verification_agent`.
