from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

# set FLASK_APP=app.py (for windows)
# export FLASK_APP=app.py (for linux/mac)\

# flask run to get started (by default localhost 5000)