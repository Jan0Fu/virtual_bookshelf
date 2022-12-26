from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = StringField("Book Rating", validators=[DataRequired()])


app = Flask(__name__)


all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        new_book = {
            "book_title": request.form["title"],
            "book_author": request.form["author"],
            "book_rating": request.form["rating"]
        }
        all_books.append(new_book)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

