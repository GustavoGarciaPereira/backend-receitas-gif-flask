from flask import Blueprint, jsonify

livro = Blueprint("livros", __name__, url_prefix="/api/livro")


@livro.route("/")
def hello_world():
    return jsonify({"status": 200})


def config(app):
    app.register_blueprint(livro)
