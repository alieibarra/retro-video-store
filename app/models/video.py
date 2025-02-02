from flask import current_app
from app import db
from datetime import datetime

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    release_date = db.Column(db.DateTime)
    total_inventory = db.Column(db.Integer)
    rentals = db.relationship("Rental", back_populates= "video") #NEW

    def to_dict(self):
            
        return {
            "id": self.id,
            "title": self.title,
            "release_date" : self. release_date,
            "total_inventory" : self.total_inventory,
        }
    
    def remaining_videos(self):
        return self.total_inventory - len(self.rentals)