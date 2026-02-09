from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["hrms"]

employee_collection = db["employees"]
attendance_collection = db["attendance"]
