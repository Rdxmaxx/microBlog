from flask import render_template
from app import app

@app.get('/')
@app.get('/index')
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
