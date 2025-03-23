from flask import request,jsonify,make_response
from werkzeug.security import generate_password_hash,check_password_hash
from app.utils.jwthandler import gen_token
from prisma.models import User

def signup():
    data=request.json
    email=data.get("email")
    password=data.get("password")
    if(not email or not password):
        return jsonify({"message":"Email and password are required"}),400
    user=User.prisma().find_first(where={"email":email})
    if user:
        return jsonify({"message":"User already exists"}),400
    user1= User.prisma().create(
        data={"email": email, "password": generate_password_hash(password)}
    )
    token=gen_token(user1.id)
    response=make_response(jsonify({"message":"User created"}),201)
    response.set_cookie("token",token,httponly=True,secure=False,samesite="Lax",max_age=3600,path="/")
    return response
