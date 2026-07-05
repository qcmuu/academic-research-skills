---
rubric_version: "1.0"
reporting_standards: "SRQR (O'Brien et al., 2014); CASP Qualitative Checklist item 6; ENTREQ"
license: CC-BY-NC 4.0
---

# Reflexivity & Positionality Rubric

**Status**: v1.0 (social-science-track Stage 6, 2026-07)
**Source**: This rubric operationalizes the reflexivity / positionality reporting expectations codified in **SRQR** (O'Brien et al., 2014, *Standards for Reporting Qualitative Research*, researcher-characteristics & reflexivity items), **CASP Qualitative Checklist item 6** ("Has the relationship between researcher and participants been adequately considered?"), and **ENTREQ**. These are EQUATOR-Network reporting standards, not a single empirical paper; the rubric is the ARS synthesis of their shared expectations.
**Canonical location**: `shared/reflexivity_rubric.md` in `Imbad0202/academic-research-skills`. External consumers should reference by stable URL; do not vendor (bump the `rubric_version` field on any modification).

---

## Why this rubric exists

The upstream ARS suite enforces statistical rigor, citation integrity, and reporting-completeness checks, but it does not surface **positionality and reflexivity** — a core reporting expectation for interpretive, qualitative, and critical social-science research. An ethnography that omits a positionality statement is not "wrong" by quantitative-rigor standards, but it falls short of its own tradition's reporting norm (SRQR reflexivity items; CASP item 6). This rubric gives `reflexivity_agent` a canonical, advisory-only checklist so the gap is visible without becoming a blocking veto.

**Advisory-only by design.** Like `collaboration_depth_rubric.md`, this rubric scores nothing that enters a blocking criterion. A finding here surfaces a reporting-standard gap; the scholar decides whether and how to address it.

---

## Profile-gated intensity

The check's intensity is calibrated by the work's `Domain Evidence Profile` (when set) and its actual method. The rubric is **never fully silent** — even a design where positionality is not a live concern gets a one-line note rather than an absent report.

| Profile / method | Intensity |
|---|---|
| `social_science_qualitative`, `humanities_interpretive`, qualitative method (ethnography / interviews / grounded theory / discourse / action research) | **Full** — all five dimensions; absence of a positionality statement is a substantive finding |
| `communication_mixed`, mixed methods with a qualitative strand | **Full** on the qualitative strand only |
| `social_science_quantitative`, `cs_ml`, quantitative / experimental / causal-inference method | **Light** — flag only researcher-discretion points (variable construction, sample framing); else "not a live concern" |
| `unknown_user_defined` / design not yet determined | **Light** early; escalate if a qualitative method emerges |

---

## The five dimensions

Each dimension is checked as **present / partial / absent**, with a one-line evidence pointer (manuscript section or quoted phrase). The dimensions map to named reporting-standard items so a finding is grounded, not a vague preference.

### 1. Positionality statement
Does the work declare the researcher's standpoint — gender, race, class, institutional position, relationship to the studied community — where the tradition expects it? An unmarked "view from nowhere" is a finding for interpretive work.
- **Maps to**: SRQR "researcher characteristics and reflexivity" item; common expectation in ethnography, feminist research, critical race research, action research.
- **Present**: a named standpoint statement (one paragraph to a dedicated section) that engages how the researcher is positioned relative to the topic/participants.
- **Partial**: the work acknowledges position implicitly (e.g., "as a former practitioner…") but does not develop its analytic implications.
- **Absent**: no positionality acknowledgment where the tradition expects one.

### 2. Researcher-effect disclosure
Does the work acknowledge how the researcher's presence, choices, or prior commitments may have shaped the data — access gained or denied, what participants felt safe to say, what was coded as salient?
- **Maps to**: CASP item 6 ("relationship between researcher and participants"); SRQR reflexivity.
- **Present**: a concrete discussion of researcher effect on the data (not a generic disclaimer).
- **Partial**: a generic "researcher bias may have influenced findings" without specifics.
- **Absent**: no acknowledgment.

### 3. Cultural sensitivity
Does the work engage the cultural context of the participants / site on its own terms, rather than imposing an outside frame? Are translation, emic terms, and local meanings handled carefully?
- **Maps to**: SRQR context item; ethnographic norms; cross-cultural research ethics.
- **Present**: emic terms retained and glossed; translation choices explained; local meaning foregrounded.
- **Partial**: some contextual engagement but with imposed outside categories.
- **Absent**: cultural context treated as transparent or ignored.

### 4. Power asymmetry
Does the work address power differences between researcher and researched — consent under asymmetry, whose interests the research serves, who benefits? Particularly load-bearing for work with vulnerable or minoritized communities.
- **Maps to**: research-ethics norms for community-based and participatory work; feminist standpoint methodology.
- **Present**: power asymmetry named and engaged (who holds it, how it shapes consent and findings).
- **Partial**: a consent-form-style ethics statement without engaging asymmetry's analytical consequences.
- **Absent**: no engagement with power asymmetry where it is a live concern (community / minoritized / vulnerable research).

### 5. Member checking / respondent validation
Where the tradition expects it, were findings taken back to participants for confirmation or refinement?
- **Maps to**: trustworthiness criterion (credibility via member checking); not all traditions require it (ethnomethodology, some Conversation Analysis, some CDA do not).
- **Present**: member checking conducted and reported (who, how, what changed), OR a justified statement of why it was not appropriate for this tradition.
- **Partial**: member checking mentioned but not reported in enough detail to evaluate.
- **Absent / N/A**: not conducted where the tradition expects it AND no justification given; OR a tradition where it is not expected (correctly marked N/A).

---

## Verdict aggregation

The agent emits one of four verdicts, derived from the dimension pattern but not a mechanical formula:

| Verdict | When |
|---|---|
| **Affirmative — positionality adequately surfaced** | All warranted dimensions present (or justifiably N/A) |
| **Partial — some dimensions present, gaps noted** | Mix of present / partial; no dimension that the tradition treats as load-bearing is fully absent |
| **Advisory finding — under-surfaced** | One or more load-bearing dimensions absent where the tradition expects them (e.g., no positionality statement in an ethnography) |
| **Not a live concern for this design** | Light-check designs (positivist / experimental / causal-inference) where positionality is not a tradition expectation |

The verdict is **advisory**. It does not enter any blocking criterion, does not change the A-F grade, and does not gate output. It is reported alongside the checkpoint presentation and the Process Record.
