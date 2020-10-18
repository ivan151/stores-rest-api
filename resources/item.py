from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.item import ItemModel
from db import db

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
            type=float,
            required=True,
            help="This field can not be empty", 
            )
    parser.add_argument('store_id',
            type=int,
            required=True,
            help="Every item needs a store id", 
            )
            

    @jwt_required()
    def get(self, name):
        item =  ItemModel.find_by_name(name)
        return item.json() if item else {'message': 'No such item'}, 404
        
    @jwt_required()
    def post(self, name):
        # if next(filter(lambda a: a['name'] == name, items), None):
        #     return {'message': 'an item with name {} is already exists'.format(name)}, 400
        #data = request.get_json(silent=True)
        if ItemModel.find_by_name(name):
            return {"message": "Such item already exists!"}, 400

        data = Item.parser.parse_args()
        new_item = ItemModel(name, **data)

        try:
            new_item.save_to_db()
            return {"message": "item is added!"}, 201
        except:
            return {"message": "Error occured!"}, 500


    @jwt_required()
    def delete(self, name):
        item_to_delete = ItemModel.find_by_name(name)
        if item_to_delete:
            db.delete_from_db(item_to_delete)
        return {"message": "Item doesn't exist!"}

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = data['price']
            item.save_to_db()
            return {"message": "item is updated!"}, 201
        else:
            item = ItemModel(name, data['price'], data['store_id'])
            item.save_to_db()
            return {"message": "New item is added!"}, 201

        # data = Item.parser.parse_args()
        # item_to_update = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        # if item_to_update:
        #     try:
        #         updated_item.update()
        #         return {"message": "item is updated!"}, 201
        #     except:
        #         return {"message": "Error occured!"}, 500
        # else:
        #     try:
        #         updated_item.insert()
        #         return {"message": "item is added!"}, 201
        #     except:
        #          return {"message": "Error occured!"}, 500

class ItemList(Resource):
    def get(self):
        return {'items': [i.json() for i in ItemModel.query.all()]}
        # conn = sqlite3.connect('data.db')
        # cursor = conn.cursor()
        # select_query = 'SELECT * FROM items'
        # result = cursor.execute(select_query)
        # items = result.fetchall()
        # conn.close()
        # if items:
        #     return {'items': items}