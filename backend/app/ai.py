import json
from groq import Groq
from .config import settings
class AI:
 def __init__(self): self.client=Groq(api_key=settings.groq_api_key) if settings.groq_api_key else None
 def json(self,system,user,fallback=None):
  if not self.client:return fallback or {}
  r=self.client.chat.completions.create(model=settings.groq_model,temperature=.2,messages=[{'role':'system','content':system},{'role':'user','content':user}])
  raw=(r.choices[0].message.content or '').strip()
  if raw.startswith('```'): raw=raw.split('```',2)[1].removeprefix('json').strip()
  try:return json.loads(raw)
  except:return fallback or {}
ai=AI()
