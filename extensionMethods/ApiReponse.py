from typing import Optional

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

