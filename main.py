from fastapi import FastAPI
from routes.route_todo import todo_route


app = FastAPI()
app.include_router(todo_route)