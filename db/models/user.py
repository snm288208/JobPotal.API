from pydantic import BaseModel
from typing import Optional

class User(BaseModel) :
    name : str
    userName : str
    password : str
    email : str
    
