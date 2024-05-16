from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()


class post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: optional[int] = None
 


@app.get("/")
def root():
    return {"message": "welcome to my api"}

@app.get("/post")
def get_post():
    return {"data": "this is your post"}


@app.post("/createpost")
def create_post(new_post: post):
    print(new_post.published)
    print(new_post.rating)
    return {"data": "new post ok"}
# title : str, content: str, category, Bool published
