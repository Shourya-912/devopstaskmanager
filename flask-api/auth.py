import jwt
from flask import request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
  
def verify_token():
    auth_header = request.headers.get('Authorization')
 
    if not auth_header:
        return None, jsonify({"msg": "Authorization header missing"}), 401
 
    try:
        token = auth_header.split(" ")[1]  # Bearer <token>
        decoded = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return decoded['sub'], None, None  # sub = user_id
    
    except jwt.ExpiredSignatureError:
        return None, jsonify({"msg": "Token expired"}), 401
    
    except jwt.InvalidTokenError:
        return None, jsonify({"msg": "Invalid token"}), 403