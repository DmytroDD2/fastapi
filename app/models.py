from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(Text())
    author_id = Column(Integer, ForeignKey('authors.id'))
    is_active = Column(Boolean, default=True)
    published_year = Column(Integer)
    price = Column(Integer, default=0)

    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)

    books = relationship("Book", back_populates="author")
