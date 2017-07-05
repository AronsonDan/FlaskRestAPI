from flask_restful import Resource, reqparse
from models.usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        required=True,
                        type=str,
                        help="username was not specified in the request, the request cannot be processed"
                        )
    parser.add_argument('password',
                        required=True,
                        type=str,
                        help="password was not specified in the request, the request cannot be processed"
                        )
    parser.add_argument('role',
                        required=True,
                        type=str,
                        help="Role was not specified in the request, the request cannot be processed"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
