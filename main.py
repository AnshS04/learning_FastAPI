from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog')
def index(limit: int=10, published: bool=True, sort: Optional[str]=None):
    if(published):
        return {'data': f'{limit} published articles from the db'}
    else:
        return {'data': f'{limit} unpublished articles from the db'}

@app.get('/blog/{id}')
def about(id: int):
    #fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit: int = 10):
    # fastapi is smart enough to know the diff between a path parameter and a query parameter
    # fetch comments of blogs with id = id
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
     return {'data': f"Blog is created with title as {blog.title}"}