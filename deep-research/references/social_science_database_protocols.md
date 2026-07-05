# Social Science Database Search Protocols

**Status**: social-science-track Stage 3
**Used by**: `bibliography_agent` (search strategy), `research_architect_agent` (database planning)
**Companion**: `shared/social_science_config.md` §3 (discipline → database mapping)

---

## Purpose

The default ARS stack (Semantic Scholar, OpenAlex, Crossref, arXiv) is **insufficient for social sciences** — arXiv has near-zero coverage of sociology/anthropology/communication, and Semantic Scholar under-indexes non-Anglophone and humanities-adjacent work. This document gives `bibliography_agent` the search-strategy details for the social-science-primary databases so it can build a complete search when the PCR `Discipline` falls in a social-science cluster.

> These databases are **discovery layer** (build the candidate set). Verification still runs through the existing S2/OpenAlex/Crossref/arXiv stack via `source_verification_agent`. Where a database has no public free API, discovery is **manual / institutional-access** — the agent constructs the search string and documents it; it does NOT fabricate retrieved records.

---

## 1. Web of Science (SSCI / SCI) — Thomson Reuters / Clarivate

**Coverage**: Social Sciences Citation Index (SSCI) is the canonical interdisciplinary social-science citation index. Strong on sociology, political science, communication, economics, public administration.

**Access**: Institutional subscription only. No public free API.

### Search strategy
```
Database: Web of Science Core Collection → SSCI (filter)
Topic field (TS) syntax:
  TS=("concept A" OR "synonym A1") AND TS=("concept B")
  Refine by: Web of Science Category (e.g. Sociology, Political Science,
             Communication), Document Type=Article, Year range, Language
Citation chaining: use the "Citing Articles" + "Cited References" features
```

### Construction rules
- Use **TS=** (Topic, searches title + abstract + keywords + Keywords Plus).
- Combine with the database's subject category filter rather than relying only on Boolean terms.
- Record the exact query string + the count of hits per iteration for the PRISMA/strategy report.
- WOS field tags: `TS=` topic, `TI=` title, `AU=` author, `SO=` source/journal, `PY=` year.

### Document for the strategy report
- The full Boolean string (one database, verbatim)
- The filters applied (category, document type, date)
- Hits per iteration (identified → after dedup → after screening)

---

## 2. Scopus — Elsevier

**Coverage**: Broadest multidisciplinary abstract-and-citation database; stronger than SSCI in communication, management, economics, and recent working papers. Good coverage of non-U.S. journals.

**Access**: Institutional subscription. Has a paid API (`api.elsevier.com`); not assumed available.

### Search strategy
```
Database: Scopus
Query syntax:
  TITLE-ABS-KEY("concept A" OR "synonym A1") AND TITLE-ABS-KEY("concept B")
  AND ( LIMIT-TO(SUBJAREA,"SOCI") OR LIMIT-TO(SUBJAREA,"BUSI")
        OR LIMIT-TO(SUBJAREA,"ECON") OR LIMIT-TO(SUBJAREA,"DECI") )
  AND PUBYEAR > 2014  AND ( LIMIT-TO(DOCTYPE,"ar") OR LIMIT-TO(DOCTYPE,"re") )
```

### Construction rules
- `TITLE-ABS-KEY` = title + abstract + indexed keywords.
- Use `SUBJAREA` codes for discipline scoping: SOCI (Sociology), BUSI (Business), ECON (Economics), DECI (Decision Sciences), PSYC (Psychology), ARTS (Arts & Humanities), SOCI (Social Sciences).
- `DOCTYPE`: ar=article, re=review, cp=conference paper, ch=book chapter, wp=working paper (where indexed).

---

## 3. SSRN — Social Science Research Network

**Coverage**: Working papers in economics, finance, law, political science, management. **Critical for `social_science_quantitative` profile** — peer review in these fields often lags the working-paper circulation by 1-3 years.

**Access**: Free registration; full text often free. No structured public API; discovery via the website search.

### Search strategy
```
Network: select the relevant SSRN subnetwork (FEN=Financial Economics,
         PSN=Political Science, etc.)
Search fields: title + abstract + keywords
Filters: date range, network/subnetwork, subject classifications (e.g. JEL codes for economics)
```

### Construction rules
- For economics/finance: **attach JEL classification codes** (e.g. JEL: J62 for labor mobility) to disambiguate.
- Working papers MUST be tagged as `working_paper` in the bibliography and cross-checked against the published version when one exists (note: SSRN → journal version may differ in title/findings).
- Combine with NBER working papers (economics) for fuller coverage.

### Provenance note for the Material Passport
- Record SSRN paper ID + date-of-access; the same finding may be revised between SSRN and journal publication.

---

## 4. JSTOR — Multidisciplinary archive

**Coverage**: Deep archive of core sociology, anthropology, political science, history journals. **Strong for canonical/foundational texts** that `humanities_interpretive` and `social_science_qualitative` profiles should admit regardless of recency.

**Access**: Institutional; some open content. No general public API.

### Search strategy
```
Search across: title + abstract + full text
  (ft:full-text search is JSTOR's distinctive strength)
Filters: discipline cluster, journal title, date, item type
```

### Construction rules
- Use **full-text search** (not just metadata) to surface canonical texts whose title/abstract may be terse.
- Filter by JSTOR's discipline clusters: Sociology, Political Science, Anthropology, Communication Studies, Economics.
- Note the "moving wall" (recent 3-5 years often not included) — supplement with current-issue databases.

---

## 5. EconLit — AEA / economics

**Coverage**: Authoritative economics index (journal articles, working papers, books, dissertations). **Primary for `social_science_quantitative` when the discipline is economics.**

**Access**: Institutional (often via EBSCO or ProQuest platform).

### Search strategy
```
Platform: EBSCOhost or ProQuest (institutional)
Fields: TI title, AB abstract, SU subject, DE descriptor
Subject descriptors: AEA JEL classification codes
  e.g. DE "Labor Mobility" or JEL J6
```

### Construction rules
- Use **JEL codes** as the primary scoping device — economics literature is organized by them.
- Combine with RePEc/IDEAS for free working-paper discovery.

---

## 6. NBER Working Papers — National Bureau of Economic Research

**Coverage**: U.S. economics working papers; many become top-5 journal articles.

**Access**: Free; full text free. RSS + a basic site search.

### Search strategy
- Browse by **NBER program** (Children, Economics of Education, Labor Studies, Public Economics, Political Economy, etc.).
- Site search on title + abstract.

---

## 7. ProQuest (Sociological Abstracts / Worldwide Political Science Abstracts)

**Coverage**: Discipline-specific abstracting services — Sociological Abstracts (sociology), Worldwide Political Science Abstracts (political science), Communication Abstracts.

**Access**: Institutional. No public free API.

### Construction strategy
- Use the discipline-specific database rather than the generic ProQuest Central for focused searches.
- Field: subject descriptors + thesaurus terms (thesaurus-controlled vocabulary is the discipline's organizing device).

---

## Database selection by social-science cluster (summary)

| Cluster | Primary (discovery) | Secondary | Verification |
|---|---|---|---|
| Sociology (any) | WoS SSCI, Sociological Abstracts (ProQuest) | Scopus, JSTOR | S2/OpenAlex/Crossref |
| Anthropology | JSTOR, AnthroSource | WoS SSCI, Scopus | Crossref/OpenAlex |
| Political science & public admin | WoS SSCI, Worldwide Political Science Abstracts (ProQuest) | SSRN, Scopus | S2/OpenAlex/Crossref |
| Economics & management | EconLit, SSRN, NBER | WoS SSCI, Scopus, RePEc | S2/OpenAlex/Crossref |
| Communication / journalism | WoS SSCI, Communication Abstracts (ProQuest) | Scopus, JSTOR | S2/OpenAlex/Crossref |

> The default ARS discovery flow (Semantic Scholar search) is **supplementary** for social science, not primary. `bibliography_agent` should present the discipline-appropriate primary database first in the search-strategy report and note where institutional access is required.
