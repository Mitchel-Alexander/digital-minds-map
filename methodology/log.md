# Digital Minds Field Map — Methodology Log

Running log of decisions, rationale, and edge cases for the methodology write-up.

---

## Session 1 — 2026-03-17

### Context & Motivation
Task: produce an organisational field map for the digital minds space, analogous to the AISafety.com field map, as part of a broader PRISM field-building initiative. Intended to serve as a webpage resource orienting new entrants and policy professionals.

### Reference Maps Reviewed
- **AISafety.com/map** — 16 categories; mixes org type (Blog, Newsletter, Podcast), topical area (Empirical research, Conceptual research, Governance), and function (Advocacy, Career support, Funding). No public GitHub; codebase not open-source. Visual format: illustrated landscape with zoned areas + filterable card view.
- Noted that AISafety.com's taxonomy works for a large, mature field but would produce a misleading picture for digital minds, where the intellectual structure is more fragmented and disciplinarily distinct.

### Key Structural Decisions

**Decision: Topical/disciplinary zones as primary organising principle**
Rationale: The primary audience (new entrants, policy professionals) needs to understand the intellectual landscape first. Functional categories (funding, media, training) are secondary queries once oriented.
Implementation: Zone = primary map placement; org_type and function = filterable secondary dimensions on card view.

**Decision: 7 zones rather than AISafety.com's 16**
Rationale: Field is smaller and more coherent. Fewer zones avoids false granularity and reflects genuine disciplinary structure.
Zones: Consciousness Science / Philosophy of Mind & Moral Status / AI Consciousness & Welfare Research / Animal & Broader Sentience / AI Lab Programs / Policy & Governance / AI Safety — Adjacent

**Decision: Separate Consciousness Science from Philosophy of Mind**
Rationale: These are genuinely distinct disciplinary traditions (empirical vs. conceptual), with different methods, venues, and institutional homes. Collapsing them would obscure important structure for new entrants.

**Decision: Animal & Broader Sentience as its own zone (not merely adjacent)**
Rationale: Animal sentience research is the closest empirical analogue to AI consciousness questions and directly informs the field. Rethink Priorities' animal welfare sub-team is a clear example.

**Decision: AI Lab Programs as a distinct zone**
Rationale: Structurally distinct from nonprofits and university centres; signals industry engagement. Anthropic is currently the sole occupant (only major lab with an explicit AI Welfare program). Zone retained anticipating field growth.

**Decision: Sub-teams listed as separate entries where genuinely distinct**
Rationale: Rethink Priorities operates distinct sub-teams (Models of Consciousness; Animal Welfare) in different zones. Listing at sub-team level is more informative than a single org-level entry. Parent org noted in each entry.

### Key Eligibility Decisions

**Nonhuman Rights Project — Adjacent**
Rationale: Legal advocacy for nonhuman persons; focus is biological rather than artificial minds. Relevant conceptually but not a digital minds organisation.

**CAIS — AI Safety — Adjacent**
Rationale: AI safety nonprofit; no primary digital minds workstream identified. Included in Zone 7 if workstream identified, otherwise excluded.

**CHAI — University Research Centre**
Rationale: UC Berkeley centre for human-compatible AI; AI safety focus rather than digital minds. Likely Zone 7 or excluded depending on workstream review.

**DeepMind — Not included in AI Lab Programs**
Rationale: No explicit model welfare or AI consciousness program identified at time of survey. Relevant safety teams exist but do not constitute a digital minds program. To be reviewed if program launched.

### Schema Design Decisions

**Decision: CSV format for corpus**
Rationale: Reproducibility, version control compatibility, accessibility to collaborators.

**Decision: schema_version field in corpus**
Rationale: Category refinement is anticipated as the field is surveyed. Version field allows retrospective reclassification to be tracked without re-running the survey from scratch. Category changes require only column value updates + changelog entry, not a new survey.

**Decision: Methodology log (this file) maintained throughout**
Rationale: Provides audit trail for PRISMA-style report. All non-obvious classification decisions recorded here with rationale.

---

---

## Session 2 — 2026-03-17 (Systematic Search Pass 1)

### Search Strategy
Three parallel agents conducted systematic web searches across all seven zones simultaneously. Seed sources used: direct web search, EA Forum, 80,000 Hours, AISafety.com, aisafety.world, PRISM stakeholder map (prism-global.com/the-field-of-artificial-consciousness), snowballing from known anchor organisations.

**Note:** PRISM already maintains a stakeholder map at their website. This map aims to provide a more formal, reproducible, and methodologically documented resource — including funders, consciousness science foundations, and philosophy of mind — beyond what PRISM's current map covers.

### Organisations Identified: 54 entries

| Zone | Count | Notes |
|---|---|---|
| Consciousness Science (Zone 1) | 14 | Rich — major theory labs all identified |
| Philosophy of Mind (Zone 2) | 6 | Core centres identified |
| AI Consciousness & Welfare (Zone 3) | 9 | More developed than expected for a field ~3 years old |
| Animal & Broader Sentience (Zone 4) | 5 | Several dual-zone orgs |
| AI Lab Programs (Zone 5) | 3 | Only Anthropic confirmed; 2 pending |
| Policy & Governance (Zone 6) | 4 | Very nascent |
| AI Safety — Adjacent (Zone 7) | 0 | None confirmed — see finding below |
| Adjacent / Excluded | 5 | NhRP, GovAI, CAIS, CHAI, FHI |
| Funders (no zone) | 5 | Captured as function=funding |
| Community / Onboarding (no zone) | 3 | EA Forum, 80k Hours, etc. |

### Key Findings

**Finding 1: Zone 7 (AI Safety — Adjacent) is empty**
None of the canonical AI safety organisations (CAIS, CHAI, MIRI, ARC, Redwood, Apollo, UK AISI) have identified digital minds workstreams. This is a meaningful structural finding: the digital minds field is institutionally and intellectually separate from mainstream AI safety. This absence should be reported in the findings section of the methodology write-up, not treated as a gap in the search.
*Decision: Retain Zone 7 in the taxonomy as a documented empty zone — its emptiness communicates field structure.*

**Finding 2: The field is more institutionally developed than anticipated**
Several major organisations launched specifically in 2024–2025 (Eleos AI, CMEP, CIMC, Longview Digital Sentience Fund, Harder Problem Project rebranding, LSE Coller Centre), suggesting rapid field formation coinciding with the period of interest. The field is young but institutionalising quickly.

**Finding 3: Anthropic is uniquely committed among AI labs**
Google DeepMind and OpenAI show exploratory or informal engagement (pending status); all other labs show no evidence of programs. Anthropic is the only lab with a named program, dedicated staff, and published welfare assessments.

**Finding 4: No government body has a digital minds mandate**
Policy discussion is occurring in civil society (Harder Problem Project, LawAI, AI Rights Institute) but has not penetrated regulatory frameworks as of March 2026. This is a genuine structural gap worth highlighting in the report.

**Finding 5: The primary dedicated funder is Longview / Digital Sentience Consortium**
Open Philanthropy funds digital minds work without a named program; Macroscopic Ventures is the other major explicit funder. EA Funds and SFF are background funders. TWCF and JTF are the major funders of foundational consciousness science.

**Finding 6: Self-inclusion of PRISM**
PRISM (the organisation producing this map) is itself a field actor in Zone 3. It has been included in the corpus with a note disclosing this. Standard practice in field mapping where the producer is also a participant.

### Classification Decisions Made in This Session

**Sentience Institute** — Zone 3 primary, Zone 4 secondary. The organisation has explicitly reoriented toward digital minds as its core priority (EOY 2024 report) while retaining its animal sentience strand.

**NYU CMEP** — Zone 3 primary, Zone 4 secondary. Equally committed to animal and AI consciousness, but CMEP's 2025 activities (MEP Summit, AI consciousness workshops) tilt toward Zone 3 as primary.

**AMCS** — Zone 3 primary, Zone 1 secondary. AI consciousness is central to its research programme though not exclusive.

**Rethink Priorities sub-teams** — Listed as separate entries (Welfare of Digital Minds; Animal Welfare Department) per the protocol decision made in Session 1. Parent organisation noted in description.

**Google DeepMind and OpenAI** — Status: pending. Evidence of interest but no formal programs confirmed. To be reviewed if programs launched.

**Conscium** — Status: pending. Private company; research output not yet public-facing. Included because it seed-funded PRISM and claims machine consciousness as a core research thread.

**FHI** — Status: excluded (defunct, closed 2024). Historically relevant as a source of researchers now active in the field.

**Funders and community orgs** — No zone assigned; captured by function field. Included in corpus for the filterable card view.

**Decision: Zone 7 removed from map; finding retained for report**
Rationale: The systematic search pass confirmed no active AI safety organisations have identifiable digital minds workstreams. An empty zone on the map would be uninformative for new entrants and policy professionals. However, the absence itself is a substantive finding — the structural separation between the digital minds field and mainstream AI safety is worth foregrounding in the methodology write-up. The corpus retains adjacent/excluded entries for CAIS, CHAI, GovAI etc., and the finding is documented in the log. The map now has 6 zones.

### Pending Actions
- Manual verification of NIAS Consciousness Studies Programme (niasconsciousnesscentre.org) — agent flagged as uncertain
- Review pending status of Google DeepMind and OpenAI if new information emerges
- Review Conscium pending status
- Consider whether Zone 7 should be retained as an empty zone or removed from the final map
- Second search pass: check for orgs in non-English-speaking regions (currently corpus is dominated by US/UK/Australia)

---

## Session 3 — 2026-03-17 (User Review + Corrections)

### User augmentations
Following user review of the full corpus list, four organisations were added and one correction made.

**GPI correction — status changed to excluded (defunct)**
User confirmed Global Priorities Institute (Oxford) is now closed. Status updated from `included` to `excluded`. Rationale preserved: historically significant — produced foundational early research including Butlin et al. 2023 and 2025 publications on AI sentience. Mirrors FHI treatment in corpus.

**New entries added:**

| Org | Zone | Status | Rationale |
|---|---|---|---|
| Neuromatch — AI Sentience Scholars | ai-consciousness-welfare | included | Only structured career-development fellowship specifically for digital minds; newly launched sub-program within Neuromatch |
| PIVOTAL Research | adjacent | adjacent | AI safety/governance fellowship; no digital minds workstream |
| SPAR | adjacent | adjacent | AI safety fellowship; no digital minds workstream |
| MATS | adjacent | adjacent | Flagship AI safety research fellowship; no digital minds workstream |

**Classification note — PIVOTAL, SPAR, MATS:**
All three are AI safety talent-pipeline fellowships with no footprint in consciousness or welfare discourse. They are included in the corpus as adjacent entries because: (a) the user identified them as relevant context; (b) their absence from the digital minds space contributes evidence for the structural separation finding; (c) they are common entry points for people who may subsequently move into digital minds work. They do not appear on the map.

### Snowball search initiated
Following user review, a systematic snowball pass was initiated. See Session 4 for results.

**Gap identified post-search: Graziano Lab (Princeton) — added**
User flagged that the Graziano lab was missing. Michael Graziano's Attention Schema Theory (AST) is one of the four major competing theories of consciousness represented in the corpus (alongside IIT/Tononi, GWT/Dehaene, RPT/Lamme). The lab had appeared only as a footnote in the AE Studio entry. Added to Zone 1 as a standalone entry. This gap arose because AST is associated with a single PI lab rather than a named centre — a recurring challenge with consciousness science where theory labs and research centres don't always map neatly.

---

## Session 4 — 2026-03-17 (Snowball Pass 1)

### Method
Two parallel agents conducted systematic snowball searches from the websites of included organisations. Agent 1 covered Zones 3, 4, 5, 6 seed orgs (Eleos, RP, PRISM, Sentient Futures, LSE JCC, CMEP, Harder Problem, Cambridge Digital Minds, CIMC). Agent 2 covered Zones 1 and 2 seed orgs (ASSC, Arizona CCS, Sussex SCCS, LCFI, M3CS, Active Inference Institute, Allen Institute, NYU CMBC). For each org, agents checked partner pages, collaborator listings, advisory boards, funder acknowledgements, and event co-sponsors.

### New organisations confirmed and added

| Org | Zone | Found via |
|---|---|---|
| Reciprocal Research | ai-consciousness-welfare | Eleos AI (Cameron Berg affiliation) |
| AE Studio — AI Alignment | ai-consciousness-welfare | Reciprocal Research snowball |
| COGITATE Consortium | consciousness-science | Allen Institute |
| Max Planck Institute for Empirical Aesthetics | consciousness-science | COGITATE |
| CIFAR Brain Mind and Consciousness Program | consciousness-science | TWCF / Monash link |

### Classification decisions

**AE Studio** — Industry-research hybrid. Commercial software studio with genuine published research on AI consciousness and funded academic research (Graziano attention schema). Classified as `lab-team` with function=research. Unusual org type flagged in notes.

**COGITATE Consortium** — Not a standalone institution; a named multi-institutional adversarial collaboration with its own website and publication record. Treated as a consortium entry (org_type=community). Precedent: similar to how ASSC is treated as a professional association rather than a research institution.

**CIFAR Program** — CIFAR itself is a Canadian funding and convening body; the Brain Mind and Consciousness Program is a distinct unit with named fellows and a 10+ year history. Listed as the program rather than the parent org.

### Candidates flagged for user decision (not yet added)

| Org | Issue | Recommendation |
|---|---|---|
| ConTraSt Database (Tel Aviv) | More a research resource than org | Note only, or include as infrastructure |
| Donders Institute (Radboud) | Broad neuroscience institute, COGITATE site | Likely too broad; exclude unless adding COGITATE member institutions systematically |
| Navigation Fund | Site down; uncertain if active | User to confirm |
| NYU Wild Animal Welfare Program | Possible Zone 4 addition; NYU internal | Confirm whether standalone or part of CMEP |

### Post-session decisions (user confirmed)

| Candidate | Decision | Rationale |
|---|---|---|
| ConTraSt Database | Note in report only; not added to corpus | Research resource rather than organisation; will be cited in methodology write-up as field infrastructure |
| Donders Institute | Excluded | Too broad; COGITATE member institutions not mapped individually at this stage |
| Navigation Fund | Added as funder | User confirmed: EA-adjacent philanthropic fund, co-funder of the 2025 Digital Sentience Consortium round |
| NYU Wild Animal Welfare Program | Added to Zone 4 | User confirmed as standalone programme |

### Technical notes
- LCFI and Monash M3CS both returned HTTP 403 — could not be snowballed. Manual browser visits recommended.
- ASSC website renders in JavaScript only — full partner/sponsor list not accessible to automated fetch.
- Most productive snowball chain: Allen Institute → COGITATE → TWCF → CIFAR.

---

## Session 5 — 2026-03-17 (Snowball Pass 2 — Completionist)

### Method
Four parallel agents conducted systematic snowball searches with general user permission. Coverage:
- Agent 1: Theory lab websites (Graziano/Princeton, Friston/UCL, Lamme/UvA, HOT network, Seth, Hohwy, Clark, COGITATE member institutions, IIT wiki)
- Agent 2: Funder grantee lists (Coefficient Giving/Open Philanthropy, Macroscopic Ventures, Longview, TWCF ARC, JTF, SFF)
- Agent 3: International organisations (Europe, Asia, Global South, Canada) + media/journals/professional associations
- Agent 4: Philosophy of mind centres (Chalmers, Schwitzgebel, Metzinger, Shevlin, Sebo, Birch, Butlin, PhilPapers)

### New entries added (18)

**Zone 1 — Consciousness Science:**
- BAMΞ — Bamberg Mathematical Consciousness Science Initiative (Germany)
- CRCN/CO3 — ULB Brussels (Axel Cleeremans)
- CHAIN — Center for Human Nature AI and Neuroscience, Hokkaido University (Japan)

**Zone 2 — Philosophy of Mind:**
- Centre for the Study of Perceptual Experience (CSPE), Glasgow (Fiona Macpherson)
- Institute for Ethics in AI, Oxford (John Tasioulas)
- PAIR — Centre for Philosophy and AI Research, FAU Erlangen (Vincent Müller)

**Zone 2/3 — Dual zone:**
- AI & Humanity Lab, HKU (Herman Cappelen)

**Zone 3 — AI Consciousness & Welfare:**
- Araya Inc AI Consciousness Research (Ryota Kanai, Japan)
- Center on Long-Term Risk (CLR)
- ShanghaiTech University — Institute of Humanities (Robert Prentner)

**Zone 4 — Animal & Broader Sentience:**
- NYU Center for Environmental and Animal Protection (Jeff Sebo)
- Insect Welfare Research Society

**Media:**
- Journal of Artificial Intelligence and Consciousness (JAIC)
- Neuroscience of Consciousness (Oxford/ASSC)
- Philosophy and the Mind Sciences (PhiMiSci)
- Journal of Consciousness Studies
- Digital Minds Newsletter

**Corpus update:**
- Open Philanthropy entry updated to Coefficient Giving (rebranded 2025–2026)

### Key structural findings

**Geographic asymmetry confirmed:** Corpus dominated by US/UK/Australia. New additions improved coverage for Germany, Belgium, Japan, Hong Kong, and China. No active organisations found in Africa, Latin America, Southeast Asia (outside Japan/China/HK), or India specifically focused on digital minds. This is both a methodological limitation and a field-structure finding.

**COGITATE granularity decision held:** Member institutions (Yale, Harvard, Birmingham, McGill, Champalimaud) not added individually. COGITATE entry covers the cluster.

**PI lab granularity threshold applied consistently:** Individual PI labs below the threshold (MetaLab/Fleming, Mudrik/TAU, Hohwy/Monash CAP Lab) not added unless the PI originated a major named theory or the lab has a distinctive institutional identity.

**Open Philanthropy rebrand:** Confirmed by user as a full organisation-wide rebrand to Coefficient Giving, completed end of 2025. Corpus entry updated accordingly. Grants database was inaccessible during the website transition — funder snowball incomplete for this source; recommend revisiting once the new site stabilises.

**MIND Foundation ≠ MIND Group:** Confirmed distinct entities. MIND Foundation is a psychedelic therapy nonprofit; no connection to Metzinger's MIND Group. No change to corpus.

**RIKEN Center for Brain Science (Japan):** Added to corpus following user review. Hakwan Lau not confirmed at RIKEN; included on own merits — RIKEN CBS explicitly frames elucidating brain information processing principles as foundational to brain-based AI, providing a direct institutional bridge from consciousness neuroscience to AI development. Japan's premier brain science institute.

---

## Session 6 — 2026-03-17 (User Review — Second Round)

### Reclassifications

**PIVOTAL Research, SPAR, MATS — adjacent → included**
User confirmed all three have AI consciousness and/or moral status mentor tracks within their broader AI safety fellowship programmes. Reclassified from `adjacent` to `included`. No primary zone assigned; function=community-onboarding reflects their role. This is a different footing from Future Impact Group (which has a fully dedicated AI Sentience track as a primary programme offering) — the digital minds element in PIVOTAL/SPAR/MATS is at the mentor/sub-track level rather than programme level. Notes updated accordingly.

### New entries added (6)

| Org | Zone | Type | Notes |
|---|---|---|---|
| Noema Magazine | media | media | Berggruen Institute publication; Anil Seth's 2025 Berggruen Prize essay on consciousness published here |
| Aeon | media | media | Primary platform for leading researchers writing for broad audiences |
| Center for the Future of AI, Mind, and Society (FAU) | Zone 3 | university-centre | Susan Schneider; AI consciousness, mind uploading, moral status |
| Google Research — Paradigms of Intelligence | Zone 5 | lab-team | Geoff Keeling and Winnie Street; AI Welfare book forthcoming 2026 |
| Co-Sentience Initiative (CoSI) | Zone 3 | nonprofit | CF Debate argument database on computational functionalism; founded 2025 |

**Notes on new Zone 5 entry:**
Google Research — Paradigms of Intelligence is distinct from the Google DeepMind entry (currently pending). This is an internal team at Google Research with explicit AI welfare research output and a forthcoming book. The two entries should be reviewed together: if Google DeepMind develops a formal program, it may be added separately; for now Google Research represents Google's most concrete digital minds engagement. URL to be verified.

**Notes on Noema / Berggruen Institute:**
Noema is the Berggruen Institute's flagship publication. The Berggruen Institute also runs the Antikythera programme (Benjamin Bratton) — which was considered and not added to the corpus (Session 5) as insufficiently focused on digital minds. The Institute awarded the 2025 Berggruen Prize for consciousness writing to Anil Seth. This institutional connection between Noema, Berggruen Prize, and consciousness science is worth noting in the report as an example of philanthropic support for public consciousness discourse.

---

## Session 7 — 2026-03-17 (User Review — Third Round)

### Reclassification: Future Impact Group — AI Sentience Track
Zone 3 → community/onboarding (no zone). User noted it is a fellowship programme analogous to PIVOTAL/SPAR/MATS. Reclassified for consistency. The AI Sentience Track is a dedicated sub-track rather than a primary research function, making community/onboarding the correct classification.

### Reclassification: Google DeepMind — pending → included (Zone 5)
User confirmed Google DeepMind has research engaging with AI consciousness. Two key examples:
- **Murray Shanahan** (Senior Research Scientist, DeepMind): sustained public-facing work on machine consciousness and AI
- **Alexander Lerchner** (Senior Staff Scientist, DeepMind / Gatsby Unit UCL): preprint "The Abstraction Fallacy: Why AI Can Simulate But Not Instantiate Consciousness" (March 2026, PhilArchive/DeepMind publications). Argues against computational functionalism from a substrate-sensitive ontological position; explicitly invokes the "AI welfare trap." A sceptical/anti-functionalist position — notable as a philosophically serious intervention from inside a major AI lab.

DeepMind does not have a formal named welfare or consciousness program (unlike Anthropic). Inclusion reflects confirmed research output rather than an institutional program. Description updated to reflect this distinction.

**Note for report:** The contrast between Anthropic (formal program, welfare-positive framing) and DeepMind (individual researcher outputs, mixed framing including sceptical positions) is a meaningful field-structure observation for Zone 5.

### URLs to verify manually:
- Center for the Future of AI, Mind, and Society (FAU) — specific centre URL pending
- Google Research Paradigms of Intelligence — specific team page URL pending

### Candidates not added

| Candidate | Reason |
|---|---|
| COGITATE member institutions (Yale, Harvard, Birmingham, McGill, etc.) | Too broad; COGITATE entry covers the cluster |
| MetaLab / Steve Fleming (UCL) | Below PI lab granularity threshold |
| Mudrik Lab / Tel Aviv University | Below granularity threshold; covered via COGITATE |
| Edinburgh PPLS / Andy Clark | Department, not dedicated consciousness centre |
| RIKEN Center for Brain Science | Lau affiliation unconfirmed; flag for manual check |
| Antikythera / Berggruen Institute | Insufficient digital minds focus |
| Qualia Research Institute (QRI) | No direct AI consciousness/welfare program confirmed |
| IIT Mandi MBCC | Conference venue, not a standing research org |
| FOCAL / CMU | Cooperative AI, not consciousness/welfare |
| Consciousness Club Tokyo | Sub-entity of Araya; noted in Araya description |
| Meditations on Digital Minds / Outpaced | Individual Substacks below media threshold |
| German EA Foundation | Peripheral funding node |

---

## Session 8 — 2026-03-17 (Methodological Boundary Decisions)

### Policy decision: Individual researchers without institutional anchor

**Decision:** Individual researchers who have no named lab or institutional unit to serve as an organisational anchor are excluded from the corpus. The unit of analysis is the *organisation*, not the individual. An individual's influence on the field can be noted in the report or captured via the companion PRISM individual researcher network.

**Rationale:** The map's purpose is to render the field's *institutional* structure visible. Including individuals with no organisational anchor would blur this framing and create an unworkable precedent — prominent lone scholars are numerous and the selection criteria would be arbitrary.

**Illustrative cases:**
- Eric Schwitzgebel (UC Riverside) — writes prolifically on AI consciousness (The Splintered Mind blog, academic publications) but has no named lab or centre. Excluded as individual. His departmental affiliation (UCR Philosophy) is not sufficient to make UC Riverside a mappable entry.
- Individual Substacks (Saad, Caviola, Outpaced/Meditations on Digital Minds) — excluded on same grounds as individual blogs.

**Protocol update:** Added explicit exclusion clause to protocol.md §3 Eligibility Criteria.

---

### New inclusion: Berggruen Institute (Zone 2 — Philosophy of Mind) + adjacent: AI & Humanity Lab (HKU)

**Decision:** Included. Distinct from prior Antikythera exclusion.

**Rationale:** The Berggruen Institute hosts two direct programs on AI consciousness:

1. **"After Consciousness" project** (berggruen.org/eu/projects/after-consciousness) — a named research initiative led by Herman Cappelen (Berggruen Institute China Fellow), framing conceptual engineering around AI consciousness as a structured experiment. Inaugural workshop January 2026, University of Hong Kong. Contributors include Keith Frankish (illusionism, Sheffield), Edouard Machery (Pittsburgh), Wayne Wu (Pittsburgh), Simon Goldstein (HKU). Explicitly addresses whether the term "consciousness" distorts AI discourse and develops alternative vocabularies.

2. **Annual essay prize** — the 2025 prize focused on "consciousness, intelligence, and the nature of mind in an age of advancing artificial systems." Winner: Anil Seth ("The Mythology of Conscious AI"). AI consciousness was the explicit competition theme.

**Why this overrides the prior Antikythera exclusion:** Antikythera (Benjamin Bratton, speculative tech/political theory) was correctly excluded as insufficiently focused on digital minds. "After Consciousness" is a different program with direct and explicit scope overlap. The Berggruen Institute as an organisation is now includable on the strength of this named program. Noema Magazine remains a separate entry.

**Zone 2 rationale:** Conceptual engineering around AI consciousness is philosophical/foundational work, not empirical consciousness science (Zone 1) or dedicated AI welfare research (Zone 3).

**Update (2026-03-18):** After Consciousness is a *joint* project between Berggruen and the AI & Humanity Lab at the University of Hong Kong (ai-humanity.net). Herman Cappelen is both the Berggruen China Fellow and the founder/director of the AI & Humanity Lab — he is the institutional link on both sides. Berggruen entry description updated to reflect joint project structure.

**Field-structure note for report:** The Berggruen–HKU relationship reflects an explicit institutional strategy of engagement with Chinese research cultures. Cappelen holds a *China* Fellowship specifically; the 2025 essay prize had a dedicated Chinese-language track (two Chinese-language co-winners alongside Anil Seth's English-language winner). This is not incidental — it represents a deliberate effort to extend the digital minds conversation into Chinese-language philosophical traditions and Chinese academic institutions. Combined with the HKU base, Araya in Japan, and RIKEN CBS, this is one of the few concrete data points in the corpus showing active bridge-building between the field's predominantly anglophone institutional core and East Asian research cultures. Worth foregrounding in the geographic asymmetry section of the report.

### Protocol update: funder eligibility criterion added (§3)

Formalised a funder-specific inclusion criterion: funding bodies must have a confirmed track record of grants specifically directed at digital minds, AI consciousness, or AI welfare research. Declared interest or proximity is not sufficient. Relative scale to be noted in descriptions.

**Funder audit against criterion (2026-03-18):**

| Funder | Confirmed grants | Assessment |
|---|---|---|
| Coefficient Giving | Eleos AI; Future Impact Group | Passes — strong |
| Longview Philanthropy | Digital Sentience Consortium (co-founded) | Passes — strong |
| Macroscopic Ventures | Eleos AI; NYU CMEP; NYU CMBC; Consortium | Passes — strong |
| Templeton Foundations (JTF/TWCF) | TWCF → Araya $222k (2018–21); COGITATE; ETHOS | Passes — strong; primary infrastructure funder of Zone 1 |
| Navigation Fund | Digital Sentience Consortium co-funder; dedicated fellowships | Passes — confirmed |
| EA Funds (LTFF) | Robert Long workshop → Butlin et al. 2023 ($10,840); anonymous digital sentience ($27,450) | Passes — modest scale but significant field impact; fund chair publicly identified AI consciousness as underinvested |

All current funder entries confirmed. EA Funds is the weakest case by grant scale; justified by the outsized field impact of the Robert Long grant.

**Templeton research note (2026-03-18):** Follow-up search found no direct AI consciousness grants from either JTF or TWCF post-Araya (2021). TWCF's primary contribution is infrastructural — the $30M ARC programme funds consciousness science adversarial collaborations (IIT, GNW, HOT, RPT, predictive processing) that the digital minds field draws on directly. ARC grantees include Allen Institute, NYU, UvA, UCL — all in the corpus. No AI safety funding identified from either foundation. **For the report:** Templeton is an early mover in AI consciousness (Araya grant predates most field formation) and the primary funder of the Zone 1 theoretical infrastructure, but has not followed through with a second wave of direct AI consciousness grants — a gap worth noting given the field's growth since 2021. Corpus entry updated to reflect the indirect/direct distinction accurately.

### Merge: Templeton World Charity Foundation (TWCF-ARC) + John Templeton Foundation → single entry

Two separate corpus rows collapsed into one entry: "Templeton Foundations (JTF / TWCF)." Rationale: JTF and TWCF are legally distinct entities but function as a single philanthropic ecosystem from the field's perspective, and separating them added complexity without commensurate clarity. The merged entry distinguishes the two funding streams in the description: JTF as the broader consciousness and big questions funder; TWCF's ARC programme as the more targeted consciousness science initiative and the largest dedicated funder of adversarial theory collaborations globally. Primary URL: templeton.org (JTF parent); TWCF ARC URL retained in notes.

---

## Session 9 — 2026-03-18 (Completeness check: five candidates)

### Not added: Meta AI
No AI welfare or consciousness research program identified. No corpus entry warranted.

### Excluded: Microsoft (AI division)
No research program; explicitly opposite position. Mustafa Suleyman (CEO of AI, Microsoft) published a blog post in August 2025 arguing the study of AI welfare is "both premature, and frankly dangerous," contending it exacerbates harms around AI-induced psychotic breaks and unhealthy human-AI attachments. Added as an excluded entry for field-structure documentation — the Microsoft/Anthropic contrast is the sharpest articulation of industry division on this question.

### Not added: UK DSIT
No confirmed government engagement with digital minds, AI welfare, or AI consciousness. DSIT's focus is AI safety, algorithmic transparency, and economic/infrastructure AI. Future Impact Group alumni going to DSIT does not make DSIT itself an includable entity.

### Adjacent: Qualia Research Institute (QRI)
Earlier search suggested AI welfare framing; homepage confirms AI is not an explicit focus. QRI's research tools and outputs are biologically focused (psychedelics, meditation, mathematical valence formalisation). The valence/phenomenology framework has conceptual relevance to AI welfare range reasoning, but AI consciousness is not a primary or named program. Classified adjacent. Added to corpus for documentation.

### Not added: Verses AI
Cognitive computing company with Karl Friston as Chief Scientist using active inference/FEP architecture for AI products. Not a consciousness research organisation. Friston's institutional home (Wellcome Centre FIL, UCL) is already in the corpus. No corpus entry warranted.

### Candidates not added

| Candidate | Reason |
|---|---|
| Meta AI | No welfare/consciousness program identified |
| UK DSIT | No confirmed digital minds engagement |
| Verses AI | Commercial AI product company; not consciousness research; Friston's lab already in corpus |

---

### Reclassification: Neuromatch — AI Sentience Scholars → community/onboarding (no zone)

Zone 3 → no zone. Consistent with PIVOTAL/SPAR/MATS/Future Impact Group — fellowship and training programme rather than primary research producer. `zone_primary` cleared.

### Reclassification: Conscium — pending → included (Zone 5)

User confirmed inclusion. Private company (UK) with machine consciousness as a core research thread; works on AI agent verification and neuromorphic computing; seed-funded PRISM. Research output not yet fully public-facing but the confirmed research mission and direct organisational engagement with the digital minds field meets the threshold. Unusual node type noted — private company alongside AE Studio as the two industry-research hybrids in the corpus.

### Reclassification: OpenAI — Model Behavior Team — pending → excluded

The Model Behavior team (~14 researchers) was merged into Post Training in September 2025 and no longer exists as a distinct unit. No successor digital minds or formal welfare program has been announced. Excluded on the basis that the named organisational entity is dissolved. An AI Welfare Specialist role was advertised but not filled with a formal program attached. Re-addition warranted if OpenAI launches a formal welfare or consciousness program. The contrast with Anthropic (formal named program, dedicated staff) and Google DeepMind (confirmed research output by named researchers) is a meaningful Zone 5 structural finding.

---

### Adjacent classification: AI & Humanity Lab (HKU)

The AI & Humanity Lab at HKU (Director: Herman Cappelen) is classified **adjacent**, not included. Primary mandate is AI ethics and philosophy of AI broadly: it runs a MA in AI Ethics and Society and supports the Hong Kong Global AI Governance Conference — wider than digital minds. The After Consciousness project is its most directly relevant program, but it is one strand within a broader AI-and-humanity agenda. Consistent with protocol §2 Zone 2 edge: "general philosophy of AI or AI ethics without a specific consciousness/moral status focus is excluded."

---

### Adjacent classification: Allen Discovery Center at Tufts University (Levin Lab)

**Decision:** Classified `adjacent`, not included.

**Rationale:** Michael Levin's Allen Discovery Center has produced direct publications on AI consciousness questions:
- Fields, Glazebrook & Levin (2021). "Scale-Free Cognition" — *Neuroscience of Consciousness*
- Levin, M. (2025). "Diverse Intelligence: an essential field for questions of AI and Consciousness" — PsyArXiv preprint

The 2025 preprint title is explicit. However, the user's assessment is that consciousness remains peripheral in the lab's broader research agenda, whose primary focus is bioelectricity, morphogenesis, and developmental biology. This matches the protocol edge for Zone 1: labs are included where their theoretical frameworks have "direct application to AI." Levin's position is effectively the inverse — he argues that AI/consciousness *should* engage with diverse intelligence frameworks, but the lab itself is not primarily a consciousness science lab applying its theories to AI.

**Ruling:** The peripheral nature of consciousness in the lab's core agenda places this below the inclusion threshold. Classified adjacent rather than included, with both papers cited in the corpus notes field for traceability. The diverse intelligence / A-Life bridge to digital minds is noted as an emerging cross-disciplinary connection worth tracking in future rounds.
