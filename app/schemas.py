from pydantic import BaseModel


class BaseBook(BaseModel):
    title: str
    description: str | None = None
    published_year: int
    price: int
    author_id: int


class CreateBook(BaseBook):
    pass


class UpdateBook(BaseBook):
    pass


class Book(BaseBook):
    id: int

    class Config:
        orm_mode = True


class BaseAuthor(BaseModel):
    first_name: str
    last_name: str


class CreateAuthor(BaseAuthor):
    pass


class UpdateAuthor(BaseAuthor):
    pass

class Author(BaseAuthor):
    id: int

    class Config:
        orm_mode = True

