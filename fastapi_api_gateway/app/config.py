from datetime import timedelta
import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

MICROSERVICES = {
    "auth": os.getenv("MICROSERVICE_AUTH"),
    "users": os.getenv("MICROSERVICE_USERS"),
    "courses": os.getenv("MICROSERVICE_COURSES")
}
REDIS_URL = os.getenv("REDIS_URL")


