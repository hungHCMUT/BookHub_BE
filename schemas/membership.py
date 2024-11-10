from pydantic import BaseModel
from typing import Optional
from datetime import date


class MembershipBase(BaseModel):
    Type: str = "Silver"
    ExpiredDay: Optional[date] = None
    RemainingBooks: Optional[int] = 1


class MembershipCreate(MembershipBase):
    pass


class MembershipUpdate(BaseModel):
    Type: Optional[str] = None
    ExpiredDay: Optional[date] = None
    RemainingBooks: Optional[int] = None


class MembershipInDB(MembershipBase):
    UserID: int

    class Config:
        orm_mode = True


class MembershipOut(MembershipBase):
    UserID: int

    class Config:
        orm_mode = True
