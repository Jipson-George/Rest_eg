from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate, upgrade
from models import db  # Assuming models.py defines 'db' as SQLAlchemy()

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Configuration for the Flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql+psycopg2://postgres:password@db:5432/mydatabase')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    # Initialize the SQLAlchemy object with the app
    db.init_app(app)
    
    # Initialize the Flask-Migrate object with the app
    migrate = Migrate(app, db)

    # Initialize API and CORS
    api = Api(app)
    CORS(app)
    
    # Automatically apply migrations on startup
    with app.app_context():
        upgrade(directory="migrations")
    
    # Define a route
    @app.route("/")
    def hello():
        return "Hello, World!"
    
    # Return the app instance
    return app

if __name__ == "__main__":
    # Create the app and run it
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
