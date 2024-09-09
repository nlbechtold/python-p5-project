# config.py
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

# Define metadata and instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
bcrypt = Bcrypt()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')  # Add this line
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications to avoid overhead

    # Flask-Mail Configuration
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() in ['true', '1']
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False').lower() in ['true', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'nancyleebechtold@gmailcom')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'nancyleebechtoldil@gmail.com')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')

# Note: Removed the app initialization from here.


# Remove the print statements or move them to app.py after configuration is loaded
# print("MAIL_SERVER:", app.config['MAIL_SERVER'])
# print("MAIL_USERNAME:", app.config['MAIL_USERNAME'])

# Instantiate CORS
# CORS(app)


# bcrypt = Bcrypt(app)

# app.secret_key = os.getenv('SECRET_KEY')
# python -c 'import os; print(os.urandom(24))'

# print("MAIL_SERVER:", app.config['MAIL_SERVER'])
# print("MAIL_USERNAME:", app.config['MAIL_USERNAME'])
