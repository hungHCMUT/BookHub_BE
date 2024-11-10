from pydantic import BaseModel, EmailStr


# Shared Properties
class UserBase(BaseModel):
    Email: EmailStr
    Username: str
    Streak: int | None = 0


class UserCreate(UserBase):
    Password: str


class UserUpdate(UserBase):
    Email: EmailStr | None = None
    Username: str | None = None
    Password: str | None = None


class UserInDB(UserBase):
    UserID: int
    Password: str

    class Config:
        orm_mode = True


class UserOut(UserBase):
    UserID: int

    class Config:
        orm_mode = True
