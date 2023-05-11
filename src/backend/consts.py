import os

BASE_DIR: str = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
BACKEND_DIR: str = os.path.join(BASE_DIR, "backend")
