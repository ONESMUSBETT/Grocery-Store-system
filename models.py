from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,Text,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
Base=declarative_base()
engine = create_engine('sqlite:///initialise.db',echo=True)
Session = sessionmaker(bind=engine)
session=Session()
class products(Base):
    __tablename__ = 'products'
    products_no = Column(Integer,primary_key=True)
    name=Column(String,unique=True,nullable=False)
    units = Column(String)
    price=Column(Integer,nullable=False)
    category = Column(String,nullable=False,default='Un categorised')
    date= Column(DateTime,default=datetime.now().date())
class sales(Base):
    __tablename__ = 'sales'
    sales_no = Column(Integer,primary_key=True,autoincrement=True)
    date = Column(DateTime,default=datetime.now().date())
    totals = Column(Integer,nullable=False)
    recipt_no = Column(Integer,ForeignKey('products.products_no'))
class recipts(Base):
    __tablename__ = 'recipts'
    recipt_no = Column(Integer,primary_key=True,autoincrement=True)
    date = Column(DateTime,default=datetime.now().date())
    info = Column(Text,nullable=False)
    totals = Column(Integer,nullable=False)
class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer,primary_key=True,autoincrement=True)
    fullName=Column(String)
    phone = Column(String)
Base.metadata.create_all(bind = engine)

