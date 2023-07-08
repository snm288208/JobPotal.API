from pymongo import MongoClient


client = MongoClient("mongodb+srv://sss288208:3ZSZI92diRPDHpqu@cluster0.oesv9zc.mongodb.net/?retryWrites=true&w=majority")

db = client.job

User_collection = db["User"]