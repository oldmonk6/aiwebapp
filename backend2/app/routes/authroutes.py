from flask import Blueprint
from app.controllers.authcontroller import login
auth_routes=Blueprint("auth_routes",__name__)
auth_routes.route("/login",methods=["POST"])(login)
