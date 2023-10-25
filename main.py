from fastapi import FastAPI
from fastapi import status

from database.database import engine
from database import models

from routers.blogs import blog_router
from routers.users import user_router
from routers.authentication import authentication_router
 
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blog_router, prefix="/blogs", tags=["Blogs"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(authentication_router, prefix="/login", tags=["Authentication"])

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"Welcome to my Blog API"}


@app.get("/about", status_code=status.HTTP_200_OK)
def about():
    return {"This is an API created by Kevin"}


@app.get("/contact", status_code=status.HTTP_200_OK)
def contact():
    return {"Contact": "otisria1@gmail.com"}




