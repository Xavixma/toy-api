# auth.py
import jwt
import datetime
from flask import request, jsonify, g, current_app
from functools import wraps

# 🔐 Clau secreta per signar els tokens (NO posar en codi real!)
SECRET_KEY = "super-secret-jwt-key"
ALGORITHM = "HS256"

# 🔒 Simulació de base de dades d'usuaris
USERS_DB = {
    "xavi": {"password": "1234", "tenant_id": "tenant-abc"},
    "anna": {"password": "abcd", "tenant_id": "tenant-xyz"}
}

def generate_token(username, tenant_id):
    payload = {
        "username": username,
        "tenant_id": tenant_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"message": "Missing or invalid Authorization header"}), 401

        token = auth_header.split(" ")[1]
        payload = decode_token(token)
        if not payload:
            return jsonify({"message": "Invalid or expired token"}), 401

        g.username = payload["username"]
        g.tenant_id = payload["tenant_id"]
        return f(*args, **kwargs)
    return decorated
