from flask import Flask

from config import Config
from src.database import init_db
from src.routes import register_routes

app = Flask(__name__)

app.config.from_object(Config)

init_db()

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)