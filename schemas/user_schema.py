from pydantic import BaseModel

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str

class BlogBase(BaseModel):
    title: str
    content: str

class ShowUser(BaseModel):
    username: str
    email: str
    blogs: list[BlogBase]
    class Config:
        orm_mode = True

    