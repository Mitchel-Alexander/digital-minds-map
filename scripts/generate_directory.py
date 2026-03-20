"""
Generate outputs/directory.html from data/corpus.csv and outputs/logos/logo_report.csv
"""
import csv, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Load logos
# ---------------------------------------------------------------------------
logo_report_path = os.path.join(ROOT, 'outputs', 'logos', 'logo_report.csv')
logo_map = {}  # org_name -> slug
with open(logo_report_path) as f:
    for row in csv.DictReader(f):
        if row.get('status') == 'ok':
            logo_map[row['org_name']] = row['slug']

# Manual slug fixes for renamed orgs
logo_map['Rethink Priorities — AI Cognition Initiative'] = logo_map.get(
    'rethink-priorities-welfare-of-digital-minds',
    'rethink-priorities-welfare-of-digital-minds')

# ---------------------------------------------------------------------------
# Subgroup classification (support/infrastructure orgs only)
# ---------------------------------------------------------------------------
JOURNALS = {
    'Journal of Artificial Intelligence and Consciousness (JAIC)',
    'Neuroscience of Consciousness (journal)',
    'Philosophy and the Mind Sciences (PhiMiSci)',
    'Journal of Consciousness Studies',
}

def subgroup(row):
    if row['zone_primary'].strip():
        return ''
    if row['org_type'].strip() == 'funding-body':
        return 'funders'
    if row['function'].strip() == 'community-onboarding' and row['org_type'].strip() == 'nonprofit':
        return 'onboarding'
    if row['org_name'].strip() in JOURNALS:
        return 'journals'
    return 'community-media'

def slug(name):
    s = name.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')

# ---------------------------------------------------------------------------
# Geography region mapping
# ---------------------------------------------------------------------------
GEO_REGION_MAP = {
    'USA': 'USA',
    'UK': 'UK',
    'France': 'Europe',
    'Germany': 'Europe',
    'Netherlands': 'Europe',
    'Belgium': 'Europe',
    'Italy': 'Europe',
    'Switzerland': 'Europe',
    'Japan': 'Asia-Pacific',
    'China': 'Asia-Pacific',
    'Hong Kong': 'Asia-Pacific',
    'Australia': 'Asia-Pacific',
    'South Korea': 'Asia-Pacific',
    'international': 'International',
}

def geo_region(raw):
    return GEO_REGION_MAP.get(raw, 'International')

# ---------------------------------------------------------------------------
# Type label map
# ---------------------------------------------------------------------------
TYPE_LABELS = {
    'nonprofit':         'Nonprofit',
    'university-centre': 'University Centre',
    'lab-team':          'Lab Team',
    'funding-body':      'Funder',
    'media':             'Media',
    'community':         'Community',
}

# ---------------------------------------------------------------------------
# Load corpus
# ---------------------------------------------------------------------------
corpus_path = os.path.join(ROOT, 'data', 'corpus.csv')
orgs = []
with open(corpus_path) as f:
    for row in csv.DictReader(f):
        if row['status'].strip() != 'included':
            continue
        name = row['org_name'].strip()
        zone = row['zone_primary'].strip()
        zone_sec = row['zone_secondary'].strip()
        sg = subgroup(row)
        logo_slug_val = logo_map.get(name, '')
        raw_geo = row['geography'].strip()
        orgs.append({
            'name':         name,
            'url':          row['url'].strip(),
            'zone':         zone,
            'zone_secondary': zone_sec,
            'subgroup':     sg,
            'type':         row['org_type'].strip(),
            'type_label':   TYPE_LABELS.get(row['org_type'].strip(), row['org_type'].strip()),
            'geography':    raw_geo,
            'geo_region':   geo_region(raw_geo),
            'description':  row['description'].strip(),
            'founding_year': row['founding_year'].strip(),
            'logo_slug':    logo_slug_val,
            'key_figures':  row.get('key_figures', '').strip(),
            'key_outputs':  row.get('key_outputs', '').strip(),
        })

orgs.sort(key=lambda o: o['name'].lower())

org_count = len(orgs)

# ---------------------------------------------------------------------------
# Zone / subgroup metadata
# ---------------------------------------------------------------------------
ZONES = [
    ('ai-consciousness-welfare', 'Digital Minds & AI Consciousness',
     'The field\'s core: organisations explicitly focused on AI consciousness, AI moral status, '
     'and digital minds as an applied research agenda.'),
    ('consciousness-science',    'Consciousness Science',
     'Organisations whose primary home is the empirical and theoretical science of consciousness. '
     'Work on neural correlates, global workspace, and integrated information provides direct '
     'empirical grounding for AI consciousness debates.'),
    ('philosophy-of-mind',       'Philosophy of Mind',
     'Academic philosophers working on consciousness, phenomenology, and the nature of mind, '
     'supplying the conceptual and analytical foundations on which digital minds questions rest.'),
    ('animal-sentience',         'Animal Sentience',
     'Organisations studying sentience and welfare in non-human animals. Methods for attributing '
     'sentience in the absence of verbal report are a close analogue for AI welfare research.'),
    ('ai-lab-programs',          'AI Lab Programmes',
     'Internal research programmes within frontier AI labs working on consciousness, model welfare, '
     'or interpretability with direct relevance to questions of AI sentience.'),
    ('ethics-law-moral-status',  'Ethics, Law & Moral Status',
     'Research groups and organisations whose primary contribution is normative, legal, or philosophical '
     'analysis of AI moral status, personhood, and legal standing. Eligibility requires published work '
     'directly engaging AI consciousness, sentience, or moral status.'),
    ('policy-governance',        'Policy & Governance',
     'Government bodies, regulatory agencies, and governance-focused organisations engaging with '
     'digital minds questions in policy and regulatory contexts. Distinct from normative scholarship: '
     'this zone covers institutions with formal or quasi-formal governance roles.'),
]

SUBGROUPS = [
    ('funders',         'Funders',
     'Philanthropic organisations and grant-makers actively funding digital minds, '
     'AI consciousness, or AI welfare research.'),
    ('onboarding',      'Onboarding & Training',
     'Fellowship programmes, training initiatives, and community organisations building '
     'capacity and entry pathways into the field.'),
    ('journals',        'Journals',
     'Academic journals with a track record of publishing work on AI consciousness, '
     'welfare, or closely related questions.'),
    ('community-media', 'Community & Media',
     'Forums, newsletters, and hubs shaping professional and public discourse around digital minds.'),
]

ALL_FILTERS = ZONES + SUBGROUPS

ZONE_LABELS = {f: label for f, label, _ in ALL_FILTERS}
ZONE_DESCS  = {f: desc  for f, label, desc in ALL_FILTERS}

# ---------------------------------------------------------------------------
# Compute zone counts for key findings
# ---------------------------------------------------------------------------
zone_counts = {}
for o in orgs:
    z = o['zone'] or o['subgroup']
    zone_counts[z] = zone_counts.get(z, 0) + 1

# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------
orgs_json = json.dumps(orgs, ensure_ascii=False)
zone_descs_json = json.dumps(ZONE_DESCS, ensure_ascii=False)

tab_rows_html = ''

# Research row
tab_rows_html += '    <div class="tab-row">\n'
tab_rows_html += '      <span class="tab-row-label">Research</span>\n'
for filt, label, _ in ZONES:
    active = ' active' if filt == 'ai-consciousness-welfare' else ''
    escaped_label = label.replace('&', '&amp;')
    tab_rows_html += f'      <span class="zone-tab{active}" data-filter="{filt}">{escaped_label}</span>\n'
tab_rows_html += '    </div>\n'

# Field Support row
tab_rows_html += '    <div class="tab-row">\n'
tab_rows_html += '      <span class="tab-row-label">Field Support</span>\n'
for filt, label, _ in SUBGROUPS:
    tab_rows_html += f'      <span class="zone-tab" data-filter="{filt}">{label}</span>\n'
tab_rows_html += '    </div>\n'

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Digital Minds — Organisation Directory</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --bg:#f0f4f8; --surface:#ffffff; --border:#d6e0ea;
  --text:#0f1f2e; --muted:#4a6070; --faint:#8fa4b8;
  --z1:#1d6fa4; --z2:#4a6fa5; --z3:#1a5f7a;
  --z4:#5a7fa0; --z5:#2d4a6b; --z6:#1e3a5f; --z7:#4a5a72;
  --sg-funders:#1d5c9a; --sg-onboarding:#1a7060; --sg-journals:#4a5a9a; --sg-media:#607a90;
  --accent-warm:#8a5a3a;
}}
body {{ font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif; background:var(--bg); color:var(--text); font-size:13px; line-height:1.5; -webkit-font-smoothing:antialiased; }}

/* --- Header --- */
.page-header {{ padding:36px 20px 0; max-width:1600px; margin:0 auto; }}
.page-header h1 {{ font-size:22px; font-weight:600; letter-spacing:-0.02em; color:var(--text); margin-bottom:2px; }}
.page-header .subtitle {{ font-size:13px; color:var(--muted); margin-bottom:12px; }}
.page-header .intro {{ font-size:12.5px; color:var(--muted); line-height:1.7; font-weight:300; max-width:900px; }}
.page-header .attribution {{ font-size:11px; color:var(--faint); margin-top:8px; }}
.page-header .attribution a {{ color:var(--z3); text-decoration:none; border-bottom:1px solid transparent; transition:border-color .12s; }}
.page-header .attribution a:hover {{ border-bottom-color:var(--z3); }}

/* --- Collapsible panels --- */
.panel-row {{ display:flex; gap:0; max-width:1600px; margin:20px auto 0; padding:0 20px; }}
.panel {{
  flex:1; background:var(--surface); border:1px solid var(--border);
  font-size:12px; line-height:1.7; color:var(--muted); overflow:hidden;
}}
.panel:first-child {{ border-right:none; }}
.panel summary {{
  cursor:pointer; padding:10px 16px; font-size:11px; font-weight:600;
  letter-spacing:.06em; text-transform:uppercase; color:var(--text);
  list-style:none; display:flex; align-items:center; gap:8px;
  user-select:none; transition:background .12s;
}}
.panel summary:hover {{ background:#f7fafd; }}
.panel summary::before {{
  content:''; display:inline-block; width:0; height:0;
  border-left:4px solid var(--faint); border-top:3px solid transparent; border-bottom:3px solid transparent;
  transition:transform .15s;
}}
.panel[open] summary::before {{ transform:rotate(90deg); }}
.panel summary::-webkit-details-marker {{ display:none; }}
.panel-body {{ padding:0 16px 14px; font-weight:300; }}
.panel-body ul {{ margin:0; padding-left:16px; }}
.panel-body li {{ margin-bottom:6px; }}
.panel-body li strong {{ font-weight:500; color:var(--text); }}
.panel-body p {{ margin-bottom:8px; }}
.panel-body .method-note {{ font-size:11px; color:var(--faint); margin-top:8px; font-style:italic; }}

/* --- Filter bar --- */
.filter-bar {{ padding:20px 20px 0; max-width:1600px; margin:0 auto; display:flex; flex-direction:column; gap:14px; }}
.filter-row {{ display:flex; align-items:center; gap:20px; flex-wrap:wrap; }}

.search-wrap {{ position:relative; flex-shrink:0; }}
.search-input {{
  width:220px; padding:6px 0 6px 22px; border:none;
  border-bottom:1.5px solid var(--border); background:transparent;
  font-family:inherit; font-size:13px; color:var(--text); outline:none; transition:border-color .15s;
}}
.search-input:focus {{ border-bottom-color:var(--text); }}
.search-input::placeholder {{ color:var(--faint); }}
.search-icon {{ position:absolute; left:0; top:50%; transform:translateY(-50%); color:var(--faint); font-size:13px; pointer-events:none; }}

.tab-section {{ display:flex; flex-direction:column; gap:0; }}
.tab-row {{ display:flex; align-items:center; flex-wrap:wrap; border-bottom:1.5px solid var(--border); }}
.tab-row-label {{
  font-size:9.5px; font-weight:600; letter-spacing:.1em; text-transform:uppercase;
  color:var(--faint); width:110px; flex-shrink:0; padding:10px 0;
}}
.zone-tab {{
  font-size:12.5px; font-weight:400; color:var(--muted); cursor:pointer;
  padding:10px 0; margin-right:20px; border-bottom:2.5px solid transparent;
  transition:color .12s, border-color .12s; position:relative; top:1.5px;
  white-space:nowrap; user-select:none;
}}
.zone-tab:hover {{ color:var(--text); }}
.zone-tab.active {{ color:var(--text); font-weight:600; border-bottom-color:var(--text); }}
.zone-tab[data-filter="consciousness-science"].active    {{ border-bottom-color:var(--z1); color:var(--z1); }}
.zone-tab[data-filter="philosophy-of-mind"].active       {{ border-bottom-color:var(--z2); color:var(--z2); }}
.zone-tab[data-filter="ai-consciousness-welfare"].active {{ border-bottom-color:var(--z3); color:var(--z3); }}
.zone-tab[data-filter="animal-sentience"].active         {{ border-bottom-color:var(--z4); color:var(--z4); }}
.zone-tab[data-filter="ai-lab-programs"].active          {{ border-bottom-color:var(--z5); color:var(--z5); }}
.zone-tab[data-filter="ethics-law-moral-status"].active  {{ border-bottom-color:var(--z7); color:var(--z7); }}
.zone-tab[data-filter="policy-governance"].active        {{ border-bottom-color:var(--z6); color:var(--z6); }}
.zone-tab[data-filter="funders"].active     {{ border-bottom-color:var(--sg-funders);    color:var(--sg-funders); }}
.zone-tab[data-filter="onboarding"].active  {{ border-bottom-color:var(--sg-onboarding); color:var(--sg-onboarding); }}
.zone-tab[data-filter="journals"].active    {{ border-bottom-color:var(--sg-journals);   color:var(--sg-journals); }}
.zone-tab[data-filter="community-media"].active {{ border-bottom-color:var(--sg-media);  color:var(--sg-media); }}

.zone-description {{
  max-width:1600px; margin:0 auto; padding:14px 20px 0;
  font-size:12px; color:var(--muted); font-weight:300; line-height:1.6;
  min-height:2.4em;
}}

.filter-selects {{ display:flex; gap:12px; margin-left:auto; }}
.filter-select {{
  border:none; border-bottom:1.5px solid var(--border); background:transparent;
  font-family:inherit; font-size:12.5px; color:var(--muted); padding:4px 18px 4px 0;
  outline:none; cursor:pointer; appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%238fa4b8'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 2px center;
  transition:border-color .15s, color .15s;
}}
.filter-select:focus {{ border-bottom-color:var(--text); color:var(--text); }}

/* --- Grid & cards --- */
.grid {{
  display:grid;
  grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
  gap:0; padding:20px;
  max-width:1600px; margin:0 auto;
  border-left:1px solid var(--border); border-top:1px solid var(--border);
  box-sizing:border-box;
}}
.card {{
  background:var(--surface); padding:18px 20px 16px;
  border-right:1px solid var(--border); border-bottom:1px solid var(--border);
  display:flex; flex-direction:column; gap:10px; cursor:pointer;
  transition:background .12s; position:relative;
  border-top:3px solid var(--card-accent,var(--border));
}}
.card:hover {{ background:#f7fafd; }}
.card[data-zone="consciousness-science"]    {{ --card-accent:var(--z1); }}
.card[data-zone="philosophy-of-mind"]       {{ --card-accent:var(--z2); }}
.card[data-zone="ai-consciousness-welfare"] {{ --card-accent:var(--z3); }}
.card[data-zone="animal-sentience"]         {{ --card-accent:var(--z4); }}
.card[data-zone="ai-lab-programs"]          {{ --card-accent:var(--z5); }}
.card[data-zone="ethics-law-moral-status"]  {{ --card-accent:var(--z7); }}
.card[data-zone="policy-governance"]        {{ --card-accent:var(--z6); }}
.card[data-subgroup="funders"]       {{ --card-accent:var(--sg-funders); }}
.card[data-subgroup="onboarding"]    {{ --card-accent:var(--sg-onboarding); }}
.card[data-subgroup="journals"]      {{ --card-accent:var(--sg-journals); }}
.card[data-subgroup="community-media"] {{ --card-accent:var(--sg-media); }}

.cross-listed-badge {{
  display:inline-block; font-size:9.5px; font-weight:500; letter-spacing:.04em;
  color:var(--faint); border:1px solid var(--border);
  padding:1px 5px; margin-top:2px;
}}

.card-header {{ display:flex; align-items:flex-start; justify-content:space-between; gap:12px; }}
.card-header-left {{ flex:1; min-width:0; }}
.card-name {{ font-size:13px; font-weight:600; color:var(--text); line-height:1.3; letter-spacing:-0.01em; }}
.card-sublabel {{ font-size:10px; font-weight:500; letter-spacing:.06em; text-transform:uppercase; color:var(--card-accent,var(--faint)); margin-top:3px; }}
.logo {{ width:68px; height:68px; flex-shrink:0; object-fit:contain; opacity:.9; }}
.logo-placeholder {{ width:68px; height:68px; flex-shrink:0; }}

.card-meta {{ font-size:11px; color:var(--muted); display:flex; align-items:center; gap:6px; flex-wrap:wrap; }}
.type-badge {{
  font-size:9.5px; font-weight:500; letter-spacing:.04em;
  color:var(--muted); border:1px solid var(--border);
  padding:1px 6px; display:inline-block; flex-shrink:0;
}}
.meta-sep {{ color:var(--border); user-select:none; }}

.card-description {{ font-size:12px; color:var(--muted); line-height:1.6; font-weight:300; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }}
.card-footer {{ display:flex; justify-content:flex-end; padding-top:2px; }}
.card-link {{ font-size:11px; color:var(--faint); text-decoration:none; border-bottom:1px solid transparent; transition:color .12s,border-color .12s; }}
.card-link:hover {{ color:var(--text); border-bottom-color:var(--border); }}
.no-results {{ grid-column:1/-1; background:var(--surface); text-align:center; padding:60px; color:var(--faint); font-size:13px; }}

/* --- Modal --- */
.modal-backdrop {{ display:none; position:fixed; inset:0; background:rgba(15,31,46,.45); backdrop-filter:blur(4px); z-index:100; align-items:center; justify-content:center; padding:20px; }}
.modal-backdrop.open {{ display:flex; }}
.modal {{
  background:var(--surface); max-width:560px; width:100%; max-height:90vh;
  overflow-y:auto; padding:32px 36px; position:relative;
  border-top:4px solid var(--card-accent,var(--border));
}}
.modal-close {{
  position:absolute; top:16px; right:20px; background:none; border:none;
  font-size:20px; color:var(--faint); cursor:pointer; line-height:1; padding:4px;
}}
.modal-close:hover {{ color:var(--text); }}
.modal-org-name {{ font-size:17px; font-weight:600; letter-spacing:-0.02em; color:var(--text); margin-bottom:4px; }}
.modal-zone {{ font-size:10px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--card-accent,var(--faint)); margin-bottom:16px; }}
.modal-logo {{ width:48px; height:48px; object-fit:contain; opacity:.9; margin-bottom:12px; display:block; }}
.modal-description {{ font-size:13px; color:var(--muted); line-height:1.7; font-weight:300; margin-bottom:20px; }}
.modal-meta-table {{ width:100%; border-collapse:collapse; font-size:12px; }}
.modal-meta-table td {{ padding:5px 0; vertical-align:top; }}
.modal-meta-table td:first-child {{ color:var(--faint); width:110px; font-size:11px; letter-spacing:.03em; }}
.modal-meta-table td:last-child {{ color:var(--text); }}
.modal-section {{ margin-top:16px; }}
.modal-section-label {{ font-size:10px; font-weight:600; letter-spacing:.06em; text-transform:uppercase; color:var(--faint); margin-bottom:6px; }}
.modal-section-list {{ list-style:none; padding:0; margin:0; }}
.modal-section-list li {{ font-size:12px; color:var(--muted); line-height:1.6; font-weight:300; padding:3px 0; }}
.modal-section-list li strong {{ font-weight:500; color:var(--text); }}
.modal-section-list a {{ color:var(--z3); text-decoration:none; border-bottom:1px solid transparent; transition:border-color .12s; }}
.modal-section-list a:hover {{ border-bottom-color:var(--z3); }}
.modal-section-list li strong a {{ font-weight:500; color:var(--text); border-bottom:1px dotted var(--border); }}
.modal-section-list li strong a:hover {{ border-bottom-color:var(--text); color:var(--z3); }}
.modal-citations li {{ font-style:italic; border-bottom:1px solid var(--bg); }}
.modal-citations li a {{ font-style:italic; }}
.modal-citations li:last-child {{ border-bottom:none; }}
.modal-link {{ display:inline-block; margin-top:20px; font-size:12px; color:var(--z3); text-decoration:none; border-bottom:1px solid transparent; transition:border-color .12s; }}
.modal-link:hover {{ border-bottom-color:var(--z3); }}

/* --- Footer --- */
.page-footer {{
  max-width:1600px; margin:0 auto; padding:24px 20px 36px;
  font-size:11px; color:var(--faint); line-height:1.6;
  border-top:1px solid var(--border);
}}

/* --- Responsive --- */
@media (max-width:700px) {{
  .panel-row {{ flex-direction:column; }}
  .panel:first-child {{ border-right:1px solid var(--border); border-bottom:none; }}
  .tab-row-label {{ width:80px; }}
  .filter-selects {{ margin-left:0; }}
}}
</style>
</head>
<body>

<div class="page-header">
  <h1>Digital Minds — Organisation Directory</h1>
  <p class="subtitle">{org_count} organisations active in AI consciousness, AI welfare, and digital minds research.</p>
  <p class="intro">
    This directory maps the organisational actors in the digital minds field &mdash; the interdisciplinary space
    concerned with whether AI systems might be conscious, sentient, or moral patients, and what follows from that.
    It covers research centres, university groups, AI lab programmes, funding bodies, training programmes, and
    community organisations, organised into six research zones and four field-support categories.
  </p>
  <p class="attribution">
    Produced by <strong>PRISM</strong> &mdash; Partnership for Research Into Sentient Machines.
    Survey date: March 2026. PRISM is itself included in this directory.
  </p>
</div>

<div class="panel-row">
  <details class="panel">
    <summary>About this map</summary>
    <div class="panel-body">
      <p>
        The corpus was assembled through four systematic search rounds in March 2026, using seed sources
        (PRISM researcher network, EA Forum, 80,000 Hours, web search) and snowball sampling from included
        organisations. Each candidate was classified as <strong>included</strong> (explicit digital minds focus),
        <strong>adjacent</strong> (relevant but outside core boundary), or <strong>excluded</strong> (documented
        with rationale). Only included organisations appear in this directory.
      </p>
      <p>
        Organisations are assigned to one of six topical zones based on primary research focus, or to a
        field-support category (funders, training, journals, community). Funding bodies must demonstrate
        confirmed grantmaking in digital minds research, not merely declared interest. Individual researchers
        without institutional anchors are excluded.
      </p>
      <p class="method-note">
        Limitations: search conducted primarily in English; non-English-language sources not systematically covered;
        private companies without public research output may exist below the visibility threshold. The full
        methodology protocol and decision log are available in the accompanying dataset.
      </p>
    </div>
  </details>
</div>

<div class="filter-bar">
  <div class="filter-row">
    <div class="search-wrap">
      <span class="search-icon">&#9906;</span>
      <input class="search-input" type="search" id="search" placeholder="Search organisations…" autocomplete="off">
    </div>
    <div class="filter-selects">
      <select class="filter-select" id="type-select">
        <option value="">All types</option>
        <option value="nonprofit">Nonprofit</option>
        <option value="university-centre">University Centre</option>
        <option value="lab-team">Lab Team</option>
        <option value="funding-body">Funder</option>
        <option value="media">Media</option>
        <option value="community">Community</option>
      </select>
      <select class="filter-select" id="geo-select">
        <option value="">All geographies</option>
        <option value="USA">USA</option>
        <option value="UK">UK</option>
        <option value="Europe">Europe</option>
        <option value="Asia-Pacific">Asia-Pacific</option>
        <option value="International">International</option>
      </select>
    </div>
  </div>

  <div class="tab-section">
{tab_rows_html}  </div>
</div>

<div class="zone-description" id="zone-description"></div>

<div class="grid" id="grid"></div>

<div class="modal-backdrop" id="modal-backdrop">
  <div class="modal" id="modal" role="dialog" aria-modal="true">
    <button class="modal-close" id="modal-close" aria-label="Close">&times;</button>
    <div class="modal-body" id="modal-body"></div>
  </div>
</div>

<div class="page-footer">
  PRISM &mdash; Partnership for Research Into Sentient Machines &middot; Survey date: March 2026 &middot;
  Corpus version 1.0 &middot; {org_count} included organisations
</div>

<script>
const ORGS = {orgs_json};
const ZONE_LABELS = {json.dumps(ZONE_LABELS, ensure_ascii=False)};
const ZONE_DESCS  = {zone_descs_json};

let activeFilter = 'ai-consciousness-welfare';
let activeType   = '';
let activeGeo    = '';
let searchQuery  = '';

function matchesFilter(card) {{
  const f = activeFilter;
  const zoneMatch = card.dataset.zone === f || card.dataset.zoneSecondary === f;
  const sgMatch   = card.dataset.subgroup === f;
  return zoneMatch || sgMatch;
}}

function renderCards() {{
  const grid = document.getElementById('grid');
  const q = searchQuery.toLowerCase();
  let visible = 0;
  document.querySelectorAll('.card').forEach(card => {{
    const typeOk = !activeType || card.dataset.type === activeType;
    const geoOk  = !activeGeo  || card.dataset.geoRegion === activeGeo;
    const filterOk = matchesFilter(card);
    const searchOk = !q || card.dataset.search.includes(q);
    const show = filterOk && typeOk && geoOk && searchOk;
    card.style.display = show ? '' : 'none';
    if (show) visible++;
  }});
  document.getElementById('no-results').style.display = visible ? 'none' : '';
}}

function updateDescription() {{
  const el = document.getElementById('zone-description');
  el.textContent = ZONE_DESCS[activeFilter] || '';
}}

function buildGrid() {{
  const grid = document.getElementById('grid');
  ORGS.forEach(o => {{
    const card = document.createElement('div');
    card.className = 'card';
    card.dataset.zone = o.zone;
    card.dataset.zoneSecondary = o.zone_secondary || '';
    card.dataset.subgroup = o.subgroup || '';
    card.dataset.type = o.type;
    card.dataset.geo  = o.geography;
    card.dataset.geoRegion = o.geo_region;
    card.dataset.search = (o.name + ' ' + o.description + ' ' + o.geography + ' ' + (o.key_figures || '')).toLowerCase();

    const accentZone = o.zone || (o.subgroup ? '' : '');
    if (o.subgroup) card.dataset.subgroup = o.subgroup;

    const logoHtml = o.logo_slug
      ? `<img class="logo" src="logos/${{o.logo_slug}}.png" alt="${{o.name}}" onerror="this.style.display='none'">`
      : `<div class="logo-placeholder"></div>`;

    const zoneLabel = ZONE_LABELS[o.zone] || ZONE_LABELS[o.subgroup] || '';
    const crossBadge = o.zone_secondary
      ? `<span class="cross-listed-badge">also: ${{ZONE_LABELS[o.zone_secondary] || o.zone_secondary}}</span>`
      : '';

    const typeBadge = `<span class="type-badge">${{o.type_label}}</span>`;
    const metaText = o.geography ? `<span class="meta-sep">&middot;</span> ${{o.geography}}` : '';

    card.innerHTML = `
      <div class="card-header">
        <div class="card-header-left">
          <div class="card-name">${{o.name}}</div>
          <div class="card-sublabel">${{zoneLabel}}</div>
          ${{crossBadge}}
        </div>
        ${{logoHtml}}
      </div>
      <div class="card-meta">${{typeBadge}}${{metaText}}</div>
      <div class="card-description">${{o.description}}</div>
      <div class="card-footer">
        <a class="card-link" href="${{o.url}}" target="_blank" rel="noopener" onclick="event.stopPropagation()">Visit &rarr;</a>
      </div>
    `;

    card.addEventListener('click', () => openModal(o));
    grid.appendChild(card);
  }});

  const noResults = document.createElement('div');
  noResults.className = 'no-results';
  noResults.id = 'no-results';
  noResults.textContent = 'No organisations match the current filters.';
  noResults.style.display = 'none';
  grid.appendChild(noResults);
}}

function openModal(o) {{
  const modal = document.getElementById('modal');
  const body  = document.getElementById('modal-body');
  const zoneLabel  = ZONE_LABELS[o.zone] || ZONE_LABELS[o.subgroup] || '';
  const alsoLabel  = o.zone_secondary ? ` · also: ${{ZONE_LABELS[o.zone_secondary] || o.zone_secondary}}` : '';

  // Compute accent colour for modal top border
  const src = document.querySelector(`[data-zone="${{o.zone}}"], [data-subgroup="${{o.subgroup}}"]`);
  if (src) {{
    modal.style.setProperty('--card-accent', getComputedStyle(src).getPropertyValue('--card-accent'));
  }}

  const logoHtml = o.logo_slug
    ? `<img class="modal-logo" src="logos/${{o.logo_slug}}.png" alt="${{o.name}}" onerror="this.style.display='none'">`
    : '';
  // Parse pipe-delimited links: "Text|URL" or just "Text"
  function linkify(text, url) {{
    return url ? `<a href="${{url}}" target="_blank" rel="noopener">${{text}}</a>` : text;
  }}

  const peopleHtml = o.key_figures
    ? `<div class="modal-section">
        <div class="modal-section-label">People</div>
        <ul class="modal-section-list">
          ${{o.key_figures.split(';').map(s => {{
            const t = s.trim();
            // Split on last pipe to get URL if present
            const pipeIdx = t.lastIndexOf('|');
            const entry = pipeIdx > -1 ? t.substring(0, pipeIdx).trim() : t;
            const url = pipeIdx > -1 ? t.substring(pipeIdx + 1).trim() : '';
            const m = entry.match(/^(.+?)\\s*\\((.+)\\)$/);
            if (m) {{
              const nameHtml = url ? `<a href="${{url}}" target="_blank" rel="noopener">${{m[1]}}</a>` : m[1];
              return `<li><strong>${{nameHtml}}</strong>, ${{m[2]}}</li>`;
            }}
            return `<li>${{url ? `<a href="${{url}}" target="_blank" rel="noopener">${{entry}}</a>` : entry}}</li>`;
          }}).join('')}}
        </ul>
      </div>`
    : '';

  const outputsHtml = o.key_outputs
    ? `<div class="modal-section">
        <div class="modal-section-label">Selected research</div>
        <ul class="modal-section-list modal-citations">
          ${{o.key_outputs.split(';').map(s => {{
            const t = s.trim();
            const pipeIdx = t.lastIndexOf('|');
            if (pipeIdx > -1) {{
              const text = t.substring(0, pipeIdx).trim();
              const url = t.substring(pipeIdx + 1).trim();
              return `<li><a href="${{url}}" target="_blank" rel="noopener">${{text}}</a></li>`;
            }}
            return `<li>${{t}}</li>`;
          }}).join('')}}
        </ul>
      </div>`
    : '';

  body.innerHTML = `
    ${{logoHtml}}
    <div class="modal-org-name">${{o.name}}</div>
    <div class="modal-zone">${{zoneLabel}}${{alsoLabel}}</div>
    <div class="modal-description">${{o.description}}</div>
    <table class="modal-meta-table">
      <tr><td>Type</td><td>${{o.type_label}}</td></tr>
      <tr><td>Geography</td><td>${{o.geography}}</td></tr>
    </table>
    ${{peopleHtml}}
    ${{outputsHtml}}
    <a class="modal-link" href="${{o.url}}" target="_blank" rel="noopener">Visit website &rarr;</a>
  `;

  document.getElementById('modal-backdrop').classList.add('open');
}}

document.getElementById('modal-close').addEventListener('click', () => {{
  document.getElementById('modal-backdrop').classList.remove('open');
}});
document.getElementById('modal-backdrop').addEventListener('click', e => {{
  if (e.target === document.getElementById('modal-backdrop'))
    document.getElementById('modal-backdrop').classList.remove('open');
}});
document.addEventListener('keydown', e => {{
  if (e.key === 'Escape') document.getElementById('modal-backdrop').classList.remove('open');
}});

document.querySelectorAll('.zone-tab').forEach(tab => {{
  tab.addEventListener('click', () => {{
    document.querySelectorAll('.zone-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    activeFilter = tab.dataset.filter;
    updateDescription();
    renderCards();
  }});
}});

document.getElementById('search').addEventListener('input', e => {{
  searchQuery = e.target.value;
  renderCards();
}});
document.getElementById('type-select').addEventListener('change', e => {{
  activeType = e.target.value;
  renderCards();
}});
document.getElementById('geo-select').addEventListener('change', e => {{
  activeGeo = e.target.value;
  renderCards();
}});

buildGrid();
updateDescription();
renderCards();
</script>
</body>
</html>
"""

out_path = os.path.join(ROOT, 'outputs', 'directory.html')
with open(out_path, 'w') as f:
    f.write(HTML)

size = os.path.getsize(out_path)
print(f"Written: {out_path} ({size:,} bytes, {org_count} orgs)")
