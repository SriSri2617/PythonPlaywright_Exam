from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    book_id: int
    favorite: bool
