from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=True)
    salary = db.Column(db.String(100), nullable=True)
    url = db.Column(db.String(500), nullable=False)
    date_scraped = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Job {self.title} at {self.company}>"
