from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
import datetime

#function to  return current timestamp
def get_timestamp():
    return datetime.datetime.now()


BASE = declarative_base()

#create our model 
class Todo(BASE):
    __tablename__= 'todo'
    _id = Column(Integer,primary_key=True, autoincrement=True)
    todo =  Column(String)
    timestamp = Column(DateTime, default=get_timestamp)

    def __init__(self, todo):
        self.todo = todo