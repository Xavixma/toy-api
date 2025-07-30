from flask import Blueprint, request, jsonify, g, abort
from .models import Item
from . import db


bp = Blueprint("routes", __name__)

@bp.before_request
def extract_tenant():
    tenant_id = request.headers.get('X-Tenant-ID')
    if not tenant_id:
        abort(400, description="Missing X-Tenant-ID header")
    g.tenant_id = tenant_id


@bp.route("/")
def hello():
    return {"message": "Et el puto Xavi!"}

@bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.filter_by(tenant_id=g.tenant_id).all()
    return jsonify([{"id": item.id, "name": item.name} for item in items])


@bp.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    item = Item(name=data['name'], tenant_id=g.tenant_id)
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Item created"}), 201

@bp.route("/ping")
def ping():
    return jsonify({"message": "pong"})
