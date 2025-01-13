import mysql.connector

#mydb = mysql.connector.connect(
#    host='localhost',
#    user = 'root',
#    password ='root',
#    port = '3306',
#    database = 'pp_shop'
#)

#mycursor = mydb.cursor()

#mycursor.execute('SELECT * FROM myuser')
#myusers = mycursor.fetchall()
#for myuser in myusers:
#    print(myuser)
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, User, Order_Item, Item
from models import User

DATABASE_URL = "mysql://root:root@localhost:3306/pp_shop"
engine = create_engine(DATABASE_URL,
                       echo = False,
                       #pool_size=5,
                       #max_overflow=10
                       )
with engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res.all()=}")

Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()

# Приклад вибірки всіх користувачів
users = session.query(User).all()

print(users)
