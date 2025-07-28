from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]= None

my_posts=[{"title":"this is the first post","content":"this is the content of the first post","id":1},
          {"title":"fave food","content":"pizza , hotdog and meat","id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        return i
@app.get("/")
def root():
    return {"message": "my api link !!!!!!!!!!!"}

@app.get("/post")
def get_posts():
    return {"data" : my_posts}

@app.post("/create_post", status_code=status.HTTP_201_CREATED)
def create_post(post: post):
    post_dict= post.dict()
    post_dict["id"]=randrange(0, 10000000000)
    my_posts.append(post_dict)
    return{"data": post_dict}

@app.get("/post/{id}")
def get_post(id: int):
    post = find_post(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} was not found")
    return{"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id):

    index = find_index_post(id)
    if index == None:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id"))
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_posts(id: int,post: post):

    index = find_index_post(id)
    if index == None:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id"))
    post_dict['id']=id
    my_posts[index]=post_dict

    return {'post':'post_dict'}