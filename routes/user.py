from typing import List, Optional
from fastapi import APIRouter
from db.models.user import User
from db.schema.userschema import user_list
from db.schema.userschema import user_indvidual
from extensionMethods.ApiReponse import queriedSuccesfully
from config.monogodb import User_collection
from bson import objectid
from fastapi.responses import JSONResponse

userrouter = APIRouter()

@userrouter.get("/home",response_model = list[User])

async def getuser(userName: str):
     user = user_list(list(User_collection.find({"userName":userName} )))
     return JSONResponse(user)

@userrouter.post("/addUser")
def adduser(user:User):
     checkUser = user_list(list(User_collection.find({"userName":user.userName} )))
     
     if any(checkUser) == False :
          User_collection.insert_one(dict(user))
          return JSONResponse(queriedSuccesfully("True", None))
     else :
          return queriedSuccesfully("False", None)


