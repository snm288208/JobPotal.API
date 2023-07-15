from typing import Optional
from typing import Generic
from typing import TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")
def queriedSuccesfully(result, msg:str = None):
    if msg == None :
        return {
            "result":result,
            "message":"Queried Sucessfully",
            "statusCode" :"OK"
        }
    else:
         return {
            "result":result,
            "message":msg,
            "statusCode" :"OK"
        }

class ApiResponse(GenericModel, Generic[T]):
    Result : T
    StatsCode: int
    Message : str
