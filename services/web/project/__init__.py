'''
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")

'''
# -------------------------------------------------------------

import os
from flask import Flask, jsonify, abort, request, make_response
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    rut = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64), unique=False, index=False)
    lastName = db.Column(db.String(64), unique=False, index=False)
    age = db.Column(db.Integer, unique=False, index=False)
    course = db.Column(db.Integer, unique=False, index=False)

    def __repr__(self):
        return '<Person %r>' % self.rut

    def asdict(self):
        return {'id': self.id, 'rut': self.rut,
                'name': self.name, 'lastName': self.lastName,
                'age': self.age, 'course': self.course}


# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# auth = HTTPBasicAuth()

# @auth.get_password
# def get_password(username):
#     if username == 'ghost':
#         return 'python'
#     return None

# @auth.error_handler
# def unauthorized():
#     return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# db = SQLAlchemy(app)

# class Person(db.Model):
#     __tablename__ = 'people'
#     id = db.Column(db.Integer, primary_key=True)
#     rut = db.Column(db.String(64), unique=True, index=True)
#     name = db.Column(db.String(64), unique=False, index=False)
#     lastName = db.Column(db.String(64), unique=False, index=False)
#     age = db.Column(db.Integer, unique=False, index=False)
#     course = db.Column(db.Integer, unique=False, index=False)

#     def __repr__(self):
#         return '<Person %r>' % self.rut

#     def asdict(self):
#         return {'id': self.id, 'rut': self.rut,
#                 'name': self.name, 'lastName': self.lastName,
#                 'age': self.age, 'course': self.course}

# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, Person=Person)

# GET /people
@app.route('/people', methods=['GET'])
# @auth.login_required
def get_people():
    people = Person.query.all()
    list_ = [person_.asdict() for person_ in people]
    return jsonify( {'people': list_} ), 200

# GET /people/:rut
@app.route('/people/<rut>', methods=['GET'])
# @auth.login_required
def get_rut(rut):
    person_ = Person.query.filter_by(rut=rut).first()
    if person_ is None:
        abort(404)
    return jsonify( {'person': person_.asdict()} ), 200

# POST /people + json
@app.route('/people', methods=['POST'])
# @auth.login_required
def create_person():
    if not request.json or not 'rut' in request.json:
        abort(400)
    rut_ = request.json['rut']
    person_ = Person.query.filter_by(rut=rut_).first()
    if person_ is None:
        name_ = request.json.get('name', "")
        lastName_ = request.json.get('lastName', "")
        age_ = request.json.get('age', 0)
        course_ = request.json.get('course', 1)
        person_ = Person(rut=rut_,name=name_,lastName=lastName_,
                          age=age_,course=course_)
        db.session.add(person_)
        db.session.commit()
    else:
        abort(400)
    return jsonify( {'person': person_.asdict()} ), 201

# PUT /people/:id + json
@app.route('/people/<id>', methods=['PUT'])
# @auth.login_required
def update_person(id):
    if not request.json:
        abort(400)
    person_ = Person.query.filter_by(id=id).first()
    if person_ is None:
        abort(404)
    person_dict = person_.asdict()
    for key in ['name', 'lastName', 'age', 'course']:
        if key in request.json:
            person_dict[key] = request.json[key]
    person_.name = person_dict['name']
    person_.lastName = person_dict['lastName']
    person_.age = person_dict['age']
    person_.course = person_dict['course']
    db.session.add(person_)
    db.session.commit()
    return jsonify( {'person': person_dict} ), 200

# DELETE /people/:id
@app.route('/people/<id>', methods=['DELETE'])
# @auth.login_required
def delete_id(id):
    person_ = Person.query.filter_by(id=id).first()
    if person_ is None:
        abort(404)
    db.session.delete(person_)
    db.session.commit()
    return jsonify( {'person': person_.asdict()} ), 200

@app.route("/")
def hello_world():
  return jsonify(hello="world")



