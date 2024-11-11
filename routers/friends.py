from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
from schemas import friends

router = APIRouter()


@router.get("/friends/{user_id}", response_model=friends.UserFriendshipOut)
def read_friend(user_id: int, db: Session = Depends(get_db)):
    db_friend = crud.get_friend_by_id(db, user_id=user_id)
    if db_friend is None:
        raise HTTPException(status_code=404, detail="Friend not found")
    return db_friend


@router.post("/friends/{user_id}", response_model=friends.UserFriendshipInDB)
def create_membership(user_id: int, friend: friends.UserFriendshipCreate, db: Session = Depends(get_db)):
    return crud.create_friend(db, friend=friend, user_id=user_id)


@router.get("/friends/", response_model=list[friends.UserFriendshipOut])
def get_all_friend(db: Session = Depends(get_db)):
    db_friend = crud.get_membership_list(db)
    if db_friend == []:
        raise HTTPException(status_code=404, detail="List is empty")
    return db_friend


@router.put("/friends/{user_id}", response_model=friends.UserFriendshipUpdate)
def update_friend_endpoint(user_id: int, friend_update: friends.UserFriendshipUpdate, db: Session = Depends(get_db)):
    friend = crud.update_membership(
        db, user_id=user_id, friend_update=friend_update)
    if friend is None:
        raise HTTPException(status_code=404, detail="Membership not found")
    return friend


@router.delete("/friend/{user_id}", status_code=204)
def delete_friend_endpoint(user_id: int, db: Session = Depends(get_db)):
    friend = crud.delete_friend(db, user_id=user_id)
    if friend is None:
        raise HTTPException(status_code=404, detail="Membership not found")
    return {"message": "User deleted successfully"}
