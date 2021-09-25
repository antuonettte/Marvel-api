from datetime import datetime as dt
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    characters = db.relationship('MarvelCharacter',backref='user',lazy='dynamic')

    def create_password_hash(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, current_password):
        return check_password_hash(self.password, current_password)

    def to_dict(self):
        from app.blueprints.main.models import MarvelCharacter as MC

        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email':self.email,
            'characters': [c.to_dict() for c in MC.query.filter_by(user_id = self.id).all()]
        }

    def save(self):
        print(self.password)
        self.create_password_hash(self.password)
        print(self.password)

        db.session.add(self)
        db.session.commit()


    def from_dict(self, data):
        for field in ['first_name','last_name','email','password']:
            if field in data:
                setattr(self, field, data[field])

    def update_profile(self, data):
        for field in ['first_name','last_name','email','bio']:
            if field in data:
                setattr(self,field,data[field])
                db.session.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))