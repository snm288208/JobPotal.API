from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel) :
    id : str
    name : str
    userName : str
    password : str
    email : str
    


def user_indvidual(user) -> dict:
    response = UserResponse(id=(str(user["_id"])), name=(user["name"]),userName=( user["userName"]), password=(user["password"]), email=(user["email"]))
    return response

        
def user_list(users) ->list:
    return[user_indvidual(user) for user in users]