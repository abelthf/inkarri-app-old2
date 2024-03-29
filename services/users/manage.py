import unittest
from flask.cli import FlaskGroup

from project import app, db

cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Ejecuta las pruebas sin cobertura de codigo"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

#$ docker-compose -f docker-compose-dev.yml up -d --build


if __name__ == '__main__':
    cli()
