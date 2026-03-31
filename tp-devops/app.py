from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevOps Version 2 BUGGEE"