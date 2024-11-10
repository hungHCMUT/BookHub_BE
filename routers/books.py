from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from database import get_db
from schemas import books


router = APIRouter()


@router.post("/books/", response_model=books.BookInDB)
def create_book(book: books.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@router.get("/books/{book_id}", response_model=books.BookOut)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/books", response_model=list[books.BookOut])
def get_all_book(db: Session = Depends(get_db)):
    db_book = crud.get_book_list(db)
    if db_book == []:
        raise HTTPException(status_code=404, detail="List is empty")
    return db_book


@router.put("/books/{book_id}", response_model=books.BookUpdate)
def update_book_endpoint(book_id: int, book_update: books.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id=book_id, book_update=book_update)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}", status_code=204)
def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
