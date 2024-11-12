from fastapi import APIRouter
from model.pydantic_model import Todo
from all_routes import todo_create,todo_all,todo_delete,todo_one,todo_update
import operations.to_do as db



todo_route = APIRouter()

#create a new todo
@todo_route.post(todo_create)
def new_todo(doc: Todo):
    doc = dict(doc)
    todo:str = doc['todo']
    res = db.create_todo(todo)
    return res



@todo_route.get(todo_all)
def all_todos():
    res = db.get_all()
    return res

@todo_route.get(todo_one)
def one_todo(_id:int):
    res = db.get_one(_id)
    return res

@todo_route.put(todo_update)
def update(_id:int, doc:Todo):
    doc = dict(doc)
    title:str = doc['todo']
    res = db.update(_id,title)
    return res 

@todo_route.delete(todo_delete)
def delete(_id:int):
    res = db.delete(_id)
    return res
