import sys
import os

# Ensure the current directory is in the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import schemas, database

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def get_root():
    return "Welcome to this Site!"


@app.post("/books")
#def create_book(request: schemas.BookAuthorPayload):
    #return "New book added!" + request.book.title + "  New author added " + request.author.first_name + "  " + request.author.last_name  
def create_book(request: schemas.BookAuthorPayload, db: Session = Depends(get_db)):
    # Create the author and book records
    new_author = database.Author(first_name=request.author.first_name, last_name=request.author.last_name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    new_book = database.Book(title=request.book.title)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    new_book_author = database.BookAuthor(author_id=new_author.author_id, book_id=new_book.book_id)
    db.add(new_book_author)
    db.commit()
    db.refresh(new_book_author)

    return {
        "message": "New book and author added!",
        "book": new_book,
        "author": new_author,
        "book_author": new_book_author
    }
#+ " " + str(request.book.number_of_pages) 

