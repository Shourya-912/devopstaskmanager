from flask import Blueprint, request, jsonify
from db import get_connection
import re 
from flask_jwt_extended import create_access_token
from auth import verify_token 

routes = Blueprint('routes', __name__)

# Generate access token to login user 
@routes.route('/login',methods = ['POST'])
def login():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("select * from users where name = %s and email = %s", (name, email))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"error":"invalid credentials"}),401
       
    access_token = create_access_token(identity = str(user['id']))
    return jsonify(access_token = access_token),200
    

# validate email  
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+",email)

# create a user for task
@routes.route('/createuser', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data['email']
    if not is_valid_email(email):
        return jsonify({"error":"invald email format"}), 400
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("insert into users (name, email) values(%s,%s)",(data['name'],data['email']))

    conn.commit()
    conn.close()

    return jsonify({"message":"User Created"}),201


#get all users
@routes.route('/showusers',methods = ['GET'])
def get_users():
    user_from_token, error_response, status_code = verify_token()

    if error_response:
        return error_response, status_code
 
    if not user_from_token:
        return jsonify({"msg": "Access denied"}), 403
    
    conn = get_connection()
    cursor = conn.cursor(dictionary =True)
    cursor.execute("select * from users")

    users = cursor.fetchall()
    conn.close()
    return jsonify(users)


#get user by id
@routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_from_token, error_response, status_code = verify_token()

    if error_response:
        return error_response, status_code
 
    if int(user_from_token) != user_id:
        return jsonify({"msg": "Access denied"}), 403
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("select*from users where id = %s",(user_id,))
    user = cursor.fetchone()
    
    conn.close()
    if user:
        return jsonify(user)
    else:
        return jsonify(None),404


#update user by using userId 
@routes.route('/update/<int:user_id>',methods = ['PUT'])
def update_user(user_id):
    
    data = request.get_json()

    user_from_token, error_response, status_code = verify_token()
    if error_response:
        return error_response, status_code
 
    if int(user_from_token) != user_id:
        return jsonify({"msg": "Access denied"}), 403

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("update users set name = %s, email = %s where id = %s",(data['name'],data['email'],user_id))

    conn.commit()
    conn.close()
    return jsonify({'message': 'user updated'})


# Delete user with userId 
@routes.route('/delete/<int:user_id>',methods = ['DELETE'])
def delete_user(user_id):

    user_from_token, error_response, status_code = verify_token()
    if error_response:
        return error_response, status_code
 
    if int(user_from_token) != user_id:
        return jsonify({"msg": "Access denied"}), 403

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("delete from users where id = %s",(user_id,))

    conn.commit()
    conn.close()
    return jsonify({'message':"user deleted"})