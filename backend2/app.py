from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv
import os
from app.routes.authroutes import auth_routes
from app.routes.blogroutes import blog_route
from prisma import Prisma,register
db=Prisma()
db.connect()
register(db)
load_dotenv()
app=Flask(__name__)
app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET")
jwt=JWTManager(app)
CORS(app)
app.register_blueprint(auth_routes,url_prefix="/auth")
app.register_blueprint(blog_route,url_prefix="/blog")
if __name__=="__main__":
    app.run(debug=True)
