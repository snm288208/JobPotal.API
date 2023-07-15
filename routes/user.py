
from typing import List, Optional
from fastapi import APIRouter
from db.models.user import User
from db.schema.userschema import UserResponse, user_list
from db.schema.userschema import user_indvidual
from extensionMethods.ApiReponse import ApiResponse, queriedSuccesfully
from config.monogodb import User_collection
from bson import objectid
from fastapi.responses import JSONResponse

userrouter = APIRouter()

@userrouter.get("/home")
def getuser(userName: str):
     user = user_list(User_collection.find({"userName":userName}))
     response = ApiResponse[list[UserResponse]](Result= user, StatsCode='200', Message= "QueriedSucessFully")
     print (response)
     return response

@userrouter.post("/addUser")
def adduser(user:User):
     checkUser = user_list(User_collection.find({"userName":user.userName} ))
     if checkUser != None :
          User_collection.insert_one(dict(user))
          return JSONResponse(queriedSuccesfully("True", None))
     else :
          return queriedSuccesfully("False", None)





