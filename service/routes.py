from flask import jsonify, request, abort, url_for
from service.models import Product, DataValidationError
from . import app

@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    """ Read a Product """
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product {product_id} not found")
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """ Update a Product """
    product = Product.find(product_id)
    if not product:
        abort(404, f"Product {product_id} not found")
    product.deserialize(request.get_json())
    product.update()
    return jsonify(product.serialize()), 200

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """ Delete a Product """
    product = Product.find(product_id)
    if product:
        product.delete()
    return "", 204

@app.route("/products", methods=["GET"])
def list_products():
    """ List Products with optional filtering """
    products = []
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available:
        products = Product.find_by_availability(available.lower() == "true")
    else:
        products = Product.all()

    return jsonify([p.serialize() for p in products]), 200


