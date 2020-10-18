from flask_restful import Resource, reqparse
import sqlite3
#from flask_jwt import jwt_required
from models.store import StoreModel
from db import db

class Store(Resource):
    def get(self, name):
        store =  StoreModel.find_by_name(name)
        return store.json() if store else {'message': 'No such store'}, 404
        

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Such store already exists!"}, 400
        new_store = StoreModel(name)

        try:
            new_store.save_to_db()
            return {"message": "Store is created!"}, 201
        except:
            return {"message": "Error occured!"}, 500


    #@jwt_required()
    def delete(self, name):
        store_to_delete = StoreModel.find_by_name(name)
        if store_to_delete:
            db.delete_from_db(store_to_delete)
        return {"message": "Store doesn't exist!"}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.name for store in StoreModel.query.all()]}