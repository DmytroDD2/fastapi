from fastapi import HTTPException
from sqlalchemy.orm import Session

from .models import Book, Author
from .schemas import CreateBook, CreateAuthor


def book_list(db: Session):
    return db.query(Book).all()


def book_create(db: Session, book: CreateBook):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def book_delete(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return None


def book_update(db: Session, book_id: int, updated_book_data):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Книга не знайдена")

    updated_data = updated_book_data.dict(exclude_unset=True)
    db.query(Book).filter(Book.id == book_id).update(updated_data)
    db.commit()
    db.refresh(book)


def book_retrieve(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def authors_list(db: Session):
    return db.query(Author).all()


def author_create(db: Session, author: CreateAuthor):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def author_retrieve(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()


def author_update(db: Session, author_id: int, updated_uthor_data):
    author = db.query(Book).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author is not found")

    updated_data = updated_uthor_data.dict(exclude_unset=True)
    db.query(Book).filter(Author.id == author_id).update(updated_data)
    db.commit()
    db.refresh(author)


def author_delete(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        db.delete(author)
        db.commit()
        return author
    return None
