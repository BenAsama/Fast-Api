from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app=FastAPI()


class post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return {"message": "my api link !!!!!!!!!!!"}

@app.get("/post")
def get_posts():
    return {"data" : "this is ur post "}

@app.post("/create_post")
def create_post(new_post: post):
    print(new_post.title)
    return{}

@app.get("/something")
def something():
    pass