from datetime import datetime,timezone
from sqlalchemy import String,Text,Float,Integer,DateTime,Boolean,JSON
from sqlalchemy.orm import Mapped,mapped_column
from .db import Base
def now(): return datetime.now(timezone.utc)
class Opportunity(Base):
 __tablename__='opportunities'; id:Mapped[int]=mapped_column(Integer,primary_key=True); niche:Mapped[str]=mapped_column(String(200)); audience:Mapped[str]=mapped_column(String(300)); problem:Mapped[str]=mapped_column(Text()); evidence:Mapped[dict]=mapped_column(JSON,default=dict); score:Mapped[float]=mapped_column(Float,default=0); status:Mapped[str]=mapped_column(String(40),default='candidate'); created_at:Mapped[datetime]=mapped_column(DateTime,default=now)
class Product(Base):
 __tablename__='products'; id:Mapped[int]=mapped_column(Integer,primary_key=True); opportunity_id:Mapped[int|None]=mapped_column(Integer,nullable=True); name:Mapped[str]=mapped_column(String(250)); price:Mapped[float]=mapped_column(Float,default=0); status:Mapped[str]=mapped_column(String(40),default='draft'); checkout_url:Mapped[str]=mapped_column(Text,default=''); pdf_path:Mapped[str]=mapped_column(Text,default=''); content:Mapped[str]=mapped_column(Text,default=''); created_at:Mapped[datetime]=mapped_column(DateTime,default=now)
class Experiment(Base):
 __tablename__='experiments'; id:Mapped[int]=mapped_column(Integer,primary_key=True); product_id:Mapped[int]=mapped_column(Integer); variant:Mapped[str]=mapped_column(String(100)); impressions:Mapped[int]=mapped_column(Integer,default=0); clicks:Mapped[int]=mapped_column(Integer,default=0); sales:Mapped[int]=mapped_column(Integer,default=0); revenue:Mapped[float]=mapped_column(Float,default=0); cost:Mapped[float]=mapped_column(Float,default=0); result:Mapped[str]=mapped_column(String(40),default='running'); created_at:Mapped[datetime]=mapped_column(DateTime,default=now)
class Event(Base):
 __tablename__='events'; id:Mapped[int]=mapped_column(Integer,primary_key=True); event_type:Mapped[str]=mapped_column(String(100)); payload:Mapped[dict]=mapped_column(JSON,default=dict); created_at:Mapped[datetime]=mapped_column(DateTime,default=now)
class DecisionLog(Base):
 __tablename__='decision_logs'; id:Mapped[int]=mapped_column(Integer,primary_key=True); action:Mapped[str]=mapped_column(String(100)); reason:Mapped[str]=mapped_column(Text); confidence:Mapped[float]=mapped_column(Float,default=0); requires_human:Mapped[bool]=mapped_column(Boolean,default=False); created_at:Mapped[datetime]=mapped_column(DateTime,default=now)
