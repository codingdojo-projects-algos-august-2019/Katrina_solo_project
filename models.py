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

    @classmethod
    def edit_tour(cls, edit_tour_data):
        print(session['user_id'])
        edit_tour = cls(tour_id = session["tour_id"], artist=edit_tour_data['artist'], date=edit_tour_data['date'], ciit=edit_tour_data['city'])
        print("updating your artist tour")
        print(edit_tour)
        db.session.update(edit_tour)
        db.session.commit()
        return edit_tour

    @classmethod
    def validate_edit(cls, edit_tour_data): 
        print(edit_tour_data)           
        is_valid = True
        if len(edit_tour_data['artist']) < 2:
            is_valid = False
            flash("A minimum of 2 characters is required.", "bad_artist")
        if len(edit_tour_data['date']) < 2:   
            is_valid = False
            flash("Please enter a valid date.", "bad_date")
        if len(edit_tour_data['city']) < 2:
            is_valid = False
            flash("Please enter a valid city.")

        
        return is_valid