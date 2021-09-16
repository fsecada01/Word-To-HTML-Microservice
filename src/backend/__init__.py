from flask import Flask
from fastapi import FastAPI


def get_app(debug=False):
    """
    Creates instance of Flask application.
    :param debug:
    :return app:
    """

    app = FastAPI(
        debug=debug,
        title='Microsoft Word to HTML Converter',
        description="A microservice to convert word documents into HTML. "
                    "Intended for consumption by ADC44's admin panel."
    )

    return app


fast_app = get_app()
