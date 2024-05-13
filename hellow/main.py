from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True



@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/post")
def get_post():
    return {"data": "this is your post"}


@app.post("/createpost")
def create_post(new_post: post):
    print(new_post)
    return {"data": "new post"}
# title : str, content: str, category, Bool published