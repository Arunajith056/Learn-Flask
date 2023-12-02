from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '61012e37d8a77f577c8f2053cb8b5072'

posts = [
    {
        'author': 'chorey',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_created': '27-05-2015'
    },
    {
        'author': 'sam',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_created': '27-05-2017'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)
