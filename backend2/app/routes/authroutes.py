from flask import Blueprint
from app.controllers.authcontroller import login
from app.controllers.signupcontroller import signup
auth_routes=Blueprint("auth_routes",__name__)
auth_routes.route("/login",methods=["POST"])(login)
auth_routes.route("/signup",methods=["POST"])(signup)