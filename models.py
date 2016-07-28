__author__ = 'pridemai'
from sqlalchemy import Column, Integer, String
from database import Base,db_session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

#create a user
#writing
# u = User("admin", "admin@localhost")
# db_session.add(u)
# db_session.commit()
#querying
# User.query.filter(User.name == 'admin').first()