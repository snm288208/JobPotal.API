from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from db import db
from routes.user import userrouter

app =  FastAPI()

connectionString = "mongodb+srv://sss288208:gQOEcPg2Hu64snuf@cluster0.oesv9zc.mongodb.net/?retryWrites=true&w=majority"

# db.connect_to_database(connectionString)

app.include_router(userrouter)

@app.get("/")
def home():
    return {"hellO Application Started"}




# asyncronus api 

# async def home():
#     await function()
#     return {"hellO Application Started"}