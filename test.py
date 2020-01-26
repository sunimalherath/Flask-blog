from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "John Doe",
        "title": "Back to basics - Python",
        "content": "Back to basics serious for Python 3",
        "date_posted": "26/01/2020"
    },
    {
        "author": "Jane Doe",
        "title": "Head First - Python",
        "content": "Lessons from Head First - Python book",
        "date_posted": "27/01/2020"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

