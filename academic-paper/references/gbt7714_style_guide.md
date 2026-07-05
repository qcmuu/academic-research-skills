# GB/T 7714-2015 Citation Style Guide — Chinese National Standard

**Status**: social-science-track Stage 4
**Used by**: `citation_compliance_agent`, `formatter_agent`
**Companion**: `references/citation_format_switcher.md` (§GB/T 7714 quick reference)

---

## Purpose

GB/T 7714-2015《信息与文献 参考文献著录规则》is the Chinese national standard for bibliographic citation, required by most Chinese journals and degree-granting institutions. It differs from Western styles in author formatting, document-type tagging, and the dual numeric/author-date system. This guide gives `citation_compliance_agent` and `formatter_agent` the rules needed to format and verify GB/T 7714 references, including the Chinese-vs-Western author distinction that trips automated converters.

## 1. Two systems — choose per venue

| System | Chinese name | When used | In-text |
|---|---|---|---|
| Numeric | 顺序编码制 | STEM Chinese journals (most) | `[1]`, `[1-3]` in order of appearance |
| Author-date | 著者-年制 | Social-science & humanities Chinese journals | `(Smith, 2024)`, `(张三, 2024)` |

The reference list ordering follows the system: numeric → order of appearance; author-date → alphabetical (Western) / stroke or pinyin order (Chinese).

## 2. Author formatting (the distinctive rules)

### Western authors
- **Numeric mode**: Surname space initials, UPPERCASE surname, no period between initials, comma between authors.
  - `SMITH J A, JONES B C` (NOT `Smith, J.A., Jones, B.C.`)
- **Author-date mode**: Surname comma initials, normal case.
  - `Smith J A, Jones B C` or `Smith, J. A., Jones, B. C.` (venue-dependent; confirm)
- **3+ authors**: list the first 3, then `, et al.` (Western) or `, 等` (Chinese).

### Chinese authors
- Names are **kept as-is, no inversion** (Chinese order is already surname-first): `张三`, `李四`.
- Multiple Chinese authors: `张三, 李四, 王五`.
- 3+ authors: list first 3 then `等` (e.g. `张三, 李四, 王五, 等`).

### Mixed Chinese-Western authorship
- Keep each author in their native format, comma-separated: `张三, SMITH J A`.

## 3. Document-type tags (mandatory)

Every reference ends its title with a document-type tag in square brackets. Omitting it is a common error.

| Tag | Document type |
|---|---|
| `[J]` | Journal article |
| `[M]` | Monograph / book |
| `[C]` | Conference proceedings / collected works (论文集) |
| `[G]` | Compilation (汇编) |
| `[N]` | Newspaper article |
| `[D]` | Dissertation (学位论文) |
| `[R]` | Report (报告) |
| `[S]` | Standard (标准) |
| `[P]` | Patent |
| `[DB]` | Database |
| `[CP]` | Computer program |
| `[EB]` | Electronic bulletin / online resource |
| `[EB/OL]` | Online electronic resource (the most common for web sources) |
| `[DB/OL]` | Online database |
| `[J/OL]` | Online-first journal article |

Composite tags (e.g. `[EB/OL]`) combine medium type with carrier.

## 4. Reference entry formats

### Journal article `[J]`
```
[1] SMITH J A, JONES B C. Article title in sentence case[J]. Journal Title,
    2024, 45(2): 123-145.
[2] 张三, 李四. 文章题名[J]. 期刊名, 2024, 45(2): 123-145.
```
- Year, comma, volume(issue) colon pages.
- For online-first: `[J/OL]` + DOI or URL + access date.

### Book / monograph `[M]`
```
[3] BOURDIEU P. The logic of practice[M]. Stanford: Stanford University
    Press, 1990.
[4] 费孝通. 乡土中国[M]. 北京: 北京大学出版社, 1998.
```
- City colon publisher comma year. Place of publication required (unlike APA 7).

### Book chapter `[M]`
```
[5] GIDDENS A. Central problems in social theory[M]//Social theory and
    modern societies. Cambridge: Cambridge University Press, 1979: 45-67.
```
- Use `//` to separate the chapter title from the container book (distinctive GB/T 7714 convention).

### Conference paper `[C]`
```
[6] SMITH J. Paper title[C]//Proceedings title. Place of conference:
    Publisher, Year: page range.
```

### Dissertation `[D]`
```
[7] 张三. 论文题名[D]. 城市: 授予机构, 年份.
```

### Online resource `[EB/OL]`
```
[8] AUTHOR. Title[EB/OL]. (Publication date)[citation date]. URL.
```
- Both publication date (in parens) and citation/access date are required for online sources.

## 5. In-text citation

### Numeric system
- `[1]` — single source
- `[1, 3, 5]` — multiple non-adjacent sources
- `[1-3]` — adjacent range
- Place at the end of the sentence before the period: `…research shows this effect[1].`
- For a specific page in numeric mode: `[1]23` or `[1]23-25` (page after the bracket).

### Author-date system
- `(Smith, 2024)` / `(张三, 2024)` — single author
- `(Smith and Jones, 2024)` — two authors
- `(Smith et al., 2024)` — 3+ authors
- `(Smith, 2024: 45)` — specific page (colon separator, distinctive vs APA's comma)

## 6. Common verification errors (what to flag)

| Error | What's wrong | Fix |
|---|---|---|
| `Smith, J. (2024). Title.` | APA format in a GB/T 7714 reference list | Convert to `SMITH J. Title[J]. …, 2024` |
| Missing `[J]` / `[M]` tag | Document-type tag omitted | Add the correct tag |
| `Smith, J.A.` in numeric mode | Lowercase surname with period-initials | Uppercase: `SMITH J A` |
| Chinese author inverted `三张` | Western inversion applied to a Chinese name | Keep as `张三` |
| Page range with en-dash `123–45` | GB/T 7714 uses hyphen `123-145` | Replace en-dash with hyphen |
| No place of publication for book | GB/T 7714 requires it (APA 7 does not) | Add `City: Publisher` |

## 7. Bilingual citation conventions

Chinese papers often cite both Chinese and Western sources. Conventions:
- Western sources keep Western format (author name as `SMITH J A` or `Smith J A`).
- Chinese sources use Chinese format (author name `张三`, Chinese punctuation `，。：`).
- In the reference list, mixing is allowed; in author-date mode, ordering is typically Western-alphabetical first, then Chinese by stroke/pinyin — confirm the venue's rule.
- Translated works: cite the translation you used; if citing both original and translation, list both with a cross-reference.
