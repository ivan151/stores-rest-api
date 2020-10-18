from models.user import UserModel
#from werkzeug.security import safe_str_cmp


def auth(username, password):
    user = UserModel.find_by_name(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)