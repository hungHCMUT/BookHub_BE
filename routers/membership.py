from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
from schemas import membership

router = APIRouter()


@router.get("/membership/{user_id}", response_model=membership.MembershipOut)
def read_membership(user_id: int, db: Session = Depends(get_db)):
    db_membership = crud.get_membership_by_id(db, user_id=user_id)
    if db_membership is None:
        raise HTTPException(status_code=404, detail="Membership not found")
    return db_membership


@router.post("/membership/{user_id}", response_model=membership.MembershipInDB)
def create_membership(user_id: int, membership: membership.MembershipCreate, db: Session = Depends(get_db)):
    db_membership = crud.get_membership_by_id(db, user_id=user_id)
    if db_membership is None:
        return crud.create_membership(user_id, db, membership_create=membership)
    else:
        raise HTTPException(
            status_code=404, detail="Membership is already exist, please choose Update")


@router.get("/membership/", response_model=list[membership.MembershipOut])
def get_all_membership(db: Session = Depends(get_db)):
    db_membership = crud.get_membership_list(db)
    if db_membership == []:
        raise HTTPException(status_code=404, detail="List is empty")
    return db_membership


@router.put("/membership/{user_id}", response_model=membership.MembershipUpdate)
def update_membership_endpoint(user_id: int, membership_update: membership.MembershipUpdate, db: Session = Depends(get_db)):
    membership = crud.update_membership(
        db, user_id=user_id, membership_update=membership_update)
    if membership is None:
        raise HTTPException(status_code=404, detail="Membership not found")
    return membership


@router.delete("/membership/{user_id}", status_code=204)
def delete_membership_endpoint(user_id: int, db: Session = Depends(get_db)):
    membership = crud.delete_membership(db, user_id=user_id)
    if membership is None:
        raise HTTPException(status_code=404, detail="Membership not found")
    return {"message": "User deleted successfully"}
