# rest_server_merged
REST API FLASK SERVER DOCKERIZED

This development was done on a Ubuntu 20.04 Desktop server.

The "mission" was to implement a REST API server given very precise instructions.

To develop and test the application I used Flask and Python 3.8.
I used the development web server included in Flask and SQLite as the database.
I added authentication to the API.

Once all was working fine I refactored the application so it could run
on a Docker container.

I changed the database for Postgres and the web server for Gunicorn.

To try the application open a terminal and execute:
$ git clone https://github.com/githubcj79/rest_server_merged.git
$ cd rest_server_merged
$ docker-compose -f docker-compose.prod.yml up -d --build

To test GET /people
$ curl -u ghost:python -i -H "Content-Type: application/json" -X GET  \
http://127.0.0.1:5000/people

To test GET /people/:rut
$ curl -u ghost:python -i -H "Content-Type: application/json" -X GET  \
http://127.0.0.1:5000/people/rut_1

To test POST /people + json
$ curl -u ghost:python -i -H "Content-Type: application/json" -X POST -d \
'{"rut":"rut_1","name":"name_1","lastName":"lastName_1","age":10,"course":11}' \
http://127.0.0.1:5000/people

To test PUT /people/:id + json
$ curl -u ghost:python -i -H "Content-Type: application/json" -X PUT -d \
'{"name":"name_1_mod","lastName":"lastName_1_mod"}' \
http://127.0.0.1:5000/people/1

To test DELETE /people/:id
$ curl -u ghost:python -i -H "Content-Type: application/json" -X DELETE  \
http://127.0.0.1:5000/people/1
