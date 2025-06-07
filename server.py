from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

# Remember it's CTRL+C to stop local host server
@app.route('/')
@app.route('/index')
def index():
    return "Testing Again"

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port = "8000")