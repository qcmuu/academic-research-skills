# Evidence Assessment Template

## Purpose
Per-source quality assessment card. Used by the source_verification_agent to systematically evaluate each source entering the research pipeline.

**Dual-track:** Report `design_level_code` (I–VII/NA) as a **descriptive design code** and grade **Evidence fitness (A–F)** under the resolved `EvidenceGradeTrack`. Do not treat design code as Overall weight. See `deep-research/references/evidence_grade_tracks.md`.

## Assessment Card

```markdown
## Evidence Assessment Card

### Source Identification
- **Citation (APA 7.0)**: [full reference]
- **DOI/URL**: [link]
- **Type**: [journal article / book / report / web / conference paper / thesis / other]
- **Access Date**: [when verified]

---

### Track & Claim

- **Evidence grade track**: [ebm_design / ss_quantitative / ss_qualitative / humanities / neutral]
- **Claim class**: [causal_effect / descriptive_pattern / interpretive_meaning / theoretical_argument / methodological / policy_evaluative / unspecified]
- **Track resolution**: [from Domain Evidence Profile `<profile>` / scholar declaration / neutral default / `[CLAIM-TRACK-OVERRIDE]` …]
- **Advisories**: [none | `[NO-TRACK-NEUTRAL]` | `[TRACK-MIXED-DEFAULT]` | `[TRACK-COARSE-PROFILE]` | `[CLAIM-TRACK-OVERRIDE]` | …]
- **Multi-claim note**: [single claim | card N of M for this source — see `evidence_grade_tracks.md` §9]

> One card = one primary claim_class. Do not average fitness across claim classes.

---

### Quality Assessment

#### 1. Design code (descriptive — not an Overall weight)
**Design level code**: [I / II / III / IV / V / VI / VII / NA]
**Justification**: [why this design code]

#### 2. Evidence fitness (A–F under active track)
**Evidence fitness**: [A / B / C / D / F]
**Justification**: [track gold-standard comparison for the claim class — not “because Level n”]

#### 3. Publication Venue
- **Journal/Publisher**: [name]
- **Indexed in**: [Scopus / WoS / PubMed / DOAJ / other / none]
- **Impact Factor/CiteScore**: [value or N/A]
- **COPE member**: [Yes / No / Unknown]
- **Predatory indicators**: [None / Flags: list]

**Venue Grade (maps to Peer Review criterion)**: [Excellent / Good / Adequate / Questionable / Unacceptable]

#### 4. Author Credibility
- **Author(s)**: [names]
- **Affiliation(s)**: [institutions]
- **ORCID**: [if available]
- **Track record**: [publication history in field]
- **Expertise match**: [relevant to topic? Yes/Partial/No]

**Author Grade**: [Excellent / Good / Adequate / Unknown / Questionable]

#### 5. Methodological Quality
- **Design**: [description]
- **Sample / data adequacy** (track-conditioned): [ebm: size/representativeness · ss_quant: identification-relevant data quality · ss_qual/humanities: depth/corpus appropriateness]
- **Analysis**: [appropriate for design and claim class?]
- **Limitations acknowledged**: [Yes / Partially / No]
- **Replicable / transparent**: [Yes / Partially / No — tradition-appropriate]

**Method Grade**: [Excellent / Good / Adequate / Weak / Flawed]

#### 6. Currency
- **Publication year**: [YYYY]
- **Data collection period**: [if stated]
- **Field velocity**: [Rapid / Moderate / Slow / Foundational]
- **Still current**: [Yes / Conditionally / No]

**Currency Grade**: [Current / Acceptable / Dated / Outdated / Foundational]

#### 7. Conflict of Interest
- **Declared COI**: [None / Listed: details]
- **Funding source**: [source or Not stated]
- **Potential undeclared COI**: [None detected / Possible: details]

**COI Grade**: [Clean / Minor / Moderate / Significant / Critical]

---

### Overall Assessment

| Dimension | Grade |
|-----------|-------|
| Design code | [I–VII/NA] *(descriptive only)* |
| Evidence fitness | [A–F] |
| Peer Review (venue) | [A–F mapped from venue grade] |
| Methodology | [A–F] |
| Sample / data adequacy | [A–F] |
| Currency | [A–F] |
| Conflicts | [A–F] |
| **Overall** | **[A / B / C / D / F]** |

**Aggregation**: integrity floor → median of six A–F criteria → fitness +1 if Evidence fitness is A and Methodology ≠ F. Track clamps apply (`evidence_grade_tracks.md` §5). Design code is **not** a seventh median input.

**Track rationale**: [one line — e.g. "ss_qualitative: trustworthiness package met; Level VI is design code only"]

### Identification Audit (only if claim_class = causal_effect)
- Prefer short form from `shared/templates/identification_audit_card.md` for bibliography sources; full card for the scholar’s own manuscript (methodology reviewer).
- **ID short-form:** design=[…] estimand=[…] variation=[…] assumptions engaged=[yes/partial/no] diagnostics=[yes/partial/no] → verdict hint=[ready|needs design repair|not causal yet]
- Fitness A for causal_effect requires identification engagement (not design_code alone).

### Recommendation
- [ ] **Use as primary evidence** (Grade A-B)
- [ ] **Use as supporting evidence** (Grade B-C)
- [ ] **Use with explicit caveats** (Grade C-D)
- [ ] **Do not use** (Grade D-F) — Reason: [specific reason]

### Notes
[Any additional observations, caveats, or context]
```

## Batch Assessment Summary

```markdown
## Source Verification Summary

**Date**: [YYYY-MM-DD]
**Sources assessed**: [N]
**Assessor**: source_verification_agent
**Evidence grade track** (run-level default): [track | neutral + tag]

### Grade Distribution
| Grade | Count | % |
|-------|-------|---|
| A (Excellent) | X | X% |
| B (Good) | X | X% |
| C (Adequate) | X | X% |
| D (Weak) | X | X% |
| F (Unacceptable) | X | X% |

### Flagged Sources
| Source | Issue | Severity | Recommendation |
|--------|-------|----------|---------------|
| [ref] | [issue] | [High/Medium/Low] | [Include with caveat / Exclude]

### Predatory Journal Alerts
[List any flagged journals]

### Overall Source Base Quality
**Assessment**: [Strong / Adequate / Mixed / Weak]
**Recommendation**: [Proceed / Supplement / Major revision of source base needed]
```

## Usage Notes
- Complete one card per source for full verification
- Batch summary should be produced after all cards are complete
- Minimum spot-check: 20% of sources get full card assessment
- All Grade D/F sources require documented justification
- Any predatory journal flag requires full verification
- Under `ss_qualitative` / `humanities`, do not lower Overall solely because design code is VI/VII
- Under `ss_quantitative`, do not award causal Evidence fitness A solely from design code III without identification engagement
- Multi-claim sources: separate cards per claim_class; no cross-claim fitness averaging (`evidence_grade_tracks.md` §9)
- Absent profile/declaration → track `neutral` and emit `[NO-TRACK-NEUTRAL]` on the run summary
