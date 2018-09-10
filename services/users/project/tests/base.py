from flask_testing import TestCase

from project import app, db

class BaseTestCase(TestCase):
    def create_db(self):
        app.config.from_object('project.config.TestingConfig')
        return app
    
    def setUP(self):
        db.create_all()
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()