from pydantic import BaseModel

class User(BaseModel) :
    name : str
    userName : str
    password : str
    email : str
    
