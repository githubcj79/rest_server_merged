README

This REST server was implemented following the instructions given in the document Ejercicio SRE-GCP-MidLevel.pdf.

The development was done in a Ubuntu 20.04 Desktop server.

An ad-doc virtual environment was created:
Language: Python 3.8.2
Web Framework: Flask 1.1.2

Besides the REST server rest_server.py, a requirements.txt file that records all
the package dependencies, with the exact version numbers is included.

The application code is available in : https://github.com/githubcj79/rest_server.git

To try the application:

Create a virtual environment.
Activate the virtual environment.
Execute:
(venv) $ pip install -r requirements.txt
(venv) $ export FLASK_APP=rest_server.py
(venv) $ export FLASK_DEBUG=1
(venv)$ flask shell
>>> from rest_server import db
>>> db.create_all()
>>> exit()
(venv) $ flask run

To test GET /people
(venv) $ curl -u ghost:python -i -H "Content-Type: application/json" -X GET  \
http://127.0.0.1:5000/people

To test GET /people/:rut
(venv) $ curl -u ghost:python -i -H "Content-Type: application/json" -X GET  \
http://127.0.0.1:5000/people/rut_1

To test POST /people + json
	(venv) $ curl -u ghost:python -i -H "Content-Type: application/json" -X POST -d \
'{"rut":"rut_1","name":"name_1","lastName":"lastName_1","age":10,"course":11}' \
http://127.0.0.1:5000/people

To test PUT /people/:id + json
(venv)$ curl -u ghost:python -i -H "Content-Type: application/json" -X PUT -d \
'{"name":"name_1_mod","lastName":"lastName_1_mod"}' \
http://127.0.0.1:5000/people/1

To test DELETE /people/:id
(venv) $ curl -u ghost:python -i -H "Content-Type: application/json" -X DELETE  \
http://127.0.0.1:5000/people/1





