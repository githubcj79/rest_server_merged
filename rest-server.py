from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# CHROME: http://127.0.0.1:5000/people
# GET /people -> devuelve la lista completa de las personas existentes
@app.route('/people', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'
