from pydantic import BaseModel
from datetime import datetime
# from schemas.user_schema import ShowUser

class BlogBase(BaseModel):
    title: str
    content: str

class CreateBlog(BlogBase):
    publisher_id: int
    pass 

class UpdateBlog(BlogBase):
    pass

class ShowCreatedBlog(BlogBase):
    created: datetime


class ShowAuthor(BaseModel):
    username: str
    email: str
    
class ShowBlog(BlogBase):
    created: datetime
    author: ShowAuthor

    class Config:
        orm_mode = True