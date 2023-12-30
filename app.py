from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 
#Flask(__name__), is a new object that inherits from the class Flask — meaning it gets all the attributes and methods built into that class
# Python has many double-underscore entities, and they always have this pattern: 
    #two underscores, a word, and two underscores. These double-underscore entities are referred to with the slang dunder

# Initialize an empty list to store tasks
tasks = []

# Route to display tasks
@app.route('/')
#A decorator begins with @ and is a unique feature of the Python language. It modifies the function that follows it
def index():
    return render_template('index.html', tasks=tasks) #render_template selects the template file to be used and passes to it any values or variables it needs

# Route to add a new task
@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
