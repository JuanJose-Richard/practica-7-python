from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

provider = 'mysql+pymysql'
database = 'registrovehiculos'
serverDB = '127.0.0.1'
port = '3306'
user = 'root'
password = ''

engine = create_engine(provider+"://"+user+":"+password+"@"+serverDB+"/"+database+"?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
