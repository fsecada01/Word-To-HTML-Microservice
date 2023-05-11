from backend.settings.dev import Settings as DevSettings
from backend.settings.prod import Settings as ProdSettings

settings_dict = {"dev": DevSettings, "prod": ProdSettings}


def get_settings(env: str = "dev", debug: bool = False):
    settings = settings_dict.get(env)()
    if debug:
        settings.DEBUG = debug

    return settings


debug_arg = True
env_arg = "dev"
app_settings = get_settings(env=env_arg, debug=debug_arg)
