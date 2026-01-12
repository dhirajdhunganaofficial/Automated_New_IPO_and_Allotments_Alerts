from extensions import db

class Subscriber(db.Model):
    __tablename__ = "subscribers"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    frequency = db.Column(db.String(50), nullable=False)
    timezone = db.Column(db.String(50), nullable=False, default="UTC")
    still_subscribe = db.Column(db.Boolean, default=True)

