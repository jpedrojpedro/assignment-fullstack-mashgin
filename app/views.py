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
    order = models.Order()
    order.save()
    return jsonify(order.to_dict())


@app.route("/orders/<int:order_id>", methods=['GET'])
def show_order(order_id):
    order = models.Order.get_or_none(id=order_id)
    if not order:
        abort(404)
    return jsonify(order.to_dict())


@app.route("/orders/<int:order_id>/products/<int:product_id>/add", methods=['GET'])
def add_product(order_id, product_id):
    item = models.Item.get_or_none(order_id=order_id, product_id=product_id)
    if not item:
        item = models.Item()
        order = models.Order.get_by_id(order_id)
        product = models.Product.get_by_id(product_id)
        item.order_id = order.id
        item.product_id = product.id
        item.price = product.price
        item.quantity = 1
        item.save()
        return item.to_dict()
    item.quantity += 1
    item.updated_at = dt.datetime.now()
    item.save()
    return item.to_dict()


@app.route("/orders/<int:order_id>/products/<int:product_id>/remove", methods=['GET'])
def remove_product(order_id, product_id):
    item = models.Item.get_or_none(order_id=order_id, product_id=product_id)
    if not item:
        abort(404)
    item.quantity -= 1
    if item.quantity == 0:
        models.Item.delete_by_id(item.id)
        return jsonify({})
    item.updated_at = dt.datetime.now()
    item.save()
    return jsonify(item.to_dict)


@app.route("/", methods=['GET'])
def root():
    return jsonify({"msg": "Hello world!"})
