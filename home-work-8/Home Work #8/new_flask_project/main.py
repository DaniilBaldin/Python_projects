from flask_project import app
from database import db


if __name__ == '__main__':
    db.create_all(app=app)
    app.run(debug=True)
