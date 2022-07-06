from .extensions import db

class BaseModel(db.Model):

    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key = True)

    @staticmethod 
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.save(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

