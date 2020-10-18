from decouple import config
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
BACKEND_DIR = os.path.join(BASE_DIR, "backend")
# FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

SECRET_KEY = config("SECRET_KEY")
