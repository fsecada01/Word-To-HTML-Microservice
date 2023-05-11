from fastapi import FastAPI


def get_app(debug=False, settings_inst=None):
    """
    Creates instance of Flask application.
    :param settings_inst:
    :param debug:
    :return app:
    """

    app = FastAPI(
        debug=debug,
        title="Microsoft Word to HTML Converter",
        description="A microservice to convert word documents into HTML. "
        "Intended for consumption by ADC44's admin panel.",
    )

    if settings_inst:
        app.settings = settings_inst

    return app
