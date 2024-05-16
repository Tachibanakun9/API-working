from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: optional[int] = None
 
my_post = [{"title": "title of the post 1", "content": "content of the post 1", "id": 1}, {"title": "hi everyone", "content": "i like to play games", "id": 2}]
#remember wherever we open and run our server this data will be removed so for this we are 
#going to hard core it

@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/post")
def get_post():
    return {"data": my_post}


@app.post("/post")
def create_post(post: Post):
    print(post.published)
    print(post.rating)
    # if ever you need to convert a schema to a python dictionary 
    print(post.dict())
    return {"data": "new post ok", post}
# title : str, content: str, category, Bool published
