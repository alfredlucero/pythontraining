from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Book, Base

engine = create_engine('sqlite:///books-collection.db')

# Bind the engine to the metadata of the Base class so that the declaratives can be accessed
# through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instances establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the database session object
session = DBSession()

# Create
# entryName = ClassName(property="value", ...)
# To persist our ClassName object, we add() it to our Session:
# session.add(entryName)
# To issue the changes to our database and commit the transaction we use commit()
# Any change made against the objects in the session won't be persisted into the database until you
# call session.commit()
# session.commit()
bookOne = Book(title="The Road less traveled",
               author="Some Writer", genre="life")
session.add(bookOne)
session.commit()

# Read
# session.query(Book).all() -> list of all books
# session.query(Book).first() => first result or 'None" if result doesn't contain a row

# Update
# Find the entry (filter_by())
# Reset the values
# Add the new entry
# Commit the session to our database
# all() - returns results as a list, one() gives one result or exception, first() returns first result or 'None'
editedBook = session.query(Book).filter_by(id=1).one()
editedBook.author = "Edit Writer"
session.add(editedBook)
session.commit()

# Delete
# Find the entry
# Delete the entry
# Commit the session
# bookToDelete = session.query(Book).filter_by(name="blah").one()
# session.delete(bookToDelete)
# session.commit()
