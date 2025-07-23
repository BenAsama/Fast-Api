from fastapi import FastAPI
from fastapi.params import Body

app=FastAPI()

@app.get("/")
def root():
    return {"message": "my api link !!!!!!!!!!!"}

@app.get("/post")
def get_posts():
    return {"data" : "this is ur post "}

@app.post("/create_post")
def create_post(payload: dict = Body(...)):
    return{"message": "creating post request"}