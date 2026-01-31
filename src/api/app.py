from flask import Flask
from .routes import api_routes   # 👈 DOT IMPORT (IMPORTANT)


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )
    app.register_blueprint(api_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
