# Digital Minds Field Map — Methodology Protocol

**Version:** 1.0
**Date:** 2026-03-17
**Authors:** PRISM

---

## 1. Scope & Objectives

This map provides a structured directory of organisational actors in the digital minds field — understood as the interdisciplinary space concerned with whether AI systems might be conscious, sentient, or moral patients, and what follows from that. The map is intended to orient new entrants and policy professionals by making the field's intellectual and institutional structure visible.

**Primary research question:** Who are the active organisational actors in the digital minds field, and how is the field structured?

**Scope boundary:** The map covers organisations with an explicit, active focus on digital minds as a topic. This includes foundational disciplines (consciousness science, philosophy of mind) insofar as their work is directly relevant to AI consciousness and welfare questions, and adjacent fields (animal sentience, AI safety) where there is meaningful overlap. It does not cover AI ethics, AI alignment, or AI governance organisations unless they have a specific digital minds workstream.

**Relationship to existing PRISM work:** This organisational map is distinct from the PRISM individual researcher network (housed in `/PRISM - Stakeholder Mapping/`). The two are complementary: the researcher network tracks individuals and their connections; this map tracks organisational actors and the field's institutional structure.

---

## 2. Zone Taxonomy

The map is organised into six topical/disciplinary zones. Zone assignment is the primary organising principle. Org type and function are captured as secondary filterable dimensions.

### Zone 1: Consciousness Science
Empirical research on consciousness in biological systems. Includes neuroscience and cognitive science labs working on theories of consciousness (IIT, GWT, Higher-Order theories, etc.). This zone is foundational for the digital minds field — frameworks developed here are the primary tools being applied to AI consciousness questions.

*Edge: Consciousness science labs are included where their theoretical frameworks have direct application to AI. Purely clinical or neuroscientific work without theoretical reach into the digital minds question is excluded.*

### Zone 2: Philosophy of Mind & Moral Status
Academic philosophy groups working on consciousness, subjective experience, moral patienthood, and personal identity. Provides the conceptual and normative foundations for AI welfare claims.

*Edge: Philosophy of mind is included; general philosophy of AI or AI ethics without a specific consciousness/moral status focus is excluded.*

### Zone 3: AI Consciousness & Welfare Research
Organisations explicitly dedicated to digital minds as a research topic — empirical and theoretical work on whether and how AI systems might be conscious, and what moral status follows. This is the core zone of the field as an emerging discipline.

*Edge: Organisations are included here only where digital minds is a primary research focus, not a secondary interest or occasional publication area.*

### Zone 4: Animal & Broader Sentience
Sentience research on non-human animals — the closest empirical analogue to AI consciousness questions. Includes organisations where animal sentience research directly informs or bridges to digital minds questions. Where an organisation has distinct sub-teams (e.g. Rethink Priorities), sub-teams may be listed separately under their relevant zones.

*Edge: Animal welfare advocacy organisations without a research/sentience science component are excluded.*

### Zone 5: AI Lab Programs
Internal teams or programs at AI laboratories with an explicit digital minds or model welfare focus. Structurally distinct from nonprofits and university centres; signals direct industry engagement with the field. Currently the smallest zone — Anthropic is the only major lab with an explicit AI Welfare program as of the initial survey date.

*Edge: General AI safety teams at labs are not included unless they have a specific digital minds workstream.*

### Zone 6: Policy & Governance
Organisations engaged in regulatory, legal, or policy work on digital minds and moral status questions. Includes think tanks, legal advocacy groups, and government bodies where digital minds is an explicit policy concern.

*Edge: General AI governance organisations without a specific digital minds focus are excluded. The Nonhuman Rights Project (legal advocacy for nonhuman persons) is classified as adjacent rather than included, as its focus is on biological rather than artificial minds.*

---

## 3. Eligibility Criteria

**Inclusion criteria:**
- Active organisation (not defunct)
- Explicit focus on digital minds, AI consciousness, AI welfare, or moral status of AI — OR foundational disciplinary work (consciousness science, philosophy of mind) with direct relevance
- Identifiable public presence (website or institutional page)

**Adjacent (not included in core map):**
- Organisations where digital minds is a minor or incidental concern
- Animal welfare advocacy without sentience research component
- General AI ethics or AI governance without specific digital minds workstream
- Legal advocacy focused on biological rather than artificial minds

**Funder-specific criterion:** Funding bodies are included only where there is a confirmed track record of grants specifically directed at digital minds, AI consciousness, or AI welfare research. Declared interest in consciousness science or proximity to the field is not sufficient — confirmed grantmaking is required. Relative scale is noted in descriptions to convey funders' importance to the field.

**Excluded:**
- Defunct organisations
- Individual researchers without an institutional anchor (named lab, centre, or unit). The unit of analysis is the organisation. Individual influence may be captured in the companion PRISM researcher network. An individual's departmental affiliation alone is not sufficient to make the department a mappable entry. Individual blogs and Substacks are excluded on the same grounds regardless of prominence.
- Purely commercial AI companies without a welfare/consciousness research program

---

## 4. Search & Identification Strategy

Search was conducted across four rounds between 2026-03-17 and 2026-03-18. All rounds logged in `methodology/log.md`.

### Seed sources used

- **PRISM individual researcher network** (`/PRISM - Stakeholder Mapping/`) — primary seed; organisational affiliations of mapped researchers used as anchor institutions
- **EA Forum** — Digital Minds topic tag; Digital Minds in Review annual posts; grant announcements
- **80,000 Hours** — problem profile on moral status of digital minds; organisation database
- **Web search** — systematic queries across all six zones using zone-specific terminology (e.g., "consciousness science lab", "AI welfare nonprofit", "AI sentience policy")
- **Snowballing** — from each included organisation: partner pages, collaborator listings, funder acknowledgements, event co-sponsors, advisory board members

### Round structure

| Round | Focus | Method |
|---|---|---|
| 1 | Parallel search across all 6 zones | Seed sources + web search |
| 2 | Snowball from Round 1 inclusions; user review | Snowball + expert consultation |
| 3 | Completionist pass — theory labs, funders, international orgs, philosophy of mind | Targeted web search + snowball |
| 4 | User review (second round); reclassification pass | Expert consultation |
| 5–9 | Ongoing additions, boundary cases, URL verification, completeness checks | Targeted web search + user-flagged candidates |

### Candidates assessed but not included

All candidates reviewed and not added are logged with rationale in `methodology/log.md`. Primary exclusion reasons: insufficient digital minds focus; individual without institutional anchor; defunct; below PI lab granularity threshold; general AI ethics/safety without digital minds workstream.

### Known limitations

- **Geographic asymmetry:** No active organisations identified in Africa, Latin America, Southeast Asia (outside Japan/Hong Kong), or India. Absence reflects field structure rather than search failure — confirmed via targeted regional searches. Documented as a field-structure finding.
- **Chinese-language sources:** Search was conducted primarily in English. Chinese-language sources and grey literature not systematically searched; the HKU and ShanghaiTech entries derive from English-language sources.
- **Private/commercial sector:** Private companies without public research output are difficult to assess. Conscium (UK) was included on the basis of confirmed research mission and direct organisational engagement; others may exist below visibility threshold.
- **Emerging organisations:** The field is growing rapidly. Organisations founded after the survey date are not captured. The corpus is intended to be re-run and compared across time.

---

## 5. Classification Procedure

1. Org identified and added to corpus with `status: pending`
2. Zone assignment made based on primary research focus
3. `status` updated to `included`, `adjacent`, or `excluded` with one-sentence rationale
4. Edge cases flagged in `notes` field and logged in `methodology/log.md`
5. Where an org has distinct sub-teams operating in different zones, sub-teams listed as separate entries with parent org noted

---

## 6. Controlled Vocabularies

**`status`:** `included` / `adjacent` / `excluded` / `pending`

**`zone_primary` / `zone_secondary`:** `consciousness-science` / `philosophy-of-mind` / `ai-consciousness-welfare` / `animal-sentience` / `ai-lab-programs` / `policy-governance`

**`org_type`:** `nonprofit` / `university-centre` / `lab-team` / `funding-body` / `government-body` / `community` / `media`

**`function`:** `research` / `advocacy` / `policy-governance` / `funding` / `training-education` / `career-support` / `media-comms` / `community-onboarding`

---

## 7. Versioning & Reproducibility

The corpus CSV includes a `schema_version` field. Changes to the schema or taxonomy trigger a version increment. All changes are logged in `metadata.md`. The goal is that the map can be re-run and compared across time, with the methodology log providing sufficient documentation to reproduce categorisation decisions.
