from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE ='mysql+pymysql://ct201/109277/22@localhost:3306/Blog_Application'

engine=create_engine(URL_DATABASE)

SessionLocal=sessionmaker(autocommit=False,autoflash=False,bind=engine)

Base=declarative_base()

 