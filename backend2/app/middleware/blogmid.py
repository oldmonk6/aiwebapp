from flask import request, jsonify
from functools import wraps
from flask_jwt_extended import decode_token

def auth_required(f):
    """Middleware to check JWT token in cookies."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get("access_token")  # Get token from cookie

        if not token:
            return jsonify({"error": "Unauthorized"}), 401

        try:
            decoded_token = decode_token(token)
            request.user = {"id": decoded_token["sub"]}
        except Exception as e:
            return jsonify({"error": "Invalid token", "message": str(e)}), 401
        
        return f(*args, **kwargs)
    
    return decorated_function