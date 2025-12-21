import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read environment variables
ENVIRONMENT = os.getenv("ENVIRONMENT")
DEBUG = os.getenv("DEBUG")
API_TITLE = os.getenv("API_TITLE")
API_VERSION = os.getenv("API_VERSION")
API_PORT = int(os.getenv("API_PORT"))

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

print("Environment:", ENVIRONMENT)
print("Debug:", DEBUG)
print("API Title:", API_TITLE)
print("API Version:", API_VERSION)
print("API Port:", API_PORT)
print("Database URL:", DATABASE_URL)
print("Redis URL:", REDIS_URL)
