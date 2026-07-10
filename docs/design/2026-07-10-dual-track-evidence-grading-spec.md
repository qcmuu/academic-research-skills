# Dual-Track Evidence Grading — Minimal Schema & Document Design

| | |
|---|---|
| **Status** | Design (schema + docs only). Implementation is a follow-up plan. |
| **Date** | 2026-07-10 |
| **Branch context** | `social-science-track` Stage follow-on (P0 from social-science adaptation review) |
| **Related** | #259 domain evidence profiles (shipped); #246 discipline-relative grading (closed as docs-only fitness language in `source_quality_hierarchy.md`); Kong §7.4.6 domain evidence standards |
| **Parent positioning** | `POSITIONING.md` copilot-not-pilot; `docs/SOCIAL_SCIENCE_ADAPTATIONS.md` layer-don't-overwrite; #259 INVARIANT 5 (advisory / no ship-block) |

---

## 0. One-sentence goal

Make **“what counts as strong evidence”** a **profile-resolved track**, so social-science sources are graded by **claim-fitness within their paradigm**, while the EBM design ladder remains available for designs that actually use it — without forking ARS or blocking manuscript ship.

---

## 1. Problem (grounded in current code)

### 1.1 What already exists (do not re-invent)

`deep-research/references/source_quality_hierarchy.md` already states:

- Study-design level (I–VII) is **field-neutral taxonomy**.
- The **Evidence Level criterion** grades **fitness for claim** against a field gold standard.
- Overall grade = integrity floor → median of six criteria → optional fitness +1.

#259 ships **Domain Evidence Profile** on the PCR and loosens **admissibility** only. Explicitly: profile **must not** change A–F Overall Grade (#259 INVARIANT 5 / Q5).

#246 is marked closed via docs that added the fitness language above. Residual gap is **operational**, not conceptual: agents and templates still **behave as if weight = pyramid height**.

### 1.2 Residual failure mode (this design closes)

| Surface | What still happens today |
|---|---|
| `source_verification_agent.md` | Embeds I–VII table with **Weight: Highest…Lowest**; qualitative = Level VI **Low-Moderate**. No pointer to fitness aggregation or profile. |
| `evidence_assessment_template.md` | “Evidence Level” filled as **I–VII**, not as fitness Grade A–F. Overall becomes pyramid-weighted in practice. |
| Field-Specific Adjustments | One coarse “Social Science → Level III–V” row; does not split quant causal vs interpretive vs theory. |
| #259 profile | Changes **who gets admitted**, not **how admitted sources are graded**. A gold-standard ethnography can still be narrated as “weak evidence.” |
| Carrier split | Profile lives on **PCR (academic-paper)**; grading often runs in **deep-research** before PCR exists. |

**Bedrock claim:** Different research traditions do not share one ordinal “design strength” scale for claim support. Collapsing them into EBM weight is not neutrality — it is a hidden paradigm choice.

**Contrast with convention:** “Add more social-science examples under Level VI.” That leaves the weight semantics intact and only softens the prose.

---

## 2. Design principles (non-negotiable)

1. **Dual track, not dual product.** One suite; track is a resolved parameter.
2. **Layer, don't overwrite.** Keep I–VII as a **descriptive design code**. Do not delete the EBM pyramid. Add a parallel **fitness track** for grading.
3. **Advisory only.** Track changes how grades are *explained and aggregated*. It does **not** block ship, does **not** auto-exclude sources, does **not** rewrite scholar claims.
4. **Scholar-confirmed paradigm, never auto-detect track as authority.** Track resolves from scholar-confirmed **Domain Evidence Profile** (or an explicit deep-research declaration). Inference may *suggest*; confirmation required (mirror #259 INVARIANT 6).
5. **Monotonicity w.r.t. integrity.** Integrity floor (COI F, predatory, fabricated) is **track-invariant**. Track must not “rescue” integrity failures.
6. **Minimal surface.** One vocabulary doc + one resolution table + three consumer touch points. No new agent. No passport Schema number. No new blocking gate.

---

## 3. Vocabulary schema (minimal)

### 3.1 Why not a JSON Schema file (yet)

Mirror #259 Style-Profile / Domain-Evidence-Profile discipline: the first ship is a **prose-validated field + reference vocabulary**, not a handoff Schema. A JSON Schema is optional later if passport cross-skill carry becomes required.

### 3.2 Core types

```text
EvidenceGradeTrack =
  | "ebm_design"          # Track M — experimental / clinical-adjacent ladder as fitness gold
  | "ss_quantitative"     # Track S-Q — identification / design integrity for observational causal & large-N
  | "ss_qualitative"      # Track S-I — trustworthiness / positionality-aware interpretive fitness
  | "humanities"          # Track H — primary-source / interpretive fitness (maps from existing profile)
  | "neutral"             # Pre-dual-track single behavior (byte-compatible default)

DesignLevelCode = "I" | "II" | "III" | "IV" | "V" | "VI" | "VII" | "NA"
  # I–VII remain the existing taxonomy. "NA" = not meaningful (pure theory, formal model without empirical design)

ClaimClass =
  | "causal_effect"
  | "descriptive_pattern"
  | "interpretive_meaning"
  | "theoretical_argument"
  | "methodological"
  | "policy_evaluative"
  | "unspecified"
```

### 3.3 Per-source grade record (prose card shape)

Extends `evidence_assessment_template.md` conceptually. Fields that must appear when dual-track is active:

```yaml
# Evidence Assessment Card — dual-track fields (additive)
evidence_grade_track: ss_qualitative          # resolved track
claim_class: interpretive_meaning             # what claim this source is asked to support
design_level_code: VI                         # descriptive only; NOT a weight
design_level_note: "single ethnography"       # free text

criteria:
  evidence_fitness: A    # was "Evidence Level"; now explicitly fitness-for-claim under track
  peer_review: B
  methodology: A         # track-conditioned interpretation (see §5)
  sample_or_data: B      # renamed semantics under ss_*; see §5.2
  currency: A            # claim-relative; already partially documented
  conflicts: A

overall: A               # aggregation per §6
track_rationale: "ss_qualitative gold standard is trustworthiness package, not RCT ladder"
```

**Invariant:** `design_level_code` is **never** copied into Overall by itself. Overall always goes through criteria → aggregation.

### 3.4 PCR / declaration carrier

| Context | Carrier | Field |
|---|---|---|
| `academic-paper` (has intake) | PCR row (existing) | `Domain Evidence Profile` → **resolve** `evidence_grade_track` (derived, not stored unless we want display) |
| Optional display | PCR row (new, optional) | `Evidence Grade Track` = resolved track (read-only derived; overwrite only via profile change) |
| Standalone `deep-research` | **Optional** declaration in Research Plan / RQ Brief | `evidence_grade_track` scholar-confirmed; default `neutral` |
| Material Passport | **Out of scope for v1** (same R7 reason as #259: passport is opt-in side input) | — |

**Derived, not second scholar choice:** Track is a pure function of profile (or explicit deep-research declaration). Do not ask the scholar for both profile and track in academic-paper intake.

---

## 4. Profile → track resolution (deterministic)

Canonical table — also to be mirrored in `shared/social_science_config.md` § new section and `domain_evidence_profiles.md` forward-ref replacement for the #246 stub.

| Domain Evidence Profile (effective) | EvidenceGradeTrack | Default ClaimClass if unspecified |
|---|---|---|
| `social_science_qualitative` | `ss_qualitative` | `interpretive_meaning` |
| `social_science_quantitative` | `ss_quantitative` | `causal_effect` |
| `communication_mixed` | split: quant strand → `ss_quantitative`; qual strand → `ss_qualitative`; if single mixed corpus without split → `ss_quantitative` with advisory `[TRACK-MIXED-DEFAULT]` | `descriptive_pattern` |
| `general_social_science` | `ss_quantitative` if methods look causal/large-N; else `ss_qualitative` if methods look interpretive; if unknown → `neutral` + `[TRACK-COARSE-PROFILE]` | `unspecified` |
| `humanities_interpretive` | `humanities` | `interpretive_meaning` |
| `cs_ml` | `ebm_design` with CS-adjusted gold (preprints OK already via #259 admit); grading stays design-ladder + reproducibility emphasis | `descriptive_pattern` |
| `unknown_user_defined` / absent | `neutral` | `unspecified` |
| reserved request (clinical, education, …) | `neutral` until reserved profile ships (no false rigor) | `unspecified` |

**Mismatch:** If PCR `Discipline` and profile disagree (#259 mismatch advisory), track still follows **profile** (paradigm signal), not Discipline (database signal). Emit `[TRACK-FOLLOWS-PROFILE]` one-liner when mismatch already fired.

---

## 5. Track definitions (what “gold standard” means)

### 5.1 Shared: design code stays descriptive

All tracks **may** still assign `design_level_code` I–VII/NA for interoperability (bibliometric habits, export). Agents must label it **Design code**, never “Evidence weight.”

### 5.2 Track `ebm_design` (Track M)

- **Gold standard for causal_effect claims:** Levels I–II (SR/MA, RCT), unchanged.
- **Evidence fitness Grade A:** design code meets field gold for that claim class.
- **Sample/Data criterion:** size, power, representativeness (current semantics).
- **Currency:** field-velocity bands (current table).
- **Byte-compatible** with pre-dual-track behavior when track is `ebm_design` or when `neutral` elects EBM interpretation (see §6.3).

### 5.3 Track `ss_quantitative` (Track S-Q)

Gold standard is **identification / design integrity for the claim**, not “was it randomized?”

| ClaimClass | Grade A fitness looks like |
|---|---|
| `causal_effect` | Credible design for the claim: DiD with parallel-trends engagement, IV with relevance+exclusion, RDD with bandwidth/manipulation checks, ITS with level+slope, or equivalent; **or** explicit non-causal framing if design cannot support causation |
| `descriptive_pattern` | Adequate sampling frame, measurement validity, uncertainty reported |
| `policy_evaluative` | Counterfactual / comparison strategy transparent; external validity scoped |

**Sample/Data criterion (reinterpreted):** not “N large,” but **data appropriateness** — administrative completeness, survey design, construct measurement, missing-data handling, prereg/analysis plan when claimed.

**Currency:** working papers (SSRN/NBER) are not penalized when the field moves on working-paper time; foundational methods papers not age-penalized.

**Must not:** award Grade A fitness solely because design_code is II; a badly identified “RCT-like” field experiment can be fitness C/D.

Cross-link (no copy): Stage 7a checklists in `statistical_reporting_standards.md` §2.8 for *what to look for*; this track only defines *grading semantics*.

### 5.4 Track `ss_qualitative` (Track S-I)

Gold standard is **trustworthiness / reporting completeness for interpretive claims**, not pyramid height.

| ClaimClass | Grade A fitness looks like |
|---|---|
| `interpretive_meaning` | Coherent method–claim fit (e.g. ethnography, GT, discourse) + trustworthiness package: audit trail / thick description / triangulation or justified alternative; positionality/reflexivity engaged where tradition expects (SRQR / CASP item 6 — **advisory link**, not a block) |
| `theoretical_argument` | Concepts specified; dialogue with prior theory; boundary conditions; evidence used illustratively is not over-claimed as general law |
| `descriptive_pattern` | Sampling logic for qualitative inquiry (purposive/theoretical) stated; saturation or stopping rule discussed where expected |

**Sample/Data criterion (reinterpreted):** **depth and appropriateness of corpus** (not probabilistic N). Thin single-interview “case” for a sweeping cultural claim → fitness D/F.

**Currency:** canonical theory and historical sources are not age-penalized (already partially in hierarchy Currency note).

**Design code:** typically VI or V; **must be allowed to receive overall A** when fitness A and other criteria hold (hierarchy already allows this in prose — this track makes agents implement it).

### 5.5 Track `humanities`

Same spirit as `ss_qualitative` but gold standard is **primary-source grounding + interpretive discipline** (existing `humanities_interpretive` profile row). Design code often VI/NA.

### 5.6 Track `neutral`

- Preserve **pre-dual-track** aggregation text as-is.
- Field-Specific Adjustments table remains the only coarse dial.
- Emit `[NO-TRACK-NEUTRAL]` in full grading reports so neutrality is visible (mirror `[NO-PROFILE-NEUTRAL]`).

---

## 6. Aggregation rules (track-aware, minimal change)

Keep the three-step skeleton in `source_quality_hierarchy.md` § Overall Source Grade:

1. **Integrity floor** (track-invariant): Conflicts = F → overall ≤ D; fabricated / predatory fail → recommend exclude (unchanged).
2. **Base grade** = median of six criteria (A=4…F=0, round down on tie).
3. **Fitness adjustment:** +1 step if `evidence_fitness` is A, unless Methodology is F.

### 6.1 Track-specific clamps (the actual #246 residual)

| Track | Clamp |
|---|---|
| `ss_qualitative`, `humanities` | **Forbidden:** lower overall **solely** because `design_level_code ∈ {VI, VII}`. Design code is not a criterion. |
| `ss_quantitative` | **Forbidden:** require design_code ≤ II for fitness A on `causal_effect`. Fitness A is identification quality. |
| `ebm_design` | Existing gold-standard ladder for causal_effect; no new clamps. |
| all | **Forbidden:** track raises a source past integrity floor. |

### 6.2 Criterion rename (docs only, one breaking label)

| Old label (template) | New label | Notes |
|---|---|---|
| Evidence Level (I–VII) | **Evidence fitness (A–F)** | Design code moves to its own line |
| Sample/Data | **Sample / data adequacy** | Interpretation track-conditioned (§5) |
| (unchanged) | Peer Review, Methodology, Currency, Conflicts | Methodology bullet lists become track-conditioned in agent prose |

### 6.3 `neutral` ≡ old behavior

Under `neutral`, agents may still fill “Evidence Level” as I–VII **and** map to fitness using Field-Specific Adjustments exactly as today’s hierarchy prose describes. Dual-track is **opt-in via profile**, not a forced migration of every run.

---

## 7. Consumer contract (who reads what)

| Consumer | v1 duty |
|---|---|
| `literature_strategist_agent` | Already profile-aware for **admit**. **Add:** when emitting quality notes / matrix rows, attach `evidence_grade_track` resolved from PCR; do not re-grade with EBM weights in prose. |
| `source_verification_agent` | **Primary grading consumer.** If track known (PCR visible in handoff materials, or deep-research declaration), grade under §5–6. If unknown → `neutral` + `[NO-TRACK-NEUTRAL]`. Replace embedded “Weight Highest…Lowest” table with design-code table + pointer to tracks doc. |
| `bibliography_agent` | Optional: show design_level_code; must not sort bibliography by “stronger level = better” under ss_* tracks. |
| `synthesis_agent` / writers | Consume overall grade + track_rationale; must not upgrade epistemic force beyond grade (existing epistemic_status rules remain orthogonal). |
| `reflexivity_agent` | **Not a grading consumer.** Orthogonal advisory. May be *cited* by ss_qualitative fitness notes as a reporting-standard pointer only. |
| Reviewer agents | Unchanged in v1 except they may read track labels if present; no new hard dimension. |

### 7.1 deep-research-before-PCR problem (explicit)

#259 deferred profile-aware `source_verification` for the same lifecycle reason. Dual-track v1 accepts:

| Path | Track resolution |
|---|---|
| Standalone deep-research | Optional scholar declaration; else `neutral` |
| deep-research → academic-paper | deep-research grades under `neutral` or declaration; academic-paper Phase 1 may **re-annotate** fitness labels under resolved track without re-fetching sources (`[TRACK-REANNOTATE]`) — optional, advisory |
| academic-paper only | Track from PCR profile at Phase 1+ |

**No requirement** that deep-research invent a PCR. That keeps R7 carrier discipline.

---

## 8. Document & file change map (implementation later)

| File | Action | Role |
|---|---|---|
| `deep-research/references/evidence_grade_tracks.md` | **NEW** | Canonical track definitions (§3–6). Single source of truth. |
| `deep-research/references/source_quality_hierarchy.md` | **EDIT** | Add short dual-track pointer; rename Evidence Level criterion to Evidence fitness; state design code ≠ weight; keep I–VII taxonomy section; expand Field-Specific Adjustments with profile-aware rows or point to tracks doc (avoid dual maintenance: prefer pointer). |
| `deep-research/templates/evidence_assessment_template.md` | **EDIT** | Split design code vs evidence fitness; add track + claim_class fields. |
| `deep-research/agents/source_verification_agent.md` | **EDIT** | Remove weight-as-authority table; load tracks doc; neutral fallback. |
| `academic-paper/references/domain_evidence_profiles.md` | **EDIT** | Replace “#246 not yet implemented” with “dual-track grading: see evidence_grade_tracks.md; profile → track table”. |
| `shared/social_science_config.md` | **EDIT** | New § “Evidence grade track resolution” copying the profile→track table. |
| `docs/SOCIAL_SCIENCE_ADAPTATIONS.md` | **EDIT** | Stage ledger entry (Stage 9 or “P0 dual-track”). |
| `scripts/check_evidence_grade_tracks.py` | **NEW** (with impl) | Surface lint: tracks doc exists; profile→track table present in config + profiles; source_verification does not contain “Weight.*Highest” authority table; template has fitness fields. |

**Not in v1:** new agent, passport schema, terminal_policies key, changes to A–F letter meanings (A still = primary evidence **for the claim under the track**).

---

## 9. Worked examples (normative for implementers)

### 9.1 Ethnography under `social_science_qualitative`

- design_level_code: VI  
- claim_class: interpretive_meaning  
- evidence_fitness: A (thick description, audit trail, positionality present)  
- sample_or_data: A (appropriate purposive sample; depth adequate)  
- peer_review: A; methodology: A; currency: A (foundational site); conflicts: A  
- **overall: A**  
- **Forbidden outcome:** overall C/D “because Level VI.”

### 9.2 Staggered DiD under `social_science_quantitative`

- design_level_code: III  
- claim_class: causal_effect  
- evidence_fitness: A if parallel trends + heterogeneous timing engaged; C if two-way FE only with known bias and no robustness  
- **Forbidden outcome:** fitness A merely from “quasi-experiment = Level III.”

### 9.3 RCT under `ebm_design` / clinical-adjacent

- Unchanged: Level II + sound methods → fitness A path as today.

### 9.4 No profile

- track: neutral; `[NO-TRACK-NEUTRAL]`; old aggregation path.

---

## 10. INVARIANTS

1. **Design code ≠ weight.** No agent may treat I–VII as Overall grade input under any track.
2. **Track resolution purity.** In academic-paper, track = f(profile) only; no silent auto-track from topic keywords as authority.
3. **Default neutral.** Absent profile/declaration ⇒ `neutral` + visible advisory.
4. **Advisory only.** Track never blocks ship; never alone excludes a source (exclusion remains predatory/fabricated/scholar decision).
5. **Integrity floor track-invariant.**
6. **No false rigor for reserved profiles.** clinical/education/… stay `neutral` until real checklists ship.
7. **#259 non-regression.** Admissibility remain loosen-only; dual-track does not tighten admit gates.
8. **Orthogonal to epistemic_status (#183).** Track grades source quality for a claim class; epistemic_status grades claim force in prose. Both can apply; neither replaces the other.
9. **Orthogonal to reflexivity_agent.** Reflexivity gaps are advisory reporting findings; they may inform ss_qualitative fitness notes but do not create a second block path.
10. **Deep-research byte-compatible under neutral.** With no declaration, source_verification output shape stays backward-compatible except for the optional advisory tag.

---

## 11. Out of scope (v1)

- Auto-detecting track from PDF text without scholar confirmation.  
- Passport Schema / append-only track ledger.  
- Making `citation_existence` or integrity gates track-dependent.  
- Reserved profile content (`clinical`, `education`, …).  
- Theory-contribution rubric (P3 in adaptation review) — separate advisory.  
- Replacing Campbell/Cochrane tools for health-policy overlap cases (RoB tools remain available).  
- Multi-track grading of one source for multiple claim classes in one card (v1: one primary claim_class per card; multi-claim → multiple cards).

---

## 12. Acceptance criteria (for a later implementation plan)

1. Spec + `evidence_grade_tracks.md` exist; profile→track table identical in config hub and profiles doc (lint-checked).  
2. Under fixture ethnography + profile `social_science_qualitative`, graded card can reach Overall A without design_code I–II.  
3. Under fixture weak-ID observational causal + `social_science_quantitative`, fitness cannot be A without identification engagement.  
4. Under no profile, `[NO-TRACK-NEUTRAL]` appears; no requirement to fill new fields beyond optional tags.  
5. `check_domain_evidence_profile.py` still green; no #259 admit-gate regression.  
6. No new Bucket A/B agent; agent count invariants unchanged.

---

## 13. Relationship summary

```text
#259 Domain Evidence Profile  →  who is ADMITTED (screening)
this design EvidenceGradeTrack →  how ADMITTED sources are GRADED (fitness)
#183 epistemic_status          →  how STRONGLY prose may claim
reflexivity_agent              →  whether POSITIONING is reported (advisory)
```

Four layers; do not merge them.

---

## 14. Recommended implementation order (not part of this schema freeze)

1. Land `evidence_grade_tracks.md` + hierarchy pointer + template field split (docs-only PR).  
2. Wire `source_verification_agent` + `literature_strategist` consumption.  
3. Lint + two golden fixtures (qual A-allowed, quant ID-sensitive).  
4. Only then consider optional PCR display row `Evidence Grade Track`.

---

## 15. Decision log (settled here)

| Decision | Choice | Why |
|---|---|---|
| Tracks vs rewrite pyramid | Dual track | Preserve EBM; fix hidden paradigm in grading |
| Track carrier | Derived from PCR profile; optional deep-research declaration | R7 / #259 carrier lesson |
| Schema form | Prose vocabulary first | Minimal; matches Style/Domain profile pattern |
| Social science split | quant vs qual tracks | One “social science” gold standard is false |
| communication_mixed | Strand split + mixed default advisory | Avoid forced single paradigm |
| overall letter meanings | Unchanged | A still “primary evidence for this claim under track” |
| Block on bad fitness | No | POSITIONING + #259 advisory discipline |
