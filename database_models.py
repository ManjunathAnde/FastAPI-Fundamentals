from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

dec_base= declarative_base() #should be inherited for passing db schema to db using sqlalchemy

class Products(dec_base):  #Schema for db instance. This is the blueprint for the table in db
    __tablename__ = "fastapi_main"  #table_name in our db
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(Float(20))
    quantity = Column(Integer)