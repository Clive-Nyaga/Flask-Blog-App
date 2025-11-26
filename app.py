from flask import Flask, render_template, request, redirect
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

@app.route('/')
def index():
    return "<h1>Home Page 1</h1>"

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()

        return redirect('/posts')
    # all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
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

