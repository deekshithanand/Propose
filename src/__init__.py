from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    
    with app.app_context():
        #import blue prints
        from .auth import auth
        from .topics import topic
        from .posts import post

        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(topic.topics_bp)
        app.register_blueprint(post.post_bp)
    
        
    return app

