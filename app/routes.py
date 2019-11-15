# -*- coding: utf-8 -*-
import os
import uuid
from flask import render_template, flash, redirect, jsonify
from app import app, db
from app.forms import AddUserForm
from app.models import User
from werkzeug.utils import secure_filename



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        image = form.photo.data
        uid = uuid.uuid4()
        filename = '.'.join([str(uid), 'jpg'])
        image.save(os.path.join(
            os.getcwd(), 'photos', filename
        ))
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, uid=str(uid))
        db.session.add(new_user)
        db.session.commit()
        flash('Login requested for user {}'.format(form.first_name.data))
        return redirect('/index')
    return render_template('add_user.html', title='Add New User', form=form)


@app.route('/user/<int:user_id>')
def user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    photo_name = '.'.join([user.uid, 'jpg'])
    return render_template('user.html', user=user, photo=photo_name)


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/api/user/<int:user_id>', methods=['GET'])
def api_user(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    required_user = {'id': user.id, 'uid': user.uid, 'first_name': user.first_name,
                     'last_name': user.last_name, 'image': '.'.join([user.uid, 'jpg'])}
    return jsonify({'user': required_user})


@app.route('/api/users', methods=['GET'])
def api_users():
    users_list = []
    users = User.query.all()
    for user in users:
        users_list.append({'id': user.id, 'first_name': user.first_name,
                           'last_name': user.last_name, 'image': '.'.join([user.uid, 'jpg'])})
    return jsonify({'users': users_list})
