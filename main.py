from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, MappedColumn
from sqlalchemy import Integer,String


class BaseModel(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(model_class=BaseModel)
db.init_app(app)



class Task(db.Model):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, default="pending", nullable=False)

with app.app_context():
    db.session.commit()

@app.route('/')
def home():
    tasks = db.session.query(Task).all()
    return render_template("index.html",tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task_text = request.form.get("task")

    if task_text:
        new_task = Task(task=task_text, status = "pending")
        db.session.add(new_task)
        db.session.commit()

    return redirect(url_for("home"))

@app.route('/done/<int:id>')
def done(id):
    task = db.session.query(Task).get(id)
    task.status = "done"
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete/<int:id>')
def delete(id):
    task = db.session.query(Task).get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)