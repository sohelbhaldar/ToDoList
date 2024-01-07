# Route to display tasks
# @app.route('/books')
# @cross_origin()
# #A decorator begins with @ and is a unique feature of the Python language. It modifies the function that follows it
# def getAllBooks():
#     breakpoint()
#     if(books == {}):
        
#         response = make_response("<h1>Oops No Books found..!</h1>", 404)
#         return response
#     else:
#         response = make_response(books, 200)
#         return response
    #return render_template('index.html', tasks=tasks) 
    ##render_template selects the template file to be used and passes to it any values or variables it needs

# Route to add a new book
# @app.route('/addBooks', methods=['POST'])
# @cross_origin()
# def addBooks():
    
#     content_type = request.headers.get('Content-Type')
#     if(content_type == 'application/json'):
#         newBook = request.json
   
#     if(newBook == {}):
#         response = make_response("Please provide atleast one book ", 400)
#         return response
#     else:
#         books.append(newBook)
        
#     return make_response(books, 201)
    #return redirect(url_for('index'))

# Route to delete a book
# @app.route('/delete/<int:BookId>')
# @cross_origin()
# def delete(BookId):
#     if BookId < len(books):

#         del books[BookId]
#         response = make_response("Please provide atleast one book ", 500)
#         return response
    
    #return redirect(url_for('index'))