from enum import Enum
from typing import Annotated, Any
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Body, Path, Query, Cookie, Header, Response, status
from fastapi.responses import JSONResponse
from schemas import Book, AnotherModel, BookWithPrice, Employee



class RandomEnum(Enum):
    one = "one"
    two = "two"


app = FastAPI()

books_data = [
    {
        "id": 1,
        "title": "Python the best!",
        "description": "Python is the best programming language in the world",
        "author": "Vladyslav Ushakov",
        "price": 1000,
        "published_year": 2023
    },
    {
        "id": 2,
        "title": "Learning Python",
        "description": "A comprehensive guide to learning Python programming",
        "author": "Jane Smith",
        "price": 750,
        "published_year": 2022
    },
    {
        "id": 3,
        "title": "Python for Data Science",
        "description": "Exploring data analysis and machine learning with Python",
        "author": "John Doe",
        "price": 850,
        "published_year": 2021
    },
    {
        "id": 4,
        "title": "Python Web Development",
        "description": "Building web applications using Python and popular frameworks",
        "author": "Emily Johnson",
        "price": 1200,
        "published_year": 2020
    }
]


@app.get("/books/")
async def get_book_list(q: Annotated[str | None, Query()] = None, content_type: Annotated[str | None, Header()] = None):
    return {"books": books_data, "q": q, "content_type": content_type}


@app.get("/books/{book_id}")
async def get_book(book_id: Annotated[int, Path(title='ID for book in my store', ge=1)], q: str):
    book = list(filter(lambda x: x['id'] == book_id, books_data))[0]
    book['q'] = q
    return book


@app.post('/book/{book_id}', response_model=Book, status_code=201)
async def create_book(book: BookWithPrice) -> Any:
    return book




employees_data = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "date_joined": "2023-01-01",
        "age": 30,
        "city": 1,
        "library_id": 101,
        "is_active": True,
        "salary": 50000
    },
    {

        "id": 1,
        "first_name": "Jane",
        "last_name": "Smith",
        "date_joined": "2022-12-15",
        "age": 28,
        "city": 2,
        "library_id": 102,
        "is_active": True,
        "salary": 55000
    },
    {
        "id": 1,
        "first_name": "Bob",
        "last_name": "Johnson",
        "date_joined": "2022-11-20",
        "age": 35,
        "city": 1,
        "library_id": 103,
        "is_active": False,
        "salary": 48000
    },
    {

        "id": 1,
        "first_name": "Alice",
        "last_name": "Brown",
        "date_joined": "2023-02-10",
        "age": 26,
        "city": 3,
        "library_id": 104,
        "is_active": True,
        "salary": 52000
    },
]


@app.get("/employees/")
async def get_employees_list(first_name: str, last_name: str, age: int):
    employee = list(filter(lambda x:
                           x['first_name'] == first_name and
                           x['last_name'] == last_name and
                           x['age'] == age,
                           employees_data))
    print(employee)
    return {"employees": employee}


@app.get("/employees/{employee_id}")
async def get_employee(employee_id: Annotated[int, Path(title='ID for book in my store', ge=1)]):
    employee = list(filter(lambda x: x['id'] == employee_id, employees_data))[0]
    return employee


@app.put("/employees/{employee_id}", status_code=204)
async def update_employee(employee_id: int, employee: Employee):
    employeer = list(filter(lambda x: x['id'] == employee_id, employees_data))[0]
    update_employee_encoded = jsonable_encoder(employee)
    employees_data[employees_data.index(employeer)] = update_employee_encoded
    return update_employee_encoded


@app.post('/employee/{employee_id}', response_model=Employee, status_code=201)
async def add_employee(employee: Employee) -> Any:
    return employee














































# class RandomEnum(Enum):
#     one = "one"
#     two = "two"
#
#
# app = FastAPI()
#
# books_data = [
#     {
#         "id": 1,
#         "title": "Python the best!",
#         "description": "Python is the best programming language in the world",
#         "author": "Vladyslav Ushakov",
#         "price": 1000,
#         "published_year": 2023
#     },
#     {
#         "id": 2,
#         "title": "Learning Python",
#         "description": "A comprehensive guide to learning Python programming",
#         "author": "Jane Smith",
#         "price": 750,
#         "published_year": 2022
#     },
#     {
#         "id": 3,
#         "title": "Python for Data Science",
#         "description": "Exploring data analysis and machine learning with Python",
#         "author": "John Doe",
#         "price": 850,
#         "published_year": 2021
#     },
#     {
#         "id": 4,
#         "title": "Python Web Development",
#         "description": "Building web applications using Python and popular frameworks",
#         "author": "Emily Johnson",
#         "price": 1200,
#         "published_year": 2020
#     }
# ]
#
#
# @app.get("/books/")
# async def get_book_list(q: Annotated[str | None, Query()] = None, content_type: Annotated[str | None, Header()] = None):
# # async def get_book_list(q: Annotated[list[str] | None, Query(min_length=5, max_length=10, pattern=r'^A\d{1,3}\w{1,3}d$')] = None, is_active: bool = False):
#     # if price is not None:
#     #     books = list(filter(lambda x: x['price'] > price, books_data))
#     #     return {"books": books, "is_active": is_active}
#     # return {"books": books_data, "is_active": is_active, "q": q}
#     return {"books": books_data, "q": q, "content_type": content_type}
#
#
# @app.get("/books/{book_id}")
# async def get_book(book_id: Annotated[int, Path(title='ID for book in my store', ge=1)], q: str):
#     book = list(filter(lambda x: x['id'] == book_id, books_data))[0]
#     book['q'] = q
#     return book
#
#
# @app.post('/book/{book_id}', response_model=Book, status_code=201)
# async def create_book(book: BookWithPrice) -> Any:
#     return book
#
#
#
# # @app.post('/book/{book_id}')
# # async def create_book(book_id: Annotated[int, Path()], book: Book, q: str | None = None):
# # # async def create_book(book_id: Annotated[int, Path()], book: Book, another: AnotherModel, other: Annotated[str, Body()], q: str | None = None):
# #     print(book.title)
# #     print(book.model_dump())
# #     return {'success': True}
