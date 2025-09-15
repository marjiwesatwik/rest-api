import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
 
from schemas import StoreSchema
from models import StoreModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt
blp=Blueprint("Stores",__name__,description="Operations on stores")



@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @jwt_required()
    @blp.response(200,StoreSchema)
    def get(self,store_id):      
        store=StoreModel.query.get_or_404(store_id)
        return store

    @jwt_required()
    def delete(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("Delete method not implemented yet")

    @jwt_required()
    @blp.arguments(StoreSchema)        
    def put(self,store_data,store_id):
        
        
        store=StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("PUT  method not implemented yet")
    

@blp.route("/store")
class StoreList(MethodView): 
    @jwt_required()
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()
        
    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(201,StoreSchema)
    def post(self,store_data):
        
        store=StoreModel(**store_data)

        try:
            db.session.add(store)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="An error occurred while inserting the item.")
        except IntegrityError:
            abort(400,message="A store with that name already exists.")
        return store
