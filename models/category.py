from run import db

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
