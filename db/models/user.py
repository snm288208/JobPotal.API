from pydantic import BaseModel
from pyrsistent import optional

class User(BaseModel) :
    id : optional[str]
    name : str
    userName : str
    password : str
    email : str
    
