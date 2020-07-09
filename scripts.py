from flask_script import Manager
from src import create_app,db
app = create_app
manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == "__main__":
    manager.run()
    print("Database initialized successfully!")
    print("Migrations are not handled by init-db")