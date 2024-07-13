
from pydantic import BaseModel
import database


class Book(BaseModel):
    
    title : str
    #number_of_pages: int


class Author(BaseModel):
    first_name: str
    last_name: str
    
class BookAuthorPayload(BaseModel):
    book: Book
    author: Author
    