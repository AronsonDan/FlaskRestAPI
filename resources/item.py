from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_current_user

from models.itemmodel import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        float,
                        required=True,
                        help="This field cannot be left blank!!!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id"
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {
                   'message': 'Item not found'
               }, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'An item with name {} already exists'.format(name)}, 400

        request_data = Item.parser.parse_args()
        item = ItemModel(name, **request_data)

        try:
            item.save_to_db()
        except:
            return {'message': 'an error occurred inserting the item'}, 500

        return item.json(), 201

    def delete(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': "item deleted"}

    @jwt_required()
    def put(self, name):
        print(get_current_user)
        request_data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        # create a new item
        if item is None:
            item = ItemModel(name, **request_data)
        else:
            item.price = request_data['price']
            item.store_id = request_data['store_id']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        items = [item.json() for item in ItemModel.query.all()]
        return {'Items': items}
