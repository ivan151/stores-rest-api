import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel
from db import db



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="This field can not be empty",
            )
    parser.add_argument('password',
            type=str,
            required=True,
            help="This field can not be empty",
            )
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_name(data['username']):
            return {'message': 'User wuth this name already exists. Try another name'}, 400

        user = UserModel(**data)
        user.save_to_db()
        # conn = sqlite3.connect('data.db')
        # curs = conn.cursor()
        # insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # user = (data['username'], data['password'])
        # curs.execute(insert_query, user)
        # conn.commit()
        # conn.close()
        return {"message": "user added!"}