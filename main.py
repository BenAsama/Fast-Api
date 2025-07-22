from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
# this is a comment line but i cant't
boy = app()