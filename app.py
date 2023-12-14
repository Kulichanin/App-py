from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! It`s Python web app!</p>"

if __name__ == '__main__':
    app.run('0.0.0.0')