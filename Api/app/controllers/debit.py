#coding: utf8
from app import app, db
from flask import jsonify, json, request
from app.models.tables import Debit

@app.route('/v1/debit/new', methods=['POST'])
def add_debit():
    data = request.get_json()
    debit = Debit(int(data['client_id']), data['client_name'], data['description'], float(data['value']))
    db.session.add(debit)
    db.session.commit()
    return jsonify(data), 200

@app.route('/v1/debit/<int:debit_id>', methods=['GET'])
def search_debit_by_id(debit_id):
    debits = Debit.query.filter_by(id=debit_id).all()
    return jsonify([i.serialize for i in debits])

@app.route('/v1/debit/<int:debit_id>/edit', methods=['PUT'])
def edit_debit(debit_id):
    debit = Debit.query.filter_by(id=debit_id).first()
    data = request.get_json()
    debit.client_id = int(data['client_id'])
    debit.client_name = data['client_name']
    debit.description = data['description']
    debit.value = float(data['value'])
    db.session.commit()
    debits = Debit.query.filter_by(id=debit_id).all()
    return jsonify([i.serialize for i in debits]), 201

@app.route('/v1/debit/<int:debit_id>', methods=['DELETE'])
def delete_debit(debit_id):
    debit = Debit.query.filter_by(id=debit_id).first()
    db.session.delete(debit)
    db.session.commit()
    return list_debit()

@app.route('/v1/debits', methods=['GET'])
def list_debit():
    debits = Debit.query.all()
    return jsonify([i.serialize for i in debits])
    