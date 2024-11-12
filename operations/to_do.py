import sys
sys.path.append('./')  #this  is add the current directory 

from connection import db_session 
from model.sql_model import Todo
import decoders.todo as decode


#create todo
def create_todo(todo:str) -> dict:
    try:
        #creating new todo list
        req = Todo(todo) # from self.todo , instance of the Todo class
        db_session.add(req) 
        db_session.commit()
        return {
            'status': 'commit',
            'message': 'new todo added'
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
    


# ---------------------------------------------------

#fetcching all todos 
def get_all():
    try:
        res = db_session.query(Todo).all() #query all todo entries from the databse #sql_model
        docs = decode.decode_todos(res) #decode the retrieved todo data  # todo decode
        return {
            'status': 'ok',
            'data': docs
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
    

#get get one
def get_one(_id:int):
    try:
        criteria = {"_id":_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none() #query one todo entries from the databse #sql_model
        if res is not None:
            record = decode.decode(res)
            return {
                'status': 'ok',
                'data':record
            }
        else:
            return{
                'status': 'error',
                'message': f'Record with id {_id} not found'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }
    


#update todo

def update(_id:int, title:str):
    try:
        criteria = {"_id":_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none() #query one todo entries from the databse #sql_model
        if res is not None:
            res.todo = title
            db_session.commit()
            return {
                'status': 'ok',
                'message':'Record updated'
            }
        else:
            return{
                'status': 'error',
                'message': f'Record with id {_id} not found'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

#delete
def delete(_id:int):
    try:
        criteria = {"_id":_id}
        res = db_session.query(Todo).filter_by(**criteria).one_or_none() #query one todo entries from the databse #sql_model
        if res is not None:
            db_session.delete(res)
            db_session.commit()
            return {
                'status': 'ok',
                'message':'Record Deleted'
            }
        else:
            return{
                'status': 'error',
                'message': f'Record with id {_id} not found'
            }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }



# res = create_todo("Machine Learning with Python")
# print(res)

# res = get_all()
# print(res)

# res = get_one(1)
# print(res)

# new = update(2,'Creating a Website')
# print(new)

# delete_todo = delete(2)
# print(delete_todo)