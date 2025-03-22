from flask_jwt_extended import create_access_token,decode_token
from datetime import timedelta
def gen_token(id):
    return create_access_token(identity=id,expires_delta=timedelta(days=1))