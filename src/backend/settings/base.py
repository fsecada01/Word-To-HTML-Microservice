from decouple import config
from pydantic_settings import BaseSettings


# FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


class Settings(BaseSettings):
    SECRET_KEY: str = config("SECRET_KEY")
