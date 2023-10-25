from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from database.models import User
from services.passwords import verify_password

from services.token import create_access_token

from sqlalchemy.orm import Session

from services.db_service import get_db


authentication_router = APIRouter()

@authentication_router.post("/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User does not exist")

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Incorrect password")
    
    # user_dict = {
    #     "username": user.username
    # }
    
    access_token = create_access_token(
        {"sub": user.username}
    
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
