from flask import Flask
from models import create_user_table
from routes import routes
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from datetime import timedelta


app = Flask(__name__)

load_dotenv()


app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)
CORS(app)


#create user table on app startup
create_user_table()


#register routes
app.register_blueprint(routes)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port= int(os.getenv("FLASK_PORT",5000)))
