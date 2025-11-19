from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Home Page 1</h1>"

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

