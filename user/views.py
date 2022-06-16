from flask import Response, jsonify, request

from app import db
from . import user
from .models import User
from .schemas import UserSchema


users_schema = UserSchema(many=True)
user_schema = UserSchema()

@user.route('/user', methods=['GET'])
def list_users():
    users = User.query.all()
    
    return jsonify(users_schema.dump(users))

@user.route('/user/<int:user_id>', methods=['GET'])
def detail_user(user_id):
    user = User.query.get_or_404(user_id)

    return jsonify(user_schema.dump(user))


@user.route('/user', methods=['POST'])
def create_user():
    user = User(**request.json)
    db.session.add(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))

@user.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    user.name = request.json.get('name', '')
    user.email = request.json.get('email', '')
    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@user.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return Response(status=204)