from fastapi import FastApi
from pydantic import BaseModel
from fastapi.params import Body

app = FastApi()


class post(BaseModel):
    title: str
    content: str



@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/post")
def get_post():
    return {"data": "this is your post"}


@app.post("/post")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title" {payload['title'] content: {payload['content']}}}
# title : str, content: str, category, Bool published