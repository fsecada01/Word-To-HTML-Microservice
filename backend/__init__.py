from flask import Flask


def get_app(debug=False):
    """
    Creates instance of Flask application.
    :param debug:
    :return app:
    """

    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this_is_a_secret_key"

    if debug is True:
        app.testing = True

    return app


flask_app = get_app()
