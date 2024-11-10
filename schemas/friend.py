
from pydantic import BaseModel
from typing import Optional


class UserFriendshipBase(BaseModel):
    status: str


class UserFriendshipCreate(UserFriendshipBase):
    friend_user_id: int


class UserFriendshipUpdate(BaseModel):
    status: Optional[str] = None


class UserFriendshipInDB(UserFriendshipBase):
    user_id: int
    friend_user_id: int

    class Config:
        orm_mode = True


class UserFriendshipOut(UserFriendshipBase):
    user_id: int
    friend_user_id: int

    class Config:
        orm_mode = True
