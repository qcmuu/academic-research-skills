# Evidence Grade Tracks — Dual-Track Grading Vocabulary

> **Canonical vocabulary** for profile-resolved evidence grading (social-science-track P0).
> Spec: [`docs/design/2026-07-10-dual-track-evidence-grading-spec.md`](../../docs/design/2026-07-10-dual-track-evidence-grading-spec.md).
> Profile → track table is mirrored in [`shared/social_science_config.md`](../../shared/social_science_config.md) §8 and
> [`academic-paper/references/domain_evidence_profiles.md`](../../academic-paper/references/domain_evidence_profiles.md).
>
> **Advisory only.** A track changes how sources are *graded and narrated*. It never blocks manuscript ship,
> never alone excludes a source, and never tightens #259 admit gates.

---

## 1. Why tracks exist

The I–VII design ladder in `source_quality_hierarchy.md` is a **descriptive taxonomy** (what kind of study
design is this?). It is **not** a universal strength ranking. Treating Level VI ethnography as inherently
weaker evidence than Level II RCTs is an EBM paradigm choice, not field-neutral science.

**Two axes (do not conflate):**

| Axis | Field | Role |
|---|---|---|
| Design code | `design_level_code` ∈ {I…VII, NA} | Descriptive interoperability only — **never** an Overall input by itself |
| Evidence fitness | `evidence_fitness` ∈ {A…F} | Claim-relative quality under the active **track** |

Overall Grade always goes through the six criteria → aggregation rules. Design code is reported beside them.

---

## 2. Track enum

```text
EvidenceGradeTrack =
  | ebm_design        # Track M — experimental / clinical-adjacent ladder as fitness gold
  | ss_quantitative   # Track S-Q — identification / design integrity (observational causal & large-N)
  | ss_qualitative    # Track S-I — trustworthiness / interpretive fitness
  | humanities        # Track H — primary-source / interpretive fitness
  | neutral           # Pre-dual-track single behavior (byte-compatible default)
```

```text
ClaimClass =
  | causal_effect | descriptive_pattern | interpretive_meaning
  | theoretical_argument | methodological | policy_evaluative | unspecified
```

```text
DesignLevelCode = I | II | III | IV | V | VI | VII | NA
```

`NA` = design ladder not meaningful (pure theory, formal model without empirical design).

---

## 3. Profile → track resolution (deterministic)

In `academic-paper`, track is **derived** from the PCR `Domain Evidence Profile` (scholar-confirmed).
Do **not** ask a second track question at intake. Standalone `deep-research` may take an optional
scholar declaration; else `neutral`.

| Domain Evidence Profile (effective) | EvidenceGradeTrack | Default ClaimClass if unspecified |
|---|---|---|
| `social_science_qualitative` | `ss_qualitative` | `interpretive_meaning` |
| `social_science_quantitative` | `ss_quantitative` | `causal_effect` |
| `communication_mixed` | strand-split: quant → `ss_quantitative`, qual → `ss_qualitative`; if undivided corpus → `ss_quantitative` + `[TRACK-MIXED-DEFAULT]` | `descriptive_pattern` |
| `general_social_science` | method-driven: causal/large-N → `ss_quantitative`; interpretive → `ss_qualitative`; unknown → `neutral` + `[TRACK-COARSE-PROFILE]` | `unspecified` |
| `humanities_interpretive` | `humanities` | `interpretive_meaning` |
| `cs_ml` | `ebm_design` (reproducibility-emphasized; preprints already admit-loosened by #259) | `descriptive_pattern` |
| `unknown_user_defined` / absent | `neutral` + `[NO-TRACK-NEUTRAL]` when grading runs in full mode with no declaration | `unspecified` |
| reserved request (clinical, education, …) | `neutral` until reserved profile ships (no false rigor) | `unspecified` |

**Mismatch:** If `[PROFILE-DISCIPLINE-MISMATCH]` already fired, track still follows **profile** (paradigm),
not `Discipline` (databases). Optionally note `[TRACK-FOLLOWS-PROFILE]`.

---

## 4. Track gold standards (what Evidence fitness A means)

### 4.1 `ebm_design`

- **causal_effect gold:** design codes I–II (SR/MA, RCT) when methods are sound.
- Sample/data: size, power, representativeness (classic semantics).
- Under this track, pre-dual-track behavior is preserved.

### 4.2 `ss_quantitative`

Gold standard is **identification / design integrity for the claim**, not “was it randomized?”

| ClaimClass | Fitness A looks like |
|---|---|
| `causal_effect` | Credible design for the claim (DiD + parallel-trends engagement; IV relevance+exclusion; RDD bandwidth/manipulation; ITS level+slope; or equivalent) **or** explicit non-causal framing if design cannot support causation |
| `descriptive_pattern` | Adequate frame, measurement validity, uncertainty reported |
| `policy_evaluative` | Counterfactual/comparison strategy transparent; external validity scoped |

**Sample/data (reinterpreted):** data appropriateness (admin completeness, survey design, constructs, missing data, analysis plan when claimed) — not “N large.”

**Forbidden:** Fitness A solely because design_code is II or III.

Cross-check lists (do not copy): `academic-paper-reviewer/references/statistical_reporting_standards.md` §2.8.

### 4.3 `ss_qualitative`

Gold standard is **trustworthiness / method–claim fit**, not pyramid height.

| ClaimClass | Fitness A looks like |
|---|---|
| `interpretive_meaning` | Coherent method–claim fit + trustworthiness package (audit trail / thick description / triangulation or justified alternative); positionality engaged where tradition expects (SRQR / CASP item 6 — **advisory pointer only**) |
| `theoretical_argument` | Concepts specified; dialogue with prior theory; boundary conditions; illustrative evidence not over-claimed as general law |
| `descriptive_pattern` | Sampling logic for qualitative inquiry stated; saturation/stopping rule where expected |

**Sample/data (reinterpreted):** depth and corpus appropriateness — not probabilistic N.

**Forbidden:** Lower overall **solely** because `design_level_code ∈ {VI, VII}`.

### 4.4 `humanities`

Primary-source grounding + interpretive discipline (see profile `humanities_interpretive`).
Same clamp as `ss_qualitative`: design code must not alone depress Overall.

### 4.5 `neutral`

Use Field-Specific Adjustments + pre-dual-track aggregation in `source_quality_hierarchy.md`.
Emit `[NO-TRACK-NEUTRAL]` in full grading reports when track was not resolved from profile/declaration.

---

## 5. Aggregation (track-aware)

Same three-step skeleton as `source_quality_hierarchy.md`:

1. **Integrity floor (track-invariant):** Conflicts = F → overall ≤ D; fabricated/predatory → recommend exclude.
2. **Base grade:** median of six criteria (A=4 … F=0; round down on adjacent-grade tie).
3. **Fitness adjustment:** +1 step if `evidence_fitness` is A, unless Methodology is F. Never past A.

### Track clamps

| Track | Clamp |
|---|---|
| `ss_qualitative`, `humanities` | Must not lower overall solely because design_level_code ∈ {VI, VII} |
| `ss_quantitative` | Must not require design_code ≤ II for fitness A on `causal_effect` |
| `ebm_design` | Classic gold-standard ladder for causal_effect |
| all | Track must not raise a source past the integrity floor |

### Criterion labels

| Label | Meaning |
|---|---|
| **Evidence fitness (A–F)** | Claim-relative quality under active track (replaces “Evidence Level” as an A–F criterion name) |
| **Design code (I–VII/NA)** | Descriptive only; separate line on the assessment card |
| Peer review / Methodology / Sample·data adequacy / Currency / Conflicts | As hierarchy; Sample·data and Methodology interpretation is track-conditioned per §4 |

---

## 6. Orthogonal layers (do not merge)

```text
#259 Domain Evidence Profile  →  who is ADMITTED (screening)
this file EvidenceGradeTrack  →  how ADMITTED sources are GRADED
#183 epistemic_status         →  how STRONGLY prose may claim
reflexivity_agent             →  whether POSITIONING is reported (advisory)
```

---

## 7. Consumer duties (v1)

| Consumer | Duty |
|---|---|
| `source_verification_agent` | Primary grader. Resolve track (§3); grade under §4–5; report design code separately from fitness. Unknown → `neutral` + `[NO-TRACK-NEUTRAL]`. |
| `literature_strategist_agent` | After profile resolve, derive track; attach track label on quality notes / matrix when non-neutral; do not rank sources by design-code height under ss_* / humanities. Does **not** replace source_verification. |
| `bibliography_agent` | May show design code; must not sort “stronger level = better” under ss_* / humanities tracks. |
| Writers / synthesis | Consume overall + track_rationale; epistemic_status rules remain separate. |

**deep-research before PCR:** standalone deep-research defaults to `neutral` unless scholar declares a track/profile-equivalent. Optional later re-annotation under academic-paper profile is advisory (`[TRACK-REANNOTATE]`).

---

## 8. Worked examples (normative)

### Ethnography + `social_science_qualitative`

- design_level_code: VI · claim_class: interpretive_meaning · evidence_fitness: A (thick description, audit trail, positionality) → **overall may be A**.
- **Forbidden:** overall C/D “because Level VI.”

### Staggered DiD + `social_science_quantitative`

- design_level_code: III · claim_class: causal_effect · evidence_fitness: A only if identification engaged; C if two-way FE only with known bias and no robustness.
- **Forbidden:** fitness A merely from “quasi-experiment = III.”

### RCT + `ebm_design`

- Unchanged classic path.

### No profile

- track: `neutral` · `[NO-TRACK-NEUTRAL]`.

---

## 9. INVARIANTS (copy of load-bearing rules)

1. Design code ≠ weight — never sole Overall input.
2. Track resolution purity — academic-paper track = f(profile) only (no silent auto-track as authority).
3. Default neutral when profile/declaration absent.
4. Advisory only — no ship block from track alone.
5. Integrity floor track-invariant.
6. Reserved profiles stay neutral until real checklists ship.
7. #259 non-regression — admit gates remain loosen-only.
8. Orthogonal to epistemic_status and reflexivity_agent.
