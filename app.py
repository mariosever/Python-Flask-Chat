from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    text = db.Column(db.String)

db.create_all()


@app.route("/", methods=["GET"])
def index():

    message = Message.query.all()

    return render_template("index.html", message=message)


@app.route("/add-message", methods=["POST"])
def add_message():

    username = request.form.get("username")
    text = request.form.get("text")

    message = Message(username=username, text=text)

    db.session.add(message)
    db.session.commit()


    return redirect("/")
    

@app.route("/delete/<msg_id>", methods=["GET"])
def delete_message(msg_id):

    message = Message.query.get(int(msg_id))

    db.session.delete(message)
    db.session.commit()

    return redirect("/")



if __name__ == "__main__":
    app.run()