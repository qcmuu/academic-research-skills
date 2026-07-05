# CNKI (中国知网) Search Protocol — Chinese Social-Science Ecology

**Status**: social-science-track Stage 8
**Used by**: `bibliography_agent` (search strategy for Chinese social-science topics)
**Companion**: `references/social_science_database_protocols.md` (Western databases); `shared/social_science_config.md` §3

---

## Purpose

CNKI (China National Knowledge Infrastructure, 中国知网) is the **primary discovery database for Chinese-language academic literature**, covering ~95% of Chinese academic journals and the CSSCI / Peking-University-Core / CSTPCD indexing subsets. For Chinese social-science research it is non-substitutable — the Western databases in `social_science_database_protocols.md` (WoS SSCI, Scopus) under-index Chinese journals. This document gives `bibliography_agent` the CNKI search-strategy details: database subsetting, query syntax, and the CSSCI vs CSTPCD vs 北大核心 distinction.

> CNKI is **discovery layer** with no public free API (institutional access only). The agent constructs and documents the Boolean query string + subset filters; it does NOT fabricate retrieved records. Verification still runs through Crossref/OpenAlex/S2 where a DOI exists, but most CNKI-indexed Chinese articles lack DOIs — record "CNKI institutional search documented; [N] hits recorded by scholar" where the search must be run manually.

---

## 1. Database subsetting — the index-distinction that matters most

CNKI's content spans several quality tiers indexed by different "核心期刊" (core-journal) lists. **Always scope to the relevant index subset** — an unscoped CNKI search returns a flood of low-quality results. The three lists relevant to social science:

| Index | Full name | Coverage | When to scope to it |
|---|---|---|---|
| **CSSCI** (南大核心) | 中文社会科学引文索引 | ~500 top Chinese social-science journals; the social-science gold standard | Default for sociology, political science, communication, economics, management, education research in Chinese |
| **北大核心** (PKU Core) | 《中文核心期刊要目总览》 | Broader multidisciplinary core (~2000 journals); broader than CSSCI | Use when CSSCI is too narrow (e.g. an interdisciplinary or applied topic) or for non-CSSCI disciplines (medicine, engineering) cited in a social-science paper |
| **CSTPCD** (统计源) | 中国科技论文与引文数据库 | Science/technology focus | Rarely relevant for social science; use only for STEM-adjacent work |

> **Decision rule for Chinese social science**: scope the search to **CSSCI** first; expand to **北大核心** if the topic is interdisciplinary or applied. Never run an unscoped CNKI search for a literature review.

---

## 2. Search syntax

CNKI's advanced search uses field-specific search boxes (not a single Boolean string like WoS). The agent documents the field-by-field construction:

```
Database: CNKI 学术期刊 (Academic Journals)
Source scope: CSSCI (南大核心) [or 北大核心 if interdisciplinary]
Topic fields (主题 = title + abstract + keywords):
  主题 = ("概念A" OR "同义词A1") AND 主题 = ("概念B")
Filters:
  - 时间 (Year range): e.g. 2014-2024
  - 学科 (Discipline category): e.g. 社会学 / 政治学 / 新闻与传媒
  - 来源类别 (Source category): CSSCI / 北大核心 / CSTPCD
  - 支持基金 (Funding): optional
```

### Field tags (CNKI advanced search)
- `SU=` 主题 (Topic — title + abstract + keywords, the primary field)
- `TI=` 篇名 (Title)
- `KY=` 关键词 (Keywords)
- `AB=` 摘要 (Abstract)
- `AU=` 作者 (Author)
- `AF=` 机构 (Affiliation)
- `PT=` 来源期刊 (Source journal)

### Chinese-keyword handling notes
- **Synonym expansion is critical**: Chinese academic concepts have variant renderings (e.g. "社交媒体" / "社会化媒体" / "社交网络"; "农民工" / "进城务工人员"). Build a synonym set per concept.
- **English term inclusion**: many Chinese social-science papers index English terms in keywords — include the English term in the search (e.g. "platform economy" alongside "平台经济").
- **Boolean in CNKI**: use the AND/OR/NOT dropdowns in advanced search; CNKI does not parse inline Boolean operators reliably across all interfaces.

---

## 3. Citation chaining on CNKI

CNKI's "引文网络" (citation network) feature supports:
- **参考文献** (this article's references) — backward chaining
- **引证文献** (articles citing this one) — forward chaining
- **相似文献** (similar articles) — recommend-based expansion

Use these the way you'd use WoS "Cited References" / "Citing Articles" — for citation-chaining rounds after the initial Boolean search.

---

## 4. Documenting the search (for the PRISMA/strategy report)

For a Chinese-social-science review, the search-strategy report must include:
1. **Database + subset**: "CNKI 学术期刊, scoped to CSSCI (南大核心)" — never just "CNKI".
2. **Exact field-by-field query**: the topic/title/keyword strings + Boolean operators.
3. **Filters applied**: year range, discipline category, source category.
4. **Hits per iteration**: identified → after dedup (含去重) → after screening (初筛后) → full-text (精读).
5. **Cross-database note**: if searched CNKI AND a Western database (WoS SSCI), note the overlap handling (some Chinese journals are dual-indexed).

> **Provenance for the Material Passport**: record the CNKI search date + the scholar's institutional access context. CNKI article URLs are session-bound; cite by the article's permanent CNKI ID (e.g. `10.1234/abc` style or the CNKI accession number), not a session URL.

---

## 5. Coverage gaps to flag

CNKI is comprehensive for Chinese journals but has known gaps the agent should surface:
- **No preprint coverage**: Chinese social science has no arXiv equivalent; working papers circulate informally. Flag if the review needs working-paper currency.
- **Dissertation coverage**: CNKI indexes Chinese dissertations (博硕士论文) — include this source type if the topic is thesis-heavy.
- **Non-mainland sources**: CNKI under-indexes Taiwan (TSSCI), Hong Kong, and overseas-Chinese scholarship. For these, supplement with TSSCI / Airiti Library / HyRead.
- **No DOIs on most articles**: CNKI articles often lack DOIs, so the `source_verification_agent` S2/OpenAlex/Crossref stack will return `unresolvable` for them — this is expected, not a fabrication signal. Mark such entries `obtained_via: cnki_institutional` in the corpus so the contamination check exempts them (mirrors the `obtained_via: manual` exemption).
