from fastapi import APIRouter, Depends, HTTPException, status
from database.models import Blog, User
from services.oaut2 import get_current_user


from schemas.blog_schema import CreateBlog, UpdateBlog, ShowBlog, ShowCreatedBlog

from sqlalchemy.orm import Session

from services.db_service import get_db

blog_router = APIRouter()


@blog_router.get("/", status_code=200, response_model=list[ShowBlog])
def show_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs



@blog_router.get("/{id}", status_code=200, response_model=ShowBlog)
def show_a_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id of {id} is not avilable")
    return blog



@blog_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowCreatedBlog)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db), current_user: User 
                  = Depends(get_current_user)):
    new_blog = Blog(title=blog.title, content=blog.content, publisher_id=blog.publisher_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@blog_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_a_blog(id: int, request: UpdateBlog, db: Session = Depends(get_db), current_user: User 
                  = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id of {id} is not avilable")
    
    blog.update(request.dict())
    db.commit()
    return {"detail": f"Blog with the id of {id} has been updated successfully"}



@blog_router.delete("/{id}", status_code=200)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Blog with the id of {id} is not avilable")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with the id of {id} has been deleted"}



