# Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Boolean, Column, Date, Float, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    e_mail = Column(String)
    password = Column(String)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    description = Column(String)
    prise = Column(Float)

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('users.id'))
    id_product = Column(Integer, ForeignKey('products.id'))
    order_date = Column(Date)
    status_order = Column(Boolean)
