# Identification Audit Card (advisory)

> **Purpose.** Structured, referee-style audit of the **identifying argument** for
> causal / quasi-experimental claims under track `ss_quantitative` (and, when
> relevant, `ebm_design` with observational causal framing).
>
> **Advisory only.** Never blocks manuscript ship. Never invents results, data, or
> citations. Does not run estimators or code. Complements — does not replace —
> `statistical_reporting_standards.md` §2.8 design checklists and dual-track
> Evidence fitness grades (`evidence_grade_tracks.md`).
>
> **Consumers:** `methodology_reviewer_agent` (manuscript under review);
> `source_verification_agent` (optional short form when grading a source for
> `claim_class: causal_effect` under `ss_quantitative`).
>
> **Inspiration (shape only):** estimand / variation / assumptions / diagnostics
> separation used in applied-economics identification review practice. ARS keeps
> human-in-the-loop authorship; this card surfaces gaps, it does not rewrite the design.

---

## When to emit

| Context | Emit full card? |
|---|---|
| Paper (or source) claims a **causal_effect** under track `ss_quantitative` | **Yes** (methodology reviewer: full; source verification: short form OK) |
| Design is DiD / IV / RDD / ITS / event-study / synthetic control / matching-as-causal / causal ML | **Yes** |
| Claim is purely descriptive / interpretive / theoretical | **No** — skip; do not force a causal audit |
| Track is `neutral` / `ss_qualitative` / `humanities` | **No** unless the prose itself advances causal_effect claims |

If multiple causal claims appear, emit **one card per primary causal claim** (or one card with numbered claim blocks). Do not average across claims.

---

## Core separations (do not collapse)

1. **Estimand** — what causal/descriptive quantity is claimed (ATT, ATE, LATE, local RD, event-time path, …).
2. **Variation** — what empirical comparison is supposed to identify it.
3. **Assumptions** — what must be true (parallel trends, exclusion, continuity, …).
4. **Diagnostics** — what can be checked in data/figures/tables.
5. **Non-testable argument** — what must be defended institutionally / theoretically, not by “more controls.”
6. **Scope** — population, period, policy claim the estimate can support.

**Guardrails:**
- Do not invent numbers, coefficients, or citations.
- First-stage F strong ≠ exclusion satisfied (IV).
- Insignificant pre-trends ≠ parallel trends proven (DiD); discuss power and event-study shape.
- Many controls ≠ identification.
- ML predictive performance ≠ causal validity.
- Robustness is not a shopping list: each check must name a **threat**.

---

## Full card template

```markdown
### Identification Audit (advisory)

**Claim (quoted or paraphrased with location):** […]
**Claim class:** causal_effect
**Evidence grade track:** ss_quantitative
**Main design:** [DiD | IV/2SLS | RDD sharp/fuzzy | ITS | event-study | synthetic control | matching | panel FE-as-causal | causal ML | hybrid | unclear]
**Estimand:** [ATT / ATE / LATE / local RD / … / unclear]
**Identifying variation:** [one sentence — treated vs control / cutoff / instrument-induced / …]

| Element | Stated? | Notes |
|---|---|---|
| Estimand named | present / partial / absent | |
| Source of variation named | present / partial / absent | |
| Identifying assumptions listed | present / partial / absent | |
| Threat→diagnostic map | present / partial / absent | |
| Scope / external validity scoped | present / partial / absent | |

**Threat → diagnostic → artifact map**

| Threat | Diagnostic that would address it | Artifact present? (table/fig/section) | Interpretation if fails |
|---|---|---|---|
| e.g. differential pre-trends | event-study / leads | yes/no/partial | |
| e.g. exclusion violation | institutional argument + placebo IV | … | |
| e.g. manipulation at cutoff | McCrary / density | … | |

**Non-testable assumptions (must be argued, not “tested away”):**
- …

**Strongest part of the identifying argument:** …
**Weakest part:** …

**Verdict:** `ready` | `needs design repair` | `not causal yet`
*(ready = identifying argument is articulated and key diagnostics engaged;
needs design repair = salvageable with named fixes;
not causal yet = causal language not supported by the design as written — reframe or redesign.)*

**Must-fix (advisory — scholar decides):**
1. …
2. …

**Suggested robustness plan (threat-tied only):**
| Threat | Diagnostic | Required artifact |
|---|---|---|
| | | |

**Cross-refs:** design checklist `statistical_reporting_standards.md` §2.8;
Evidence fitness under `evidence_grade_tracks.md` §4.2 (fitness A requires identification engagement, not design_code III alone).
```

---

## Short form (source verification only)

When grading a **bibliography source** (not the scholar’s own manuscript), use ≤120 words:

```markdown
**ID short-form:** design=[…] estimand=[…] variation=[…] assumptions engaged=[yes/partial/no]
diagnostics present=[yes/partial/no] → Evidence fitness for causal_effect cannot be A if assumptions/diagnostics are absent.
Verdict hint: ready | needs repair | not causal yet
```

---

## Negative examples (forbidden)

| Bad move | Why |
|---|---|
| “DiD is Level III so fitness A” | Design code ≠ identification quality |
| “Robust to 12 FE specs → causal” | Spec soup without threat map |
| “F>10 → IV valid” | Relevance ≠ exclusion |
| Inventing a parallel-trends figure the paper lacks | Fabrication |
| Blocking ship because verdict is `not causal yet` | Card is advisory |

---

## Relation to dual-track

- Card **feeds** Evidence fitness judgment under `ss_quantitative` + `causal_effect`.
- Card does **not** change admit gates (#259) or integrity floor.
- Card is **orthogonal** to reflexivity_agent and epistemic_status.
