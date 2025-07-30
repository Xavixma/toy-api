from flask import Blueprint, request, jsonify
from .models import Item
from . import db

bp = Blueprint("routes", __name__)

@bp.route("/")
def hello():
    return {"message": "Et el puto Xavi!"}

@bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])

@bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    new_item = Item(name=data["name"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"id": new_item.id, "name": new_item.name}), 201

@bp.route("/ping")
def ping():
    return jsonify({"message": "pong"})
