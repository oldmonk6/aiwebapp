from flask import request,jsonify,make_response
from werkzeug.security import generate_password_hash,check_password_hash
from app.utils.jwthandler import gen_token
from prisma.models import User


def login():
    data=request.json
    
    email=data.get("email")
    password=data.get("password")
    user=User.prisma().find_many(where={"email":email})
    if not user or not check_password_hash(user[0].password,password):
        return jsonify({"message":"Invalid credentials"}),401
    token=gen_token(user[0].id)
    response = make_response(jsonify({"message": "Login successful"}), 200)
    response.set_cookie("token", token, httponly=True,  # Prevent JavaScript access
        secure=False, # Send only over HTTPS (set to False for local dev)
        samesite="Lax", # Protect against CSRF
        max_age=3600 ,
        path="/" )
    return response
