from flask import Flask
from datetime import datetime

books = {1: "Python book", 2: "Java book", 3: "Flask book"}
app = Flask(__name__)


@app.route("/hello")
@app.route("/")
def index():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello Flask6! {time} </h1>"


@app.route("/books")
def get_books():
    return books


@app.route("/books/<int:id>")
def book(id):
    try:
        return books[id]
    except Exception as e:
        print(e, "編號錯誤")
        return "書籍編號錯誤!"


@app.route("/sum/x=<x>&y=<y>")
def get_sum(x, y):
    return f"總合為:{eval(x)+eval(y)}"


app.run(debug=True)
