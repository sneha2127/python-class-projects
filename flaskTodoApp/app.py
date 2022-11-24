from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# create the extension
db = SQLAlchemy(app)


# Model Create
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)

# task = Task()
# print(task.task_name)

# class Dog:
#   no_of_legs = 4

# d1 = Dog
# d1.no_of_legs = 3


@app.route('/', methods=['GET',"POST"])
def index():
    if request.method == "POST":
        task_title = request.form["task"]
        task_obj = Task(task_name=task_title)
        db.session.add(task_obj)
        db.session.commit()


    # get a list of all objects of the Task table
    tasks = Task.query.all()
    len_of_tasks = len(tasks)
    return render_template('index.html', tasks=tasks, len_of_tasks=len_of_tasks)


# /delete/3

@app.route('/delete/<int:id>')
def delete_task(id):
    deleted_objs = Task.query.filter_by(id=id).all()
    delete_obj = deleted_objs[0]
    db.session.delete(delete_obj)
    db.session.commit()
    return redirect('/')


# Edit 

@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit_task(id):
    edited_objs = Task.query.filter_by(id=id).all()
    edited_obj = edited_objs[0]
    if request.method == "POST":
        new_task_title = request.form["task"]
        edited_obj.task_name = new_task_title
        db.session.add(edited_obj)
        db.session.commit()
        return redirect("/")
    return render_template("update.html", edit_task = edited_obj)


# Delete All

@app.route('/delete-all')
def delete_all_task():
    db.session.query(Task).delete()
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)