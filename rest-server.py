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
# GET /people
@app.route('/people', methods=['GET'])
def get_people():
    return jsonify({'tasks': tasks})

# GET /people/:rut
@app.route('/people/<rut>', methods=['GET'])
def get_rut(rut):
    return jsonify({'tasks': tasks})

# POST /people + json
@app.route('/people', methods=['POST'])
def create_person():
    return jsonify({'tasks': tasks})

# PUT /people/:id + json
@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
    return jsonify({'tasks': tasks})

# DELETE /people/:id
@app.route('/people/<id>', methods=['DELETE'])
def delete_id(id):
    return jsonify({'tasks': tasks})

# @app.route('/')
# def index():
#   return '<h1>Hello World!</h1>'
