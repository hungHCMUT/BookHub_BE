from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
from schemas import users

router = APIRouter()


@router.post("/users/", response_model=users.UserInDB)
def create_user(user: users.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=users.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users", response_model=list[users.UserOut])
def get_all_user(db: Session = Depends(get_db)):
    db_user = crud.get_user_list(db)
    if db_user == []:
        raise HTTPException(status_code=404, detail="List is empty")
    return db_user


@router.put("/users/{user_id}", response_model=users.UserUpdate)
def update_user_endpoint(user_id: int, user_update: users.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, user_id=user_id, user_update=user_update)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
