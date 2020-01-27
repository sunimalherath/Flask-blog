from flask import Flask, render_template, url_for
from forms import RegistraionForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'd2ce6f77363d58f974669fd1db2b46c5'

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


@app.route("/register")
def register():
    form = RegistraionForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)

