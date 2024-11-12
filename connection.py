from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.sql_model import BASE

db_user: str  = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = '1234'
uri:str = F'postgresql+pg8000://{db_user}:{db_password}@{db_host}:{db_port}/to-do' #sqlalchemy use URI to connect with db


engine = create_engine(uri)

BASE.metadata.create_all(bind=engine)



#session 
#sessionmaker  is  factory function that create new session object.In SQLAlchemy is essentially a "workspace" where you can query and interact with the db.
session = sessionmaker( 
        bind = engine, #SQLAlchemy that the session should be connected to the previously created engine
        autoflush=True #automatically update changes , sync
)
#why use session ?
#The session abstracts database operations so that you can work with Python objects instead of SQL statements


db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print("Connected")
except Exception as e:
    print(str(e))