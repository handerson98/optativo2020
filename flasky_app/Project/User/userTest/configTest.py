from flask_testing import TestCase
from flask import current_app
from Project import db

class configTest(TestCase):

    def create_app(self):
        return current_app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
