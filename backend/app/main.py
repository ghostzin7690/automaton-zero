from pathlib import Path
from fastapi import FastAPI,Depends,Header,HTTPException,Request
from fastapi.responses import FileResponse,HTMLResponse
from sqlalchemy.orm import Session
from .config import settings
from .db import init_db,get_db
from .models import Opportunity,Product,Experiment,Event
from .research import ResearchEngine
from .decision import DecisionEngine
from .product_factory import ProductFactory
from .ai import ai
app=FastAPI(title='Automaton V4')
@app.on_event('startup')
def startup():init_db()
def auth(t):
 if settings.run_token and t!=settings.run_token:raise HTTPException(401,'Token inválido')
@app.get('/health')
def health():return {'ok':True,'mode':settings.mode}
@app.get('/dashboard',response_class=HTMLResponse)
def dash():return HTMLResponse(Path(__file__).with_name('dashboard.html').read_text())
@app.post('/api/research/run')
def research(x_run_token:str|None=Header(default=None),db:Session=Depends(get_db)):
 auth(x_run_token); r=ResearchEngine().search(['problemas que pessoas querem resolver','produtos digitais procurados','tendências de compra online Brasil','o que pessoas querem aprender'],25); ev='\n'.join(f"- {x['title']}: {x['summary']}" for x in r[:20]); data=ai.json('Analise mercado rigorosamente.',f'Retire até 5 oportunidades deste material:\n{ev}\nJSON: {{"opportunities":[{{"niche":"","audience":"","problem":"","score":0}}]}}',{'opportunities':[]})
 for o in data.get('opportunities',[]):db.add(Opportunity(niche=o.get('niche',''),audience=o.get('audience',''),problem=o.get('problem',''),evidence={'sources':r},score=float(o.get('score',0))))
 db.commit();return {'sources':len(r),'opportunities':data.get('opportunities',[])}
@app.get('/api/opportunities')
def opps(db:Session=Depends(get_db)):return [{'id':x.id,'niche':x.niche,'audience':x.audience,'problem':x.problem,'score':x.score} for x in db.query(Opportunity).order_by(Opportunity.score.desc()).limit(30)]
@app.post('/api/opportunities/{oid}/build')
def build(oid:int,x_run_token:str|None=Header(default=None),db:Session=Depends(get_db)):
 auth(x_run_token);o=db.get(Opportunity,oid)
 if not o:raise HTTPException(404,'Oportunidade não encontrada')
 d=DecisionEngine().choose_opportunity(o.score)
 if d.action!='VALIDATE_OPPORTUNITY':raise HTTPException(409,d.reason)
 data,pdf=ProductFactory().create({'niche':o.niche,'audience':o.audience,'problem':o.problem});p=Product(opportunity_id=o.id,name=data['name'],price=float(data.get('price',19.9)),pdf_path=pdf,status='ready');db.add(p);db.commit();return {'id':p.id,'name':p.name,'pdf':f'/api/products/{p.id}/pdf'}
@app.get('/api/products')
def products(db:Session=Depends(get_db)):return [{'id':p.id,'name':p.name,'price':p.price,'status':p.status,'checkout_url':p.checkout_url} for p in db.query(Product).order_by(Product.id.desc()).limit(50)]
@app.get('/api/products/{pid}/pdf')
def pdf(pid:int,db:Session=Depends(get_db)):
 p=db.get(Product,pid)
 if not p or not Path(p.pdf_path).exists():raise HTTPException(404,'PDF não encontrado')
 return FileResponse(p.pdf_path,media_type='application/pdf',filename=Path(p.pdf_path).name)
@app.post('/api/products/{pid}/checkout')
def checkout(pid:int,payload:dict,x_run_token:str|None=Header(default=None),db:Session=Depends(get_db)):
 auth(x_run_token);p=db.get(Product,pid);u=payload.get('checkout_url','')
 if not p or not u.startswith(('http://','https://')):raise HTTPException(400,'Produto/URL inválido')
 p.checkout_url=u;p.status='published';db.commit();return {'ok':True}
@app.post('/api/experiments/{eid}/metrics')
def metrics(eid:int,payload:dict,x_run_token:str|None=Header(default=None),db:Session=Depends(get_db)):
 auth(x_run_token);e=db.get(Experiment,eid)
 if not e:raise HTTPException(404,'Experimento não encontrado')
 for k in ['impressions','clicks','sales','revenue','cost']:
  if k in payload:setattr(e,k,payload[k])
 d=DecisionEngine().optimize_experiment(e.impressions,e.clicks,e.sales,e.revenue,e.cost);e.result=d.action;db.commit();return {'decision':d.__dict__}
@app.post('/api/webhooks/kiwify')
async def webhook(request:Request,db:Session=Depends(get_db)):
 db.add(Event(event_type='kiwify_webhook',payload=await request.json()));db.commit();return {'received':True}
