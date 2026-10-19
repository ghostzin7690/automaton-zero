from dataclasses import dataclass
@dataclass
class Decision:
 action:str; reason:str; confidence:float; requires_human:bool=False
class DecisionEngine:
 def choose_opportunity(self,score): return Decision('VALIDATE_OPPORTUNITY','Evidência suficiente para MVP.',.8) if score>=70 else Decision('RESEARCH_MORE','Evidência insuficiente.',.65)
 def optimize_experiment(self,impressions,clicks,sales,revenue,cost):
  cvr=sales/clicks if clicks else 0; profit=revenue-cost
  if sales>=10 and cvr>=.02 and profit>0:return Decision('SCALE_WINNER','Volume, conversão e lucro sustentam escala.',.9)
  if clicks>=30 and sales==0:return Decision('CHANGE_OFFER','Há interesse, mas a oferta não converte.',.84)
  if impressions>=300 and clicks<5:return Decision('CHANGE_CONTENT','Pouca atração.',.82)
  return Decision('KEEP_TESTING','Ainda faltam dados.',.6)
