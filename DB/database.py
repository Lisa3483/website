from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .databaseClass import User
import psycopg2
Base = declarative_base()


class UserDatabase:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:123@localhost/postgres')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_user(self, nickname, hashed_password, email):
        new_user = User(nickname=nickname, hashed_password=hashed_password, email=email)

        self.session.add(new_user)

        self.session.commit()

    def close_connection(self):
        self.session.close()

    def check_log_in(self, email, password):
        user = self.session.query(User).filter(User.email == email, User.hashed_password == password).first()
        if user:

            return user.nickname,user.id
        else:
            return False

    def check_regis(self, email, nickname):
        user = self.session.query(User).filter((User.email == email) | (User.nickname == nickname)).first()
        if user:

            return True
        else:
            return False
