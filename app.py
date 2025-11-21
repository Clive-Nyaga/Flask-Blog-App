from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=True, default='Unknown Author')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        # return f"Blog Post('{self.title}', '{self.author}')"
        return 'Blog Post ' + str(self.id)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1.',
        'author': 'John Doe'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2.'
    }
]

@app.route('/')
def index():
    return "<h1>Home Page 1</h1>"

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/hello')
def hello_world():
    return render_template('index.html')

@app.route('/home/users/<string:username>/posts/<int:id>')
def home(username, id):
    return 'Welcome to the home page ' + username + '!' + ' Your ID is ' + str(id) + '.'

@app.route('/get', methods=['GET'])
def get_route():
    return 'This is a GET route. 200 OK!'

if __name__ == '__main__':
    app.run(debug=True)

