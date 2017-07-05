from models.usermodel import UserModel
from flask_jwt import current_identity


def authenticate(username, password):
    print("authenticate invoked")
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload):
    print("identity invoked")
    user_id = payload['identity']
    user = UserModel.find_by_id(user_id)
    payload['role'] = user.role
    print('Printing Payload!!!')
    print(payload)
    print(payload['role'])

    return user
