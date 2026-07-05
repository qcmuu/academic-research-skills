# Chinese Social-Science Writing Conventions

**Status**: social-science-track Stage 8
**Used by**: `draft_writer_agent`, `abstract_bilingual_agent`, `formatter_agent` (when `Body Language` = zh-CN or Bilingual)
**Companion**: `references/gbt7714_style_guide.md` (citation); `deep-research/references/cnki_protocol.md` (discovery)

---

## Purpose

Chinese-language social-science venues (CSSCI-indexed; see `top_journals_by_field.md` §Mainland China) have structural conventions that differ from English APA-IMRaD in several load-bearing ways. This document gives the writing-side agents the conventions so a Chinese manuscript draft meets venue expectations rather than reading as a translated English paper. GB/T 7714 citation (Stage 4) handles reference formatting; this file handles everything else.

---

## 1. Title (标题)

- **Concise + declarative**: Chinese social-science titles favor declarative noun phrases or "研究" (study) / "分析" (analysis) suffixes over the English colon-separated title+subtitle form.
  - ✅ `平台经济中的劳动者控制研究` (A study of labor control in the platform economy)
  - ⚠️ Avoid overusing the English `Title: Subtitle` colon form unless the venue uses it.
- **No title-case concept**: Chinese has no capitalization; title "prominence" comes from concision and the declarative form.
- **Length**: typically ≤ 20 Chinese characters for the main title; longer work uses a subtitle after a dash `——` (Chinese em-dash), not a colon.

## 2. Abstract (摘要) and Keywords (关键词)

### 摘要 structure
Chinese social-science abstracts are usually **one paragraph, 200–400 characters**, covering: 研究问题 (RQ) → 方法 (method) → 发现 (findings) → 贡献 (contribution). Unlike APA, they are often **not structured** (no 研究背景/方法/结果/结论 labels) for theoretical/qualitative work, but **may be structured** for empirical work — check the venue.

### 关键词
- **3–5 keywords**, separated by semicolons (；), not commas.
- Keywords are usually drawn from the title and core concepts; include both the Chinese term and its accepted English equivalent where the venue is bilingual.
- Example: `平台经济；劳动关系；算法控制；外卖骑手 (platform economy; labor relations; algorithmic control; food-delivery riders)`

### 中图分类号 (CLC classification) + 文献标识码
Many CSSCI journals require:
- **中图分类号** (Chinese Library Classification number) — a discipline-specific code (e.g. C913.2 for labor sociology). Look up in the CLC tables; the agent should propose one and the scholar confirms.
- **文献标识码** (Document identifier code) — `A` (理论性论文/理论研究), `B` (应用性论文), `C` (综述), `D` (一般性动态). Default `A` for theoretical research articles.

## 3. Section structure — Chinese conventions vs English IMRaD

| English IMRaD | Chinese social-science convention |
|---|---|
| Introduction | 一、引言 (or 一、问题的提出 — "the problem posed") |
| Literature Review | 二、文献综述 / 二、文献回顾与研究空间 |
| Method | 三、研究方法 / 三、研究设计 |
| Results | 四、研究发现 / 四、结果与分析 |
| Discussion | 五、讨论 (sometimes merged into 四) |
| Conclusion | 六、结论与展望 / 六、结论 |

### Numbering conventions
- **Chinese numerals for top-level sections** (一、二、三) — not Arabic `1. 2. 3.` — in most CSSCI humanities/social-science venues. Some empirical venues use Arabic; check the venue.
- **Subsections**: （一）（二）（三）(Chinese-paren numerals) or `1.` `2.` depending on venue.
- **Fourth level**: `1.` or `（1）`.

> This is a frequent tell of a translated English paper: Arabic `1. 2. 3.` top-level numbering where the venue expects 一、二、三. Match the venue.

## 4. 基金项目标注 (Funding acknowledgment) — fixed format

CSSCI journals require a **strict funding-acknowledgment format** in a footnote or an opening section. The standard form:

```
基金项目：国家社会科学基金一般项目"XXXXXXXX"（项目编号：21BSH001）
国家自然科学基金面上项目"XXXXXXXX"（项目编号：72172001）
```

- **"基金项目："** label, then the **full funding-body name + project tier + exact project title in quotes** + **（项目编号：XXX）**.
- Multiple grants each get their own line.
- Place: first-page footnote (most common) or a 基金项目 section after the abstract.

### Common funding-body full names (use the full name, not abbreviations, on first mention)
- 国家社会科学基金 (National Social Science Fund) — 一般项目 / 重点项目 / 青年项目 / 重大项目
- 国家自然科学基金 (National Natural Science Foundation) — 面上项目 / 青年项目 / 重点项目
- 教育部人文社会科学研究项目 (MOE Humanities & Social Sciences)
- 中国博士后科学基金 (China Postdoctoral Science Foundation)

## 5. Citations in Chinese prose

- **作者 + 年份** in author-date systems: `(张三, 2024)` or `张三(2024)指出……`.
- **Multiple authors**: `(张三, 李四, 2024)`; 3+ uses `等`: `(张三等, 2024)`.
- **Numeric system**: `[1]` superscript or inline at the end of the clause before the period: `……研究表明这一效应[1]。`
- **Quoting Chinese sources**: use Chinese quotation marks 「」 or 『』 (some venues) or the standard "" for direct quotes; page reference as `[1]23` or `(张三, 2024: 23)`.

## 6. Author affiliation and biography

CSSCI venues require a **first-page footnote** with:
- **作者简介** (Author bio): 姓名 (name), 性别 (gender), 出生年 (birth year), 民族 (ethnicity, optional), 籍贯 (native place, optional), 单位 (affiliation), 职称 (title), 研究方向 (research direction), often 学位/学历 (degree).
  - Example: `作者简介：张三（1985—），男，山东济南人，北京大学社会学系副教授，博士，研究方向：劳动社会学。`
- **通讯作者** (Corresponding author) marker if applicable.

> This first-page-footnote bio block is a near-universal CSSCI requirement and a tell of a non-localized draft when missing.

## 7. Common localization errors to flag

| Error | Why it's wrong | Fix |
|---|---|---|
| `1. 2. 3.` top-level sections where venue uses 一、二、三 | Reads as a translated English paper | Convert to Chinese numerals per venue |
| No 基金项目 / 作者简介 first-page footnote | CSSCI requires both | Add the standard-format blocks |
| APA `(Smith, 2024, p.45)` in a GB/T 7714 manuscript | Citation style mismatch | Convert to `(Smith, 2024: 45)` or `[1]45` |
| Colon-separated title `Title: Subtitle` | Non-idiomatic in Chinese | Use `——` (em-dash) subtitle form |
| "Abstract:" / "Keywords:" English labels in a zh-CN manuscript | Localization leftover | Use 摘要 / 关键词 |
| No 中图分类号 where the venue requires one | Incomplete submission | Propose a CLC code for scholar confirmation |
| Translated English hedging ("可能在一定程度上……") overused | Reads as machine translation; Chinese academic prose is more direct | Use natural Chinese hedging or state findings plainly |

## 8. Bilingual (中英文) handling

For bilingual venues (common in CSSCI + international-facing journals):
- **Chinese is the primary text**; English abstract + title + keywords are the secondary, **matching** translation — not the source.
- **Author names**: provide both 张三 and the romanization (Zhang San) per the author's preferred form (not automatic pinyin for names with established romanizations).
- **Bibliography**: Chinese references in GB/T 7714 format; Western references in their native format (APA/Chicago/etc.) per the venue's rule — do not force Western references into GB/T 7714 unless the venue requires it.
- **Translation faithfulness**: the English abstract must reflect the Chinese findings, not introduce claims absent from the Chinese text (a reviewer-attention point).
