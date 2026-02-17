from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def hello():
    # return "Hello"
    return "<h1>Hello</h1>"

@app.route('/about')
def about():
    return "<h1>About</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# =====================================================
# m1 - Using Environment Variables (Flask CLI method)
# =====================================================

# Windows (CMD)
# set FLASK_APP=app.py
# set FLASK_DEBUG=1
# set FLASK_RUN_PORT=5001
# flask run

# Windows (PowerShell)
# $env:FLASK_APP="app.py"
# $env:FLASK_DEBUG="1"
# $env:FLASK_RUN_PORT="5001"
# flask run

# Linux / macOS
# export FLASK_APP=app.py
# export FLASK_DEBUG=1
# export FLASK_RUN_PORT=5001
# flask run

# =====================================================
# m2 - Using Flask CLI directly (Recommended modern way)
# =====================================================

# flask --app app.py run
# flask --app app.py run --debug
# flask --app app.py run --port 5001
# flask --app app.py run --host 0.0.0.0

# =====================================================
# m3 - Running Python file directly (Traditional way)
# =====================================================

# if __name__ == '__main__':
#     app.run()

# if __name__ == '__main__':
#     app.run(debug=True)

# if __name__ == '__main__':
#     app.run(port=5001)