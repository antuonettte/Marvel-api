from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class MarvelCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text())
    comics_appeared_in = db.Column(db.Text())
    super_power = db.Column(db.String(50))
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        from app.blueprints.auth.models import User

        return {
            'id':self.id,
            'name': self.name,
            'description': self.description,
            'comics': self.comics_appeared_in,
            'super_power': self.super_power,
            'date_created': self.date_created,
            'owner': User.query.get(self.owner).to_dict()
        }
        
    def from_dict(self,data):
        for field in ['name','description','comics_appeared_in','super_power','owner']:
            if field in data:
                setattr(self, field, data[field])

