from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(os.path.join('.env'))
ENVIRONMENT = os.environ.get('ENVIRONMENT')
DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_NAME=os.environ.get('DB_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')