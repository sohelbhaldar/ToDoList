from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'

    BookId = db.Column(db.Integer, primary_key=True)
    PageNum = db.Column(db.Integer)
    BookName = db.Column(db.String(100))
    Author = db.Column(db.String(100))
