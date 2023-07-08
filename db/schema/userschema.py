def user_indvidual(user) -> dict:
    return {
         "id" : str(user["_id"]),
        "name" : user["name"],
        "userName" : user["userName"],
        "password" : user["password"],
        "email" : user["email"]
    }

def user_list(users) ->list:
    return[user_indvidual(user) for user in users]