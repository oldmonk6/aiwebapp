from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
from app.routes.authroutes import auth_routes
from app.routes.blogroutes import blog_route
from prisma import Prisma,register

load_dotenv()
def create_app():
    db=Prisma()
    db.connect()
    register(db)
    app=Flask(__name__)
    app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET")
    jwt=JWTManager(app)
    CORS(app,supports_credentials=True,origins=["http://localhost:3000"], allow_headers=["Content-Type", "X-Requested-With", "Authorization"])
    app.register_blueprint(auth_routes,url_prefix="/auth")
    app.register_blueprint(blog_route,url_prefix="/blog")
    return app

