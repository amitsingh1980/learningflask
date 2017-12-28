from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from flask import Flask

db = SQLAlchemy() 

class User(db.Model):
    __tablename__='Users'
    Name = db.Column(db.String(100), primary_key=True)
    Email = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.Name = name.title()
        self.Email = email.title()