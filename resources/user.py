import sqlite3
from flask_restful import Resource, reqparse
from models.usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        type=str,
                        help="This field cannot be left blank!!!"
                        )
    parser.add_argument('password',
                        required=True,
                        type=str,
                        help="This field cannot be left blank!!!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists"}, 400

        print(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
