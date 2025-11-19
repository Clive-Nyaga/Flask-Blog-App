from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home/users/<string:username>/posts/<int:id>')
def home(username, id):
    return 'Welcome to the home page ' + username + '!' + ' Your ID is ' + str(id) + '.'

@app.route('/get', methods=['GET'])
def get_route():
    return 'This is a GET route. 200 OK!'

if __name__ == '__main__':
    app.run(debug=True)

