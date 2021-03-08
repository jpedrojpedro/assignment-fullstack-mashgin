import json
import datetime as dt
import decimal
from pathlib import Path
import peewee as pw
from init import db
from playhouse.shortcuts import model_to_dict


class BaseModel(pw.Model):
    @classmethod
    def all(cls):
        objs = cls.select()
        ret = []
        for obj in objs:
            m_dict = model_to_dict(obj)
            m_dict = {k: (str(v) if type(v) in [dt.datetime, decimal.Decimal] else v) for k, v in m_dict.items()}
            ret.append(m_dict)
        return ret

    class Meta:
        database = db


class Category(BaseModel):
    id = pw.IntegerField(primary_key=True)
    image_id = pw.CharField()
    name = pw.CharField()
    created_at = pw.DateTimeField(default=dt.datetime.now)
    updated_at = pw.DateTimeField(default=dt.datetime.now)

    class Meta:
        table_name = 'category'


class Product(BaseModel):
    id = pw.IntegerField(primary_key=True)
    category_id = pw.ForeignKeyField(Category, backref='products')
    image_id = pw.CharField()
    name = pw.CharField()
    price = pw.DecimalField(decimal_places=2)
    created_at = pw.DateTimeField(default=dt.datetime.now)
    updated_at = pw.DateTimeField(default=dt.datetime.now)

    class Meta:
        table_name = 'product'


class Order(BaseModel):
    id = pw.AutoField(primary_key=True)
    name = pw.CharField()  # auto generated field
    total_amount = pw.DecimalField(decimal_places=2)
    created_at = pw.DateTimeField(default=dt.datetime.now)
    updated_at = pw.DateTimeField(default=dt.datetime.now)

    class Meta:
        table_name = 'order'


class Item(BaseModel):
    id = pw.AutoField(primary_key=True)
    order_id = pw.ForeignKeyField(Order, backref='items')
    product_id = pw.ForeignKeyField(Product)
    quantity = pw.IntegerField()
    price = pw.DecimalField(decimal_places=2)
    created_at = pw.DateTimeField(default=dt.datetime.now)
    updated_at = pw.DateTimeField(default=dt.datetime.now)

    class Meta:
        table_name = 'item'


def create_tables():
    db.create_tables([Category, Product, Order, Item], safe=True)


def populate_database(folder="static", filename="menu.json"):
    menu_path = Path(folder, filename)
    with open(menu_path) as fp:
        menu = json.loads(fp.read())
        for category in menu["categories"]:
            Category.get_or_create(**category)
        for product in menu["products"]:
            Product.get_or_create(**product)
