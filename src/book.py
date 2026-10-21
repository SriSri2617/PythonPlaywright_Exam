from dataclasses import dataclass


@dataclass
class Book:
    author: str
    title: str
    book_id: int
    favorite: bool
