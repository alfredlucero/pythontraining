from database_setup import Base, Book
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from flask import Flask, request
app = Flask(__name__)


# Connect to database and create database session
engine = create_engine('sqlite:///books-collection.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Read
@app.route("/")
@app.route("/books")
def readBooks():
    books = session.query(Book).all()
    return books

# Create
@app.route("/books", methods=["POST"])
def createBook():
    newBook = Book(
        title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
    session.add(newBook)
    session.commit()
    return newBook

# Update
@app.route("/books/<int:book_id>", methods=["PATCH"])
def updateBook(book_id):
    editedBook = session.query(Book).filter_by(id=book_id).one()
    editedBook.name = request.form['name']
    editedBook.title = request.form['title']
    editedBook.genre = request.form['genre']
    session.add(editedBook)
    session.commit()
    return editedBook

# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    session.delete(bookToDelete)
    session.commit()
    return bookToDelete


if __name__ == '__main__':
    app.debug = True
    app.run()
