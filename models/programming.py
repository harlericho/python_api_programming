from utils.db import db

class Programming(db.Model):
    __tablename__ = 'programming'
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, names, description):
        self.names = names
        self.description = description