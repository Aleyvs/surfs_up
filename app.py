from flask import Flask

## create a new flask app instance ** always the same **
app = Flask(__name__)

## define the starting point (root)
@app.route('/')
def hello_world():
    return 'Hello World'