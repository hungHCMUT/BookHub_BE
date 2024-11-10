# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date


class BookBase(BaseModel):
    Title: str
    Author: str
    PublicationDate: date
    Rating: float | None = None
    ReleaseDate: date


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    Title: Optional[str] = None
    Author: Optional[str] = None
    PublicationDate: Optional[date] = None
    Rating: Optional[float] = None
    ReleaseDate: Optional[date] = None


class BookInDB(BookBase):
    BookID: int
    class Config:
        orm_mode = True


class BookOut(BookBase):
    BookID: int

    class Config:
        orm_mode = True
