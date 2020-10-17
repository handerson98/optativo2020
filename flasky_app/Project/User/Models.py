from Project import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    rut = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    confirmPassword = db.Column(db.String, nullable=False)
