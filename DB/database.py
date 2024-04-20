from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Numeric, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    datetime = Column(DateTime, default=func.now())
    balance = Column(Numeric(precision=10, scale=2), default=0.0)
    nickname = Column(String(10), nullable=False)
    hashed_password = Column(String, nullable=True)
    email = Column(String, index=True, unique=True, nullable=True)


class UserDatabase:
    def __init__(self):
        # Путь к файлу базы данных SQLite3
        db_path = os.path.join(os.path.dirname(__file__), 'mydatabase.db')
        self.engine = create_engine('sqlite:///' + db_path, connect_args={'check_same_thread': False})
        # Создаем таблицы, если они еще не существуют
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
            return user.nickname, user.id
        else:
            return False

    def check_regis(self, email, nickname):
        user = self.session.query(User).filter((User.email == email) | (User.nickname == nickname)).first()
        if user:
            return True
        else:
            return False

    def change_user_balance(self, user_id, new_balance):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            user.balance += int(new_balance)
            self.session.commit()
        else:
            print("User not found.")

    def change_balance(self, user_id, money):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user.balance >= money:
            user.balance -= money
            self.session.commit()
            return True
        else:
            return False
    def get_balance(self,user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        return user.balance