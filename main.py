from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published:bool =True
    rating:Optional[int] =None

my_posts=[{"title":"title of post1","content":"content of post 1","id":1},{
          "title":"favorite foods","content":"I like pizza","id":2}]

@app.get("/login")
async def get_user():
    return {"message": "Welcome To My API"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/createPosts")
def create_posts(new_post:Post):
    print(new_post)
    return {"Data":new_post}

@app.post("/posts")
def create_posts(new_post:Post):
    new_post =new_post.dict()
    new_post['id'] = randrange(0,10000000)
    my_posts.append(new_post)
    return {"Data":my_posts}

@app.get("/posts/{id}")
def get_post(id:int):
    print(id)
    post=find_post(id)
    return {"post details":post}

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p




