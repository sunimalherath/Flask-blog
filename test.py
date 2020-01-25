from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<H1>Home Page</H1>"


if __name__ == '__main__':
    app.run(debug=True)

