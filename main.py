from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app=FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]= None


@app.get("/")
def root():
    return {"message": "my api link !!!!!!!!!!!"}

@app.get("/post")
def get_posts():
    return {"data" : "this is ur post "}

@app.post("/create_post")
def create_post(post: post):
    print (post)
    print(post.dict())
    return{"data": post}