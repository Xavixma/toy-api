from flask import Blueprint, request, jsonify, g, abort, current_app
from .models import Item
from . import db
from backend.auth import generate_token, require_auth, USERS_DB


bp = Blueprint("routes", __name__)

@bp.before_request
def extract_tenant():
    tenant_id = request.headers.get('X-Tenant-ID')
    if request.path not in ["/ping","/","/login"] and "X-Tenant-ID" not in request.headers:
        abort(400, description="Missing X-Tenant-ID header")
    g.tenant_id = tenant_id


@bp.route("/")
def hello():
    return {"message": "Et el puto Xavi!"}


@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = USERS_DB.get(username)
    if user and user["password"] == password:
        token = generate_token(username, user["tenant_id"])
        return jsonify({"access_token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@bp.route("/me", methods=["GET"])
@require_auth
def me():
    try:
        return jsonify({
            "username": g.username,
            "tenant_id": g.tenant_id
            })
    except Exception as e:
        current_app.logger.error(f"❌ ERROR al /me: {e}")
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500


@bp.route("/items", methods=["GET"])
@require_auth
def get_items():
    try:
        items = Item.query.filter_by(tenant_id=g.tenant_id).all()
        return jsonify([{"id": item.id, "name": item.name} for item in items])
    except Exception as e:
        current_app.logger.error(f"❌ ERROR retrieving items: {e}")
        return jsonify({"error": str(e)}), 500

@bp.route("/items", methods=["POST"])
@require_auth
def create_item():
    try:
        data = request.get_json()
        if "name" not in data:
            return jsonify({"error": "Missing 'name' field"}), 400

        item = Item(name=data['name'], tenant_id=g.tenant_id)
        db.session.add(item)
        db.session.commit()
        return jsonify({"message": "Item created"}), 201
    except Exception as e:
        current_app.logger.error(f"❌ ERROR retrieving items: {e}")
        return jsonify({"error": str(e)}), 500

@bp.route("/ping")
def ping():
    return jsonify({"message": "pong"})
