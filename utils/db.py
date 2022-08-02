import os
from datetime import datetime
from pyasn1_modules.rfc1902 import Integer
from sqlalchemy import MetaData, Table, Column, Integer, Float, Date, create_engine
from sqlalchemy.orm import Session, mapper, sessionmaker


class OrderDb:
    """
    Класс создания подключения к базе данных
    """
    class Orders:
        """
        Класс-представление таблицы sqlalchemy
        """
        def __init__(self, table_number, order_number, price_usd, price_rub, date):
            self.id = None
            self.table_number = table_number
            self.order_number = order_number
            self.price_usd = price_usd
            self.price_rub = price_rub
            self.date = date

    def __init__(self):
        """
        Констурктор класса БД
        """
        self.engine = create_engine(
            f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
            f"@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}")
        self.engine.connect()
        self.metadata = MetaData()

        order = Table('orders', self.metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('table_number', Integer(), nullable=True),
                      Column('order_number', Integer(), nullable=True),
                      Column('price_usd', Integer(), nullable=True),
                      Column('price_rub', Float(), nullable=True),
                      Column('date', Date(), default=True)
                      )
        self.metadata.create_all(self.engine)
        mapper(self.Orders, order)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session.commit()

    def add_data(self, data, valute):
        """
        Метод для добавления данных в таблицу
        """
        for item in tuple(data):
            ord = self.Orders(
                table_number=item[0] if item[0] else None,
                order_number=item[1] if item[1] else None,
                price_usd=item[2] if item[2] else None,
                price_rub=round(int(item[2]) * valute, 2) if item[2] else None,
                date=datetime.strptime(item[3], "%d.%m.%Y") if item[3] else None
            )
            self.session.add(ord)
            self.session.commit()

    def del_data(self):
        """
        Метод очищения таблицы
        """
        self.session.query(self.Orders).delete()
        self.session.commit()

    def print_values(self):
        """
        Печать данных из таблицы
        """
        data = self.session.query(self.Orders).all()
        for item in data:
            print(
                f'{item.table_number} | {item.order_number} | {item.price_usd} | {item.price_rub} | {item.date}')
