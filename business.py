from flask import Blueprint, render_template, request, redirect, url_for, make_response
from models import db, Book
from flask_cors import cross_origin

book_routes = Blueprint('book_routes', __name__)

myBooks1 = {}
allBooks = []
json_numbers = any
book_routes.route('/books')
@cross_origin()
#A decorator begins with @ and is a unique feature of the Python language. It modifies the function that follows it
def getAllBooks():

    books = Book.query.all()

    for book in books:
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)

    if(books == {}):        
        response = make_response("<h1>Oops No Books found..!</h1>", 404)
        return response
    else:
        return make_response(allBooks,200)


# Route to add a new book
book_routes.route('/addBooks', methods=['POST'])
@cross_origin()
def addBooks():
    
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        newBook = request.json
   
    if(newBook == {}):
        response = make_response("Please provide atleast one book ", 400)
        return response
    else:
        
        if(newBook.get('BookId') is None or newBook["BookId"] == "" or newBook.get('PageNum') is None or newBook["PageNum"] == "" or newBook.get('BookName') is None or newBook["BookName"] == "" or newBook.get('Author') is None or newBook["Author"] == ""):
                response = make_response("Please provide correct information to add a book ", 400)
                return response
        try:
            book = Book(BookId=newBook["BookId"], PageNum=newBook["PageNum"], BookName=newBook["BookName"], Author=newBook["Author"])
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            response = make_response(str(e), 400)
            return response
    
    books = Book.query.all()

    for book in books:
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)     
        
    return make_response(allBooks,200)
    #return redirect(url_for('index'))
# Route to delete a book
book_routes.route('/book/<int:BookId>', methods=['GET'])
@cross_origin()
def getBookById(BookId):

    try:
        book = {}
        mybook = db.session.get(Book,BookId)
        if(mybook is not None):
            book["BookId"] = mybook.BookId
            book["PageNum"] = mybook.PageNum
            book["BookName"] = mybook.BookName
            book["Author"] = mybook.Author
        else:
            response = make_response("No Book Found ", 400)
            return response

        return make_response(book,200)
    except Exception as e:
        response = make_response(str(e), 400)
        return response

# Route to delete a book
book_routes.route('/delete/<int:BookId>', methods=['DELETE'])
@cross_origin()
def delete(BookId):

    try:
        mybook = db.session.get(Book,BookId)
        db.session.delete(mybook)
        db.session.commit()
    except Exception as e:
        response = make_response(str(e), 400)
        return response
    
    books = Book.query.all()

    for book in books:
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)     
        
    return make_response(allBooks,200)

# Route to add a new book
book_routes.route('/book', methods=['PUT'])
@cross_origin()
def upsertBook():
    
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        newBook = request.json
   
    if(newBook == {}):
        response = make_response("Please provide atleast one book ", 400)
        return response
    else:
        
        if(newBook.get('BookId') is None or newBook["BookId"] == "" or newBook.get('PageNum') is None or newBook["PageNum"] == "" or newBook.get('BookName') is None or newBook["BookName"] == "" or newBook.get('Author') is None or newBook["Author"] == ""):
                response = make_response("Please provide correct information to add a book ", 400)
                return response
        try:
            book = Book(BookId=newBook["BookId"], PageNum=newBook["PageNum"], BookName=newBook["BookName"], Author=newBook["Author"])
            db.session.merge(book)
            db.session.commit()
        except Exception as e:
            response = make_response(str(e), 400)
            return response
    
    try:
        book = {}
        mybook = db.session.get(Book,newBook["BookId"])
        if(mybook is not None):
            book["BookId"] = mybook.BookId
            book["PageNum"] = mybook.PageNum
            book["BookName"] = mybook.BookName
            book["Author"] = mybook.Author
        else:
            response = make_response("No Book Found ", 400)
            return response

        return make_response(book,200)
    except Exception as e:
        response = make_response(str(e), 400)
        return response   