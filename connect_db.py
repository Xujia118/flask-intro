from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve credentials from environment variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

# Database URL
DB_URL = f"mysql+mysqlconnector://{username}:{
    password}@{host}:{port}/{database}"

# Create an engine
engine = create_engine(DB_URL)