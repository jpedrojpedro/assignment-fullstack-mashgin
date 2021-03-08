import models
import datetime as dt
from init import app
from flask import jsonify, abort


@app.route("/menu", methods=['GET'])
def menu_index():
    categories = models.Category.all()
    products = models.Product.all()
    return jsonify({"categories": categories, "products": products})


@app.route("/orders", methods=['POST'])
def create_order():
    pass


@app.route("/orders/<int:order_id>", methods=['GET'])
def show_order(order_id):
    models.Order.get_or_none(id=order_id)


@app.route("/orders/<int:order_id>/products/<int:product_id>/add", methods=['GET'])
def add_product(order_id, product_id):
    new_item, item = models.Item.get_or_create(order_id=order_id, product_id=product_id)
    if new_item:
        p = models.Product.get_by_id(product_id)
        item.price = p.price
        item.quantity = 1
        item.save()
        return jsonify(item)
    item.quantity += 1
    item.updated_at = dt.datetime.now()
    item.save()
    return jsonify(item)


@app.route("/orders/<int:order_id>/products/<int:product_id>/remove", methods=['GET'])
def remove_product(order_id, product_id):
    item = models.Item.get_or_none(order_id=order_id, product_id=product_id)
    if item:
        item.quantity -= 1
        if item.quantity == 0:
            item.delete()
            return jsonify({})
        item.updated_at = dt.datetime.now()
        return jsonify(item)
    abort(404)


@app.route("/", methods=['GET'])
def root():
    return jsonify({"msg": "Hello world!"})
