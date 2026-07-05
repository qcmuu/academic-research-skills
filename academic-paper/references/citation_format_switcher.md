# Citation Format Switcher — Multi-Citation Format Switching

Quick-reference for switching between 8 citation formats. Used by `citation_compliance_agent` and `formatter_agent`. The social-science-track additions (APSA, Harvard, GB/T 7714) are marked (social-science-track).

## Format Comparison Matrix

### In-Text Citation Patterns

| Scenario | APA 7th | Chicago (Notes) | Chicago (Author-Date) | MLA 9th | IEEE | Vancouver | APSA (SS-track) | Harvard (SS-track) | GB/T 7714 (SS-track) |
|----------|---------|-----------------|----------------------|---------|------|-----------|-----------------|--------------------|----------------------|
| Single author | (Smith, 2024) | ¹ (footnote) | (Smith 2024) | (Smith 45) | [1] | ¹ (superscript) | (Smith 2024) | (Smith, 2024) | (Smith, 2024) / [1]² |
| Two authors | (Smith & Jones, 2024) | ¹ | (Smith and Jones 2024) | (Smith and Jones 45) | [1] | ¹ | (Smith and Jones 2024) | (Smith and Jones, 2024) | (Smith and Jones, 2024) |
| 3+ authors | (Smith et al., 2024) | ¹ | (Smith et al. 2024) | (Smith et al. 45) | [1] | ¹ | (Smith et al. 2024) | (Smith et al., 2024) | (Smith et al., 2024) |
| Direct quote | (Smith, 2024, p. 45) | ¹ | (Smith 2024, 45) | (Smith 45) | [1, p. 45] | ¹⁽ᵖ⁴⁵⁾ | (Smith 2024, 45) | (Smith, 2024, p. 45) | (Smith, 2024)⁴⁵ |
| Multiple works | (Chen, 2023; Smith, 2024) | ¹ ² | (Chen 2023; Smith 2024) | (Chen 12; Smith 45) | [1], [2] | ¹˒² | (Chen 2023; Smith 2024) | (Chen, 2023; Smith, 2024) | (Chen, 2023; Smith, 2024) |
| Order | Alphabetical | Order of appearance | Alphabetical | Alphabetical | Order of appearance | Order of appearance | Alphabetical | Alphabetical | Order of appearance (numbered) or alphabetical (author-date) |

² GB/T 7714 supports BOTH a numbered (顺序编码制, common in STEM Chinese journals) and an author-date (著者-年制, common in social-science Chinese journals) system — pick per venue.

### Reference List Naming

| Format | Section Title | Entry Order |
|--------|--------------|-------------|
| APA 7th | References | Alphabetical |
| Chicago (Notes) | Bibliography | Alphabetical |
| Chicago (Author-Date) | References | Alphabetical |
| MLA 9th | Works Cited | Alphabetical |
| IEEE | References | Order of appearance |
| Vancouver | References | Order of appearance |
| APSA | References | Alphabetical |
| Harvard | Reference List | Alphabetical |
| GB/T 7714 | 参考文献 (References) | Order of appearance (numbered) or alphabetical (author-date) |

## Format Details

### APA 7th Edition
**Discipline**: Education, Psychology, Social Sciences

**Journal Article**:
```
Smith, J. A., & Jones, B. C. (2024). Article title in sentence case.
    Journal Title in Title Case, 45(2), 123-145. https://doi.org/10.xxxx
```

**Book**:
```
Smith, J. A. (2024). Book title in sentence case (2nd ed.). Publisher.
```

**Key rules**: Hanging indent, DOI as URL, sentence case for titles, "&" before last author.

---

### Chicago 17th (Notes-Bibliography)
**Discipline**: History, Humanities, some Social Sciences

**Footnote (first citation)**:
```
1. John A. Smith and Betty C. Jones, "Article Title in Title Case,"
Journal Title 45, no. 2 (2024): 123, https://doi.org/10.xxxx.
```

**Footnote (subsequent)**:
```
2. Smith and Jones, "Article Title," 130.
```

**Bibliography entry**:
```
Smith, John A., and Betty C. Jones. "Article Title in Title Case."
    Journal Title 45, no. 2 (2024): 123-145.
    https://doi.org/10.xxxx.
```

**Key rules**: Full names, title case throughout, footnotes + bibliography, period after URL.

---

### Chicago 17th (Author-Date)
**Discipline**: Natural Sciences, some Social Sciences

**In-text**: (Smith 2024, 45)

**Reference**:
```
Smith, John A. 2024. "Article Title in Title Case." Journal Title
    45 (2): 123-145. https://doi.org/10.xxxx.
```

**Key rules**: Year after author name, full names in reference, title case.

---

### MLA 9th Edition
**Discipline**: Literature, Languages, Cultural Studies

**In-text**: (Smith 45) — author + page, no comma, no year

**Works Cited**:
```
Smith, John A., and Betty C. Jones. "Article Title in Title Case."
    Journal Title, vol. 45, no. 2, 2024, pp. 123-45.
```

**Key rules**: No year in in-text, page numbers always, containers model, no DOI in basic format (include if online), title case for all titles.

---

### IEEE
**Discipline**: Engineering, Computer Science, Technology

**In-text**: [1] — numbered brackets in order of appearance

**Reference**:
```
[1] J. A. Smith and B. C. Jones, "Article title in sentence case,"
    Journal Title, vol. 45, no. 2, pp. 123-145, Feb. 2024,
    doi: 10.xxxx.
```

**Key rules**: Numbered [N], initials before surname, abbreviated month, "doi:" prefix (not URL).

---

### Vancouver
**Discipline**: Medicine, Biomedical Sciences, Nursing

**In-text**: Superscript numbers ¹ or (1) in order of appearance

**Reference**:
```
1. Smith JA, Jones BC. Article title in sentence case. Journal Title.
   2024;45(2):123-145. doi:10.xxxx
```

**Key rules**: Numbered in order of appearance, no spaces in initials, abbreviated journal titles (per NLM), semicolon before volume, colon before pages.

---

### APSA — American Political Science Association (social-science-track)
**Discipline**: Political science, public administration

APSA is a modified Chicago Author-Date style adapted for political science. It drops the comma between author and year that Chicago uses, and uses an em-dash for repeated authors in the reference list.

**In-text**: (Smith 2024) — no comma between author and year; (Smith and Jones 2024); (Smith et al. 2024); (Smith 2024, 45) for direct quotes.

**Reference**:
```
Smith, John A. 2024. "Article Title in Sentence Case." *Journal Title in
Title Case* 45 (2): 123–45. https://doi.org/10.xxxx.
```

**Repeated author**: use a 3-em dash `———.` in place of the author name for the second and subsequent works by the same author.

**Key rules**: Author comma year (no comma in in-text), italics for journal title, en-dash in page ranges, italics for book titles, headline-style capitalization for titles.

---

### Harvard — Author-Date (social-science-track)
**Discipline**: General social sciences, business, education (especially UK/AU institutions)

Harvard is a family of author-date styles (not a single canonical standard — institutions vary). The form below is the most common convention; check the target institution's house variant.

**In-text**: (Smith, 2024) — comma between author and year; (Smith and Jones, 2024); (Smith et al., 2024); (Smith, 2024, p. 45) for direct quotes.

**Reference**:
```
Smith, J.A. (2024) 'Article title in sentence case', *Journal Title in
Title Case*, 45(2), pp. 123–145. Available at: https://doi.org/10.xxxx
(Accessed: DD Month YYYY).
```

**Key rules**: Author comma year (with comma in in-text), single quotes for article titles, italics for journal/book titles, "pp." before pages, "Available at:" for URLs (the distinguishing Harvard convention vs APA), Accessed date for online sources.

> Because Harvard has no single authority, **always confirm the target venue's house style** before finalizing. The variant above is the most widely taught.

---

### GB/T 7714-2015 — Chinese National Standard (social-science-track)
**Discipline**: Chinese-language venues across all disciplines; required by most Chinese journals and degree-granting institutions.

GB/T 7714 supports two systems — select per venue:
- **顺序编码制 (numeric / order-of-citation)** — common in STEM Chinese journals
- **著者-年制 (author-date)** — common in social-science and humanities Chinese journals

> See `references/gbt7714_style_guide.md` for the full rules including Chinese-vs-Western author handling, document-type codes, and bilingual citation rules. The summary below is the quick reference.

**Numeric in-text**: `[1]` or `[1-3]` in order of appearance
**Author-date in-text**: `(Smith, 2024)` / `(张三, 2024)`

**Reference (numeric, journal article)**:
```
[1] SMITH J A, JONES B C. Article title in sentence case[J]. Journal
    Title, 2024, 45(2): 123-145.
[2] 张三, 李四. 文章题名[J]. 期刊名, 2024, 45(2): 123-145.
```

**Document-type codes** (in brackets after the title): `[J]` journal, `[M]` monograph/book, `[C]` conference proceedings, `[D]` dissertation, `[R]` report, `[N]` newspaper article, `[EB/OL]` electronic/online.

**Key rules**: Surname-space-initials (no period between, comma between authors), uppercase Western surnames in numeric mode, document-type tag mandatory, year-volume(issue):pages punctuation differs from Western styles, Chinese names kept as-is (no inversion).

## Conversion Quick Reference

### APA → Chicago (Notes-Bibliography)
1. Change in-text (Author, Year) → footnotes
2. Expand first names in reference list
3. Change sentence case → title case for article titles
4. Add period after URLs
5. Rename "References" → "Bibliography"

### APA → MLA
1. Remove years from in-text, add page numbers
2. Expand first names, change "&" → "and"
3. Change format: vol., no., year order
4. Remove DOIs (unless online-only source)
5. Rename "References" → "Works Cited"

### APA → IEEE
1. Change (Author, Year) → [N] numbered brackets
2. Reorder references by appearance (not alphabetical)
3. Change to initials-first format
4. Add "doi:" prefix to DOIs
5. Abbreviate month names

### APA → Vancouver
1. Change (Author, Year) → superscript numbers
2. Reorder references by appearance
3. Remove spaces between initials
4. Abbreviate journal titles (NLM catalog)
5. Use semicolons/colons for volume/page separators

## Chinese Citation Format Switching

### APA 7.0 Chinese Format

For complete specifications, see `apa7_chinese_citation_guide.md`. Below is a quick reference.

**Chinese journal article**:
```
Wang, Da-Ming, & Li, Xiao-Hua (2024). Article title. Journal Name, Volume(Issue), Pages. https://doi.org/xxxxx
```

**Chinese book**:
```
Zhang, San (2023). Book title. Publisher.
```

**Government publication**:
```
Ministry of Education (2024). Publication title. https://url
```

### Mixed Chinese-English Reference Handling

**In-text citations**:
- Chinese uses full-width parentheses: (Author, Year)
- English uses half-width parentheses: (Author, Year)
- Chinese multiple authors use enumeration comma; English uses &

**Reference list ordering**:

| Option | Description | Applicable Scenario |
|------|------|---------|
| **Option A (Recommended)** | Chinese first (ordered by stroke count), English after (ordered alphabetically) | Convention for most Taiwan journals |
| **Option B** | Mixed Chinese-English ordering (unified stroke count / alphabetical) | Some international journals |

**Same author with both Chinese and English works**: List separately — Chinese works go in the Chinese section, English works go in the English section.

### Format Conversion Notes (Chinese Papers)

**Chinese APA → Chicago**:
1. Publication format differs (APA 7 does not require publication location, Chicago does)
2. Change titles to "title case" format
3. Add footnote citation system

**Chinese APA → IEEE**:
1. Add numbered labels [N]
2. Remove year from after author position
3. Order by citation appearance (not stroke count)

**Chinese paper format conventions**:
- Most Taiwan journals use APA
- Humanities disciplines (history, literature) occasionally use Chicago
- Engineering/CS fields mostly use IEEE
- Medical fields use Vancouver

---

## AI-Generated Content Citation (by Format)

| Format | How to Cite AI |
|--------|---------------|
| APA 7th | OpenAI. (2024). ChatGPT (Version 4) [Large language model]. https://chat.openai.com |
| Chicago | OpenAI. ChatGPT. Version 4. 2024. Large language model. https://chat.openai.com. |
| MLA | "ChatGPT response to [prompt description]." OpenAI, 15 Mar. 2024, chat.openai.com. |
| IEEE | [N] OpenAI, "ChatGPT," ver. 4, 2024. [Online]. Available: https://chat.openai.com |
| Vancouver | OpenAI. ChatGPT [Large language model]. 2024. Available from: https://chat.openai.com |
