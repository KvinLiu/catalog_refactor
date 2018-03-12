from run import db

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    cat_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String)
    description = db.Column(db.String)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'cat_id' : self.cat_id,
            'description' : self.description,
            'id' : self.id,
            'title' : self.title
        }
