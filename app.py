from flask import Flask
from routes.post import post_pages
from sqlmodel import SQLModel, create_engine
from models.post import Post

def create_app():
    app = Flask(__name__,  static_folder='static')
    app.register_blueprint(post_pages)
    app.engine = create_engine("sqlite:///database.db")
  
    return app

@app.before_first_request
def create_db():
    SQLModel.metadata.create_all(app.engine)
