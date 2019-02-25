#coding: utf8
from app import app, db
from flask import jsonify, json, request, render_template, redirect, url_for
from app.models.tables import Debit
from app.models.form import DebitForm
from datetime import datetime


@app.route('/v1/debit/new', methods=['POST'])
@app.route('/debit/new', methods=['POST'])
def add_debit():
    if str(request.url_rule) == "/debit/new":
        client_id = request.form['client_id']
        description = request.form['description']
        value = request.form['value']
        date = request.form['date']
        debit = Debit(int(client_id), description, float(value), date)
        db.session.add(debit)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        data = request.get_json()
        debit = Debit(int(data['client_id']), data['description'], float(data['value']), data['date'])
        db.session.add(debit)
        db.session.commit()
        return jsonify(data), 200


@app.route('/v1/debit/<int:debit_id>/edit', methods=['PUT'])
@app.route('/debit/<int:debit_id>/edit', methods=['GET', 'POST'])
def edit_debit(debit_id):
    debit = Debit.query.filter_by(id=debit_id).first()
    if str(request.url_rule) == "/debit/<int:debit_id>/edit":
        if request.method == 'GET':
            form = DebitForm(obj=debit)
            debits = Debit.query.all()
            return render_template('debit.html', form=form, action='edit', debits=debits, debit=debit)
        else:
            debit.description = request.form['description']
            debit.value = float(request.form['value'])
            debit.date = datetime.strptime(request.form['date'], '%Y-%m-%d')            
            db.session.add(debit)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        data = request.get_json()
        debit.client_id = data['client_id']
        debit.description = data['description']
        debit.value = float(data['value'])
        db.session.commit()
        debits = Debit.query.filter_by(id=debit_id).all()
        return jsonify([i.serialize for i in debits]), 201


@app.route('/v1/debit/<int:debit_id>', methods=['DELETE'])
@app.route('/debit/<int:debit_id>', methods=['POST'])
def delete_debit(debit_id):
    debit = Debit.query.filter_by(id=debit_id).first()
    db.session.delete(debit)
    db.session.commit()
    if str(request.url_rule) == "/debit/<int:debit_id>":    
        return redirect(url_for('index'))
    else:
        return list_debit()


@app.route('/', methods=["GET"])
def index():
    form = DebitForm()
    debits = Debit.query.all()
    return render_template('debit.html', form=form, action='add', debits=debits)


@app.route('/v1/debits', methods=['GET'])
def list_debit():
    debits = Debit.query.all()
    return jsonify([i.serialize for i in debits])


@app.route('/v1/debit/<int:debit_id>', methods=['GET'])
def search_debit_by_id(debit_id):
    debits = Debit.query.filter_by(id=debit_id).all()
    return jsonify([i.serialize for i in debits])
