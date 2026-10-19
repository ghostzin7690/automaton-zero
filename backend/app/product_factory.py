from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .ai import ai
OUT=Path('generated');OUT.mkdir(exist_ok=True)
class ProductFactory:
 def create(self,opp):
  d=ai.json('Você cria produtos digitais originais e éticos.',f'''Crie um MVP digital para esta oportunidade: {opp}. Retorne JSON com name,promise,price,audience,modules,sales_copy,social_hooks,disclaimer. Não invente depoimentos ou garantias.''',{'name':'Guia Prático','promise':'Um guia objetivo para testar uma solução.','price':19.9,'audience':opp.get('audience',''),'modules':['Diagnóstico','Planejamento','Execução','Teste','Medição','Próximos passos'],'sales_copy':'Guia prático para sair da ideia e testar.','social_hooks':['Pare de adivinhar.'],'disclaimer':'Conteúdo educacional.'})
  path=OUT/( ''.join(c if c.isalnum() else '_' for c in d['name'])[:60]+'.pdf')
  s=getSampleStyleSheet(); doc=SimpleDocTemplate(str(path),pagesize=A4); story=[Paragraph(d['name'],s['Title']),Paragraph(d['promise'],s['BodyText']),Spacer(1,20)]
  for i,m in enumerate(d.get('modules',[]),1):story += [Paragraph(f'{i}. {m}',s['Heading2']),Paragraph('Aplicação prática, exemplos e checklist.',s['BodyText']),Spacer(1,12)]
  doc.build(story); return d,str(path)
