from sqlalchemy.sql import func
from config import db, bcrypt
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User {self.id}>:  {self.email}'

    @classmethod
    def validate_subscription(cls, postData):
        is_valid = True
        if len(postData['email']) < 1 or not EMAIL_REGEX.match(postData['email']):
            is_valid = False
            flash("Please enter a valid email address.")
        return is_valid




class Tour(db.Model):
    __tablename__ = "tours"
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.Text)
    date = db.Column(db.Text)
    city = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    added_by = db.relationship("User", foreign_keys=[
                               user_id], backref="user_authors")
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now())
