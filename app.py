from flask import Flask, render_template

app = Flask(__name__)

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

