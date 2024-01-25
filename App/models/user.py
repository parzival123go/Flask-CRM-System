from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    staff_id = db.Column(db.Integer, nullable=False, unique=True)

    def __init__(self, staff_id, username, password):
        self.staff_id = staff_id
        self.username = username
        self.set_password(password)

    def get_json(self):
        return {
            'id': self.id,
            'staff_id': self.staff_id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
