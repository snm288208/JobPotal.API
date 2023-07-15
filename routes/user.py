
from typing import List
from fastapi import APIRouter
from db.models.user import User
from db.schema.userschema import UserResponse, user_list
from db.schema.userschema import user_indvidual
from extensionMethods.ApiReponse import ApiResponse, queriedSuccesfully
from config.monogodb import User_collection
from bson import objectid
from fastapi.responses import JSONResponse

userrouter = APIRouter()

@userrouter.get("/home", response_model = ApiResponse[List[UserResponse]])
def getuser(userName: str):
     user = user_list(User_collection.find({"userName":userName}))
     response = ApiResponse[List[UserResponse]](Result= user, StatsCode='200', Message= "QueriedSucessFully")
     return response

@userrouter.post("/addUser", response_model = ApiResponse[bool])
def adduser(user:User):
     checkUser = user_list(User_collection.find({"userName":user.userName} ))
     if checkUser != None :
          User_collection.insert_one(dict(user))
          return ApiResponse[str](Result= True, StatsCode='200', Message= "QueriedSucessFully")
     else :
          return ApiResponse[str](Result= False, StatsCode='200', Message= "Already Exists")





