from flask import render_template, flash, redirect, url_for
from .forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'John Doe'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Today is a beautiful day !'
        },
        {
            'author': {'usename': 'Void'},
            'body': 'I like Ice-cream'
        }
    ]
    return render_template('index.html', title='Homepage', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)