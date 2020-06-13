import json
from pathlib import Path
import re

p = Path('.')

posts = []

for p in p.rglob('*.md'):
    with p.open() as r:
        match = re.search(r'(?<=^# ).+', r.read())
        title = match.group() if match else 'untitled'

        posts.append({
            'title': title,
            'path': f'{p}',
            'date': p.name[:10]
        })


posts.sort(key=lambda x: x['date'], reverse=True)

with open('meta.json','w') as w:
    w.write(json.dumps(posts, indent=4, ensure_ascii=False))
