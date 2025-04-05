from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy import text
import os

load_dotenv()

# Retrieve credentials from environment variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_NAME')

print("username:", username)
print("password:", password)
print("host:", host)
print("port:", port)
print("database:", database)

# Database URL
DB_URL = f"mysql+mysqlconnector://{username}:{
    password}@{host}:{port}/{database}"

# Create an engine
engine = create_engine(DB_URL)
# Add this after engine creation
with engine.connect() as conn:
    result = conn.execute(text("SELECT DATABASE()"))
    current_db = result.scalar()
    print(f"ACTUALLY CONNECTED TO DATABASE: {current_db}")
