"""Validate catalogue integrity and static deployment assets, without network calls."""
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
data = json.loads((root / 'data/catalogue.json').read_text())
errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

groups = {g['id'] for g in data['groups']}
institutions = {i['id']: i for i in data['institutions']}
require(len(institutions) == len(data['institutions']), 'Duplicate institution IDs')
ids = [p['id'] for p in data['programs']]
require(len(set(ids)) == len(ids), 'Duplicate route IDs')
for i in data['institutions']:
    require(i['group'] in groups, f"Unknown group: {i['id']}")
    require(any(p['institution'] == i['id'] for p in data['programs']), f"Institution has no route: {i['id']}")
    for key in ['intro', 'verdict', 'upside', 'downside', 'comparison']:
        require(bool(i.get(key)), f"Missing {key}: {i['id']}")
for p in data['programs']:
    require(p['institution'] in institutions, f"Unknown institution: {p['id']}")
    require(p['group'] == institutions.get(p['institution'], {}).get('group'), f"Group mismatch: {p['id']}")
    require(p['kind'] in ['programa', 'canal', 'destino'], f"Unknown kind: {p['id']}")
    require(p['stage'] in ['pre', 'phd', 'grado', 'experiencia'], f"Unknown stage: {p['id']}")
    require(p['pay'] in ['salary', 'grant', 'unpaid', 'varies', 'unknown'], f"Unknown pay: {p['id']}")
    require(p['priority'] in [1, 2, 3, 4], f"Unknown priority: {p['id']}")
    require(all(t in data['themes'] for t in p['themes']), f"Unknown theme: {p['id']}")
    for key in ['eligibility', 'duration', 'rhythm', 'watch', 'docs', 'fit']:
        require(bool(p.get(key)), f"Missing {key}: {p['id']}")
for record in data['institutions'] + data['programs'] + data['voices']:
    for key in ['url', 'portal']:
        if record.get(key):
            u = urlparse(record[key])
            require(u.scheme in ['https', 'http'] and bool(u.netloc), f"Invalid URL: {record[key]}")
for asset in ['index.html', 'styles.css', 'app.js', 'catalogue.js', 'fuentes.txt']:
    require((root / 'dist' / asset).stat().st_size > 0, f"Empty asset: {asset}")
require((root / 'dist/catalogue.js').read_text().startswith('window.ATLAS = '), 'Missing catalogue global')
js = (root / 'dist/app.js').read_text()
require('fetch(' not in js and 'setInterval(' not in js, 'Unexpected remote fetching or polling')
require(not list((root / 'dist').glob('**/.env*')), 'Unexpected env file in public assets')
if errors:
    raise SystemExit('\n'.join(errors))
print(f"Valid: {len(institutions)} institutions; {len(ids)} routes; {dict(Counter(p['kind'] for p in data['programs']))}")
