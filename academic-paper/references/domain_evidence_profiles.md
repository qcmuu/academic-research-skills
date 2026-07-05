# Domain Evidence Profiles

> **Advisory only.** A domain evidence profile changes which evidence types the literature screening *admits*. It never changes the A-F Overall Grade and never blocks manuscript ship. It never changes which databases are queried (that stays `Discipline`-driven in `literature_strategist_agent` Step 2). Consumed only by `academic-paper`'s `literature_strategist_agent`; produced by `intake_agent` Step 12 as the PCR `Domain Evidence Profile` row.

## Domain Evidence Profiles

The ship-ready enum is seven values. `unknown_user_defined` is the default and the neutral fallback. The three `social_science_*` / `communication_mixed` profiles are social-science-track refinements (Stage 1 of [`docs/SOCIAL_SCIENCE_ADAPTATIONS.md`](../../docs/SOCIAL_SCIENCE_ADAPTATIONS.md)) that split the original single `general_social_science` bucket by paradigm; `general_social_science` is retained as a coarse fallback for multidisciplinary or mixed-strand social-science work that does not fit one of the refined buckets.

| Profile | Standard evidence types | Common provenance requirements | Critical gaps to surface | Reserved-note |
|---|---|---|---|---|
| `social_science_qualitative` | Ethnographic fieldwork, interview transcripts, grounded-theory memos, policy texts, archival records, oral histories; peer-reviewed qualitative studies | Fieldnote / archive provenance acceptable; expert-elicitation records acceptable; recency is not a quality signal (canonical theory texts are central) | Single-context over-generalization; thin trustworthiness (no member checking / audit trail); interpretive over-reach | — (ship-ready, social-science-track Stage 1) |
| `social_science_quantitative` | Peer-reviewed empirical studies, working papers (SSRN / NBER / arXiv q-fin / econ), quasi-experimental & causal-inference designs, large-N administrative data | Preprint servers and working-paper series acceptable (peer review lags the field); code/data replication packages valued | Weak identification strategy; specification search / p-hacking; external-validity overreach beyond the sample | — (ship-ready, social-science-track Stage 1) |
| `communication_mixed` | Peer-reviewed studies AND industry/sector reports, news archives, media corpora, platform/audience data, content-analysis coding sheets; grey literature on media markets | Industry-report and news-archive provenance acceptable where directly relevant; computational trace data acceptable with provenance | Selection bias in media corpora; industry-funded report without independent corroboration; claims of generalizability from single-platform data | — (ship-ready, social-science-track Stage 1) |
| `general_social_science` | Peer-reviewed empirical studies, mixed-methods, expert-panel / context-dependent policy analyses | Journal or proceedings; expert-panel reports acceptable where context-dependent | Single-context generalization; weak external validity | — (ship-ready; coarse social-science fallback when the refined buckets above do not fit) |
| `cs_ml` | Peer-reviewed papers AND archival preprints (e.g. arXiv), conference proceedings; industry technical reports | Preprint server or proceedings acceptable; peer-review lags the field | Non-reproducible results; benchmark cherry-picking | — (ship-ready) |
| `humanities_interpretive` | Primary sources, archival material, canonical/older texts, monographs | Primary-source provenance; recency is not a quality signal | Interpretive over-reach; missing primary-source grounding | — (ship-ready) |
| `unknown_user_defined` | Neutral single-pyramid (pre-#259 behavior) — peer-reviewed default | Standard peer-review expectation | (no profile-specific loosening) | Default / neutral fallback |

**Reserved profiles (documented, NOT in the enum).** Selecting one records effective `unknown_user_defined` and surfaces a reserved-fallback advisory — its checklist does not exist yet, so it falls back to neutral to prevent false rigor:

`clinical` · `wet_lab` · `materials_physics` · `legal_case_based` · `education` — *not in enum yet; selecting this falls back to `unknown_user_defined`.*

## Field-guidance carry-forward (seeded from the deep-research evidence hierarchy)

The substance of the field-centric `## Field-Specific Adjustments` table in `deep-research/references/source_quality_hierarchy.md` is carried forward here so no per-field guidance is silently dropped. The deep-research file is **read, not edited** — this is a one-time authoring copy, not a runtime dual-read.

Normative (folded into a ship-ready profile row above):
- **Social Science (qualitative strand)** → folded into `social_science_qualitative` (Level V-VI qualitative + archival; interpretive).
- **Social Science (quantitative strand)** → folded into `social_science_quantitative` (Level III-IV empirical + causal-inference; working papers admissible).
- **Communication / journalism** → folded into `communication_mixed` (Level III-V mixed + industry/news archives).
- **Social Science (indeterminate / multidisciplinary strand)** → folded into `general_social_science` (Level III-V; mixed methods common).
- **Technology** → folded into `cs_ml` (Level III + industry reports; peer review lags reality).
- **Humanities** → folded into `humanities_interpretive` (Level VI primary sources; different epistemology — "evidence" means different things).
- **Policy** → folded into `general_social_science` (Level IV-V + VII expert panels; context-dependent, expert opinion valued). There is no dedicated Policy profile.

**Historical reference — non-normative; current behavior for these domains is neutral `unknown_user_defined` until the `clinical` / `education` profile ships:**
- **Medicine/Health** — Level I-II (RCTs, meta-analyses); Level I-III common; evidence-based-medicine tradition. *(maps to reserved `clinical`)*
- **Education** — Level III-IV (quasi-experimental); Level IV-VI common; randomization often impractical. *(maps to reserved `education`)*

These two rows are preserved verbatim for the eventual `clinical` / `education` profiles. They do NOT change runtime behavior today: until those reserved profiles ship, Medicine/Health and Education runs use the neutral `unknown_user_defined` pyramid, exactly as every other unmapped selection does.

## #246 forward reference

Discipline-relative *grade aggregation* (how these evidence expectations roll up into an Overall Grade) is tracked separately in #246 and is **not yet implemented**. Until #246 ships, the A-F Overall Grade lookup in `deep-research/references/source_quality_hierarchy.md` applies unchanged. #259 ships no aggregation logic and no placeholder aggregation code.
