from run import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    picture = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String(64))
