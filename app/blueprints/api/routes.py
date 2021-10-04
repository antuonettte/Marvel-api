from app.blueprints.auth.models import User
from .import bp as api
from flask import jsonify, request
from app import db
from app.blueprints.main.models import MarvelCharacter
import json

@api.route('/characters', methods=['GET'])
def get_Characters():
    """
    [GET] /api/characters
    """
    characters = [m.to_dict() for m in MarvelCharacter.query.all()]
    return jsonify(characters)

# @api.route('/characters/<id>', methods=['GET'])
# def get_Characters():
#     """
#     [GET] /api/characters
#     """
#     characters = [m.to_dict() for m in MarvelCharacter.query.all()]
#     return jsonify(characters)

@api.route('/character/<id>', methods=['GET'])
def get_Character(id):
    """
    [GET] /api/character/<id>
    """
    return jsonify(MarvelCharacter.query.get_or_404(id).to_dict())

# @api.route('/addcharacter/<id>', methods=['Post'])
# def add_Character(id):
    
#     """
#     [GET] /api/character/<id>
#     """

#     return jsonify(MarvelCharacter.query.get_or_404(id).to_dict())