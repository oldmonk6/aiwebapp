from flask import Blueprint
from app.controllers.blogcontroller import generate
blog_route=Blueprint("blog_route",__name__)
blog_route.route("/generate",methods=["POST"])(generate)