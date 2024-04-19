from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Hedgehog(Base):
    __tablename__ = 'Table_hedgehogs'

    id = Column(Integer, primary_key=True)
    chance = Column(Float)
    cost = Column(Float)
    img_name = Column(String)


class Cat(Base):
    __tablename__ = 'Table_cats'

    id = Column(Integer, primary_key=True)
    chance = Column(Float)
    cost = Column(Float)
    img_name = Column(String)


class Dog(Base):
    __tablename__ = 'Table_dogs'

    id = Column(Integer, primary_key=True)
    chance = Column(Float)
    cost = Column(Float)
    img_name = Column(String)


# Создаем движок для подключения к базе данных
engine = create_engine('sqlite:///cases_info.db')

# Создаем таблицы, если они еще не существуют
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Добавляем данные
hedgehogs_data = [
    {'chance': 0.05, 'cost': 10000, 'img_name': 'hedgehog1.png'},
    {'chance': 0.1, 'cost': 20000, 'img_name': 'hedgehog2.png'},
    {'chance': 0.15, 'cost': 30000, 'img_name': 'hedgehog3.png'},
    {'chance': 0.2, 'cost': 40000, 'img_name': 'hedgehog4.png'},
    {'chance': 0.25, 'cost': 50000, 'img_name': 'hedgehog5.png'}
]

cats_data = [
    {'chance': 0.05, 'cost': 10000, 'img_name': 'cat1.png'},
    {'chance': 0.1, 'cost': 20000, 'img_name': 'cat2.png'},
    {'chance': 0.15, 'cost': 30000, 'img_name': 'cat3.png'},
    {'chance': 0.2, 'cost': 40000, 'img_name': 'cat4.png'},
    {'chance': 0.25, 'cost': 50000, 'img_name': 'cat5.png'}
]

dogs_data = [
    {'chance': 0.05, 'cost': 10000, 'img_name': 'dog1.png'},
    {'chance': 0.1, 'cost': 20000, 'img_name': 'dog2.png'},
    {'chance': 0.15, 'cost': 30000, 'img_name': 'dog3.png'},
    {'chance': 0.2, 'cost': 40000, 'img_name': 'dog4.png'},
    {'chance': 0.25, 'cost': 50000, 'img_name': 'dog5.png'}
]

# Добавляем данные для ежей
for data in hedgehogs_data:
    hedgehog = Hedgehog(**data)
    session.add(hedgehog)

# Добавляем данные для кошек
for data in cats_data:
    cat = Cat(**data)
    session.add(cat)

# Добавляем данные для собак
for data in dogs_data:
    dog = Dog(**data)
    session.add(dog)

# Фиксируруруем изменения в базе данных
session.commit()

# Закрываем сессию
session.close()
