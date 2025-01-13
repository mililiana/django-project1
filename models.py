# models.py
from spacy.lang import sa
from sqlalchemy import Column, Integer, String, Date, VARCHAR, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
import sqlalchemy as sqlalchemy_module
Base = sqlalchemy_module.orm.declarative_base()


class User(Base):
    __tablename__ = 'myuser'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    surname = Column(VARCHAR(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    contact_number = Column(VARCHAR(255), nullable=False, unique=False)

    order_items = relationship("Order_Item", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, surname={self.surname}, date_of_birth={self.date_of_birth}, contact_number={self.contact_number})>"

class Order_Item(Base):
    __tablename__ = 'order_item'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String(255), nullable=True)

    user_id = Column(Integer, ForeignKey('myuser.id'), nullable=False)
    user = relationship("User", back_populates="order_items")

    item_id = Column(Integer, ForeignKey('item.id'), nullable=False)
    item = relationship("Item", back_populates="order_items")

    def __repr__(self):
        return f"<Order_Item(id={self.id}, date={self.date}, amount={self.amount}, status={self.status}, user_id={self.user_id}, item_id={self.item_id})>"

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    price = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    color = Column(VARCHAR(255), nullable=False)
    quantity = Column(Integer, nullable=False)

    order_items = relationship("Order_Item", back_populates="item")

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, size={self.size}, color={self.color}, quantity={self.quantity})>"




DATABASE_URL = "mysql://root:root@localhost:3306/pp_shop"
engine = create_engine(DATABASE_URL,
                       echo = False,
                       #pool_size=5,
                       #max_overflow=10
                       )
with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.all()=}")
Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
orders = session.query(Order_Item).all()
item = session.query(Item).all()

print(orders)
