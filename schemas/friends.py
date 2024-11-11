
from pydantic import BaseModel
from typing import Optional


class UserFriendshipBase(BaseModel):
    Status: str


class UserFriendshipCreate(UserFriendshipBase):
    FriendUserId: int


class UserFriendshipUpdate(BaseModel):
    Status: Optional[str] = None


class UserFriendshipInDB(UserFriendshipBase):
    UserId: int
    FriendUserId: int

    class Config:
        orm_mode = True


class UserFriendshipOut(UserFriendshipBase):
    UserId: int
    FriendUserId: int

    class Config:
        orm_mode = True
