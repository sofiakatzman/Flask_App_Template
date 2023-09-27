from random import randint

from app import app
from models.models import User
from config import db

def seed():
    # delete current data
    User.query.delete()
    
    # create admin user for testing and debugging
    admin = User(username="admin", admin=True)
    admin.password_hash = 'admin'

    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        seed()
        print("Seed complete!")