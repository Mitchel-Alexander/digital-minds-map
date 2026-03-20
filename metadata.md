# Digital Minds Field Map — Dataset Metadata

## Current Version
**Schema version:** 1.1
**Last updated:** 2026-03-20
**Corpus status:** Complete — 93 entries (78 included, 7 adjacent, 8 excluded)

## Dataset Description
Organisational field map of the digital minds space (AI consciousness, AI welfare, moral status of AI). Covers active organisations with explicit or foundational relevance to digital minds questions. Intended to orient new entrants and policy professionals.

Companion to the PRISM individual researcher network (`/PRISM - Stakeholder Mapping/`).

## Search Rounds

| Round | Date | Sources | Orgs identified | Notes |
|---|---|---|---|---|
| 1 | 2026-03-17 | Web search, EA Forum, 80,000 Hours, PRISM stakeholder map, snowballing | 54 | Parallel search across all 7 zones; see methodology/log.md Session 2 |
| 2 | 2026-03-17 | Snowball from included orgs; user review | 62 | 5 confirmed additions from snowball; 4 user additions; 1 correction (GPI); see Session 3–4 |
| 3 | 2026-03-17 | Completionist snowball — theory labs, funders, international, philosophy of mind | 84 | 18 new entries + RIKEN CBS; Coefficient Giving rebrand confirmed; geographic asymmetry confirmed; see Session 5 |
| 4 | 2026-03-17 | User review (second round) | 93 | 6 new entries; PIVOTAL/SPAR/MATS reclassified from adjacent to included; see Session 6 |
| 5 | 2026-03-18 | User review (third round); boundary cases; new additions | 97 | Berggruen Institute added; AI & Humanity Lab (adjacent); Levin Lab (adjacent); QRI (adjacent); Microsoft (excluded); various reclassifications; see Sessions 7–9 |

## Changelog

| Version | Date | Change | Reason |
|---|---|---|---|
| 1.0 | 2026-03-17 | Initial schema and protocol established | Project setup |
| 1.0 | 2026-03-17 | Corpus populated — 54 entries from Search Round 1 | First systematic search pass |
| 1.0 | 2026-03-18 | Corpus complete — 97 entries; protocol §4 written; funder eligibility criterion added; URLs verified; Templeton entries merged | Sessions 5–9 |
| 1.0 | 2026-03-18 | Corpus revised — 92 entries (77 included, 7 adjacent, 8 excluded); 4 orgs reclassified to excluded (Institute for Ethics in AI, RIKEN CBS, Center for Consciousness Studies Arizona, ShanghaiTech); MoC conferences folded under AMCS | Session 10 |
| 1.1 | 2026-03-20 | Schema extended: added `key_figures` and `key_outputs` columns; enriched Z1 descriptions with field-relevance bridges; fixed broken descriptions (ASSC, CHAIN, EA Forum); corrected included count to 78 | Directory enrichment pass |

## File Index

| File | Description |
|---|---|
| `data/corpus.csv` | Main organisational dataset |
| `methodology/protocol.md` | Formal protocol — scope, taxonomy, eligibility criteria |
| `methodology/log.md` | Running decision log for methodology write-up |
| `metadata.md` | This file — versioning and changelog |
| `outputs/reports/` | Written outputs and report drafts |
| `outputs/tables/` | Exported summary tables |

## Changelog

### 2026-03-20 — Comprehensive Description Rewrite Pass
- **Phase 0:** Fixed 3 structural CSV row errors (ASSC line 14, EA Forum line 55, CHAIN line 73) — column-shift misalignment in source/date_identified/notes fields
- **Phase 1a:** Rewrote 5 Tier 4 (problematic) descriptions with web research: Institute for Law and AI, AI Rights Institute, UFAIR, Astera Institute, Conscium
- **Phase 1b:** Expanded 11 Tier 3 (short/weak) descriptions to 60+ words following Position→Mandate→Notable work schema
- **Phase 1c:** Restructured ~30 Tier 2 (adequate) descriptions for schema consistency and added specificity where below 60 words
- **Phase 2:** Filled key_figures for 11 entries via web research; filled key_outputs for 15 entries from existing knowledge
- **Phase 3:** CSV integrity verified (all 94 rows × 17 columns); HTML regenerated (78 orgs, 116KB); word count audit: 59/78 included entries at 60-120 words, remaining 19 at 54-59 words
- Corrected Astera Institute description: Digital Sentience Consortium coordinated by Longview Philanthropy, not Astera
