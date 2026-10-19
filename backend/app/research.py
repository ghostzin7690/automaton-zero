import feedparser
from urllib.parse import quote_plus
class ResearchEngine:
 def search(self,queries,limit=30):
  out=[]
  for q in queries:
   try:
    u='https://news.google.com/rss/search?q='+quote_plus(q)+'&hl=pt-BR&gl=BR&ceid=BR:pt-419'
    f=feedparser.parse(u)
    for e in f.entries[:limit]:out.append({'title':e.get('title',''),'url':e.get('link',''),'summary':e.get('summary','')[:1500],'source':'rss'})
   except:pass
  return out[:limit]
