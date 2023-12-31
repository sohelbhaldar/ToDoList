from flask import Flask, render_template, request, redirect, url_for, make_response, Blueprint
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_migrate import Migrate 
import json
from flask_restx import Resource, fields
from flask_restx import Api, Namespace, Resource

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications

ns = Namespace('Books', description='Book Namespace')

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Book(db.Model):
    myBooks = []
    __tablename__ = 'books'

    BookId = db.Column(db.Integer, primary_key=True)
    PageNum = db.Column(db.Integer)
    BookName = db.Column(db.String(100))
    Author = db.Column(db.String(100))


allBooks = []
json_numbers = any
api = Api(app)
# Add the namespace to the API
api.add_namespace(ns)
model = api.model('Book', {
    'BookId': fields.Integer,
    'PageNum': fields.Integer,
    'BookName': fields.String,
    'Author': fields.String,
})

@ns.route('/')
class Book(Resource):
    @api.marshal_with(model, envelope='data')
    def get(self, **kwargs):
        return Book.query.all()  # Some function that queries the db
    
    @api.expect(model)
    @api.marshal_with(model, envelope='data')
    def post(self):
        newBook = api.payload
        book = Book(BookId=newBook["BookId"], PageNum=newBook["PageNum"], BookName=newBook["BookName"], Author=newBook["Author"])
        db.session.add(book)
        db.session.commit()
        return book
    
    @api.expect(model)
    @api.marshal_with(model, envelope='data')
    def asa(self):
        newBook = api.payload
        book = Book(BookId=newBook["BookId"], PageNum=newBook["PageNum"], BookName=newBook["BookName"], Author=newBook["Author"])
        db.session.add(book)
        db.session.commit()
        return book
        # content_type = request.headers.get('Content-Type')
        # if(content_type == 'application/json'):
        #     newBook = request.json
    
        # if(newBook == {}):
        #     response = make_response("Please provide atleast one book ", 400)
        #     return response
        # else:
            
        #     if(newBook.get('BookId') is None or newBook["BookId"] == "" or newBook.get('PageNum') is None or newBook["PageNum"] == "" or newBook.get('BookName') is None or newBook["BookName"] == "" or newBook.get('Author') is None or newBook["Author"] == ""):
        #             response = make_response("Please provide correct information to add a book ", 400)
        #             return response
        #     try:

        #     except Exception as e:
        #         response = make_response(str(e), 400)
        #         return response
        
        # return book
    
# Route to display tasks
#@api.route('/books')
@cross_origin()
#A decorator begins with @ and is a unique feature of the Python language. It modifies the function that follows it
#@api.marshal_with(model, envelope='resource')
def getAllBooks():
    
    return Book.query.all()

    if(books == {}):        
        response = make_response("<h1>Oops No Books found..!</h1>", 404)
        return response
    
    for book in books:
        myBooks1 = {}
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)

    return make_response(allBooks,200)


# Route to add a new book
@app.route('/addBooks', methods=['POST'])
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
        myBooks1 = {}
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)     
        
    return make_response(allBooks,200)
    #return redirect(url_for('index'))
# Route to delete a book
@app.route('/book/<int:BookId>', methods=['GET'])
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
@app.route('/delete/<int:BookId>', methods=['DELETE'])
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
        myBooks1 = {}
        myBooks1["BookId"] = book.BookId
        myBooks1["PageNum"] = book.PageNum
        myBooks1["BookName"] = book.BookName
        myBooks1["Author"] = book.Author
        allBooks.append(myBooks1)     
        
    return make_response(allBooks,200)

# Route to add a new book
@app.route('/book', methods=['PUT'])
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
            myBooks1 = {}
            myBooks1["BookId"] = mybook.BookId
            myBooks1["PageNum"] = mybook.PageNum
            myBooks1["BookName"] = mybook.BookName
            myBooks1["Author"] = mybook.Author
        else:
            response = make_response("No Book Found ", 400)
            return response

        return make_response(myBooks1,200)
    except Exception as e:
        response = make_response(str(e), 400)
        return response   
         
    #return redirect(url_for('index')      
if __name__ == '__main__':  #__main__ is the name of the environment where top-level code is run. Sometimes “top-level code” is called an entry point to the application.
    app.run(debug=True)
