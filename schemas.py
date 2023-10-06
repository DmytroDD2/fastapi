from pydantic import BaseModel


from typing import List


class Employee(BaseModel):
    first_name: str
    last_name: str
    date_joined: str
    age: int
    city: str
    library_id: int
    is_active: bool = False
    salary: int








class AnotherModel(BaseModel):
    some_field: str
    some_field2: int


class Book(BaseModel):
    id: int
    title: str
    description: str | None = None
    author: str
    published_year: int
    # Another: AnotherModel


class BookWithPrice(Book):
    price: int


