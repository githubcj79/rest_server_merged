from flask.cli import FlaskGroup

from project import app, db, Person


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(Person(rut="rut_1",name="name_1",lastName="lastName_1",
      age=10,course=11))
    db.session.commit()


if __name__ == "__main__":
    cli()
