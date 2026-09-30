"""One-off source link audit. Never run on a schedule or in the website."""
import json, re, concurrent.futures, urllib.request, urllib.error, datetime
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/catalogue.json').read_text())
urls=sorted({x[field] for key in ['institutions','programs','voices','targets'] for x in data[key] for field in ['url','portal'] if x.get(field)})
def check(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'SocialDataClub-source-review/1.0'}),timeout=18) as res:
            body=res.read(700000).decode('utf-8',errors='replace')
            m=re.search(r'<title[^>]*>(.*?)</title>',body,re.S|re.I)
            return dict(url=url,status=res.status,final_url=res.url,title=re.sub(r'\s+',' ',m.group(1)).strip() if m else '',checked='2026-09-30')
    except urllib.error.HTTPError as e:
        return dict(url=url,status=e.code,error=str(e),checked='2026-09-30')
    except Exception as e:
        return dict(url=url,status=None,error=str(e),checked='2026-09-30')
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    results=list(pool.map(check,urls))
(root/'research/link-audit.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('Checked',len(results),'sources;',sum(x['status']==200 for x in results),'HTTP 200')
for x in results:
    if x['status']!=200: print(x['status'],x['url'],x.get('error',''))
