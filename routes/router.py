from flask import Blueprint, request, redirect, jsonify
from flask.helpers import flash
from utils.db import db
from models.programming import Programming

programming = Blueprint('router', __name__)

@programming.route('/')
def index():
    try:
        data = Programming.query.all()
        list = []
        for i in data:
            file = {
                'id': i.id,
                'names': i.names,
                'description': i.description,
            }
            list.append(file)
        return jsonify({'programming': list})
    except Exception as e:
        return jsonify({'error': str(e)})

@programming.route('/<int:id>', methods=['GET'])
def get(id):
    try:
        data = Programming.query.get(id)
        if data != None:
            file = {
                'id': data.id,
                'names': data.names,
                'description': data.description,
            }
            return jsonify({'programming': file})
        else:
            return jsonify({'error': 'Programming not found'})
    except Exception as e:
        return jsonify({'error': str(e)})


@programming.route('/', methods=['POST'])
def create():
    try:
        json = request.get_json()
        if request.method == 'POST':
            names = json['names']
            description = json['description']
            data = Programming(names, description)
            db.session.add(data)
            db.session.commit()
            return jsonify({'programming': 'Programming created'})
    except Exception as e:
        return jsonify({'error': str(e)})

@programming.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        file = Programming.query.get(id)
        if file != None:
            json = request.get_json()
            if request.method == 'PUT':
                file.names = json['names']
                file.description = json['description']
                db.session.commit()
                return jsonify({'programming': 'Programming updated'})
        else:
            return jsonify({'error': 'Programming not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

@programming.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        file = Programming.query.get(id)
        if file != None:
            db.session.delete(file)
            db.session.commit()
            return jsonify({'programming': 'Programming deleted'})
        else:
            return jsonify({'error': 'Programming not found'})
    except Exception as e:
        return jsonify({'error': str(e)})