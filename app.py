# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import models after db is initialized
    import models

    with app.app_context():
        db.create_all()  # create tables if not exists

    # Routes
    @app.route("/")
    def index():
        return render_template("index.html")

    return app


# Run the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
