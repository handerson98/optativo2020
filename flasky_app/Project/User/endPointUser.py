from flask import Blueprint, request, jsonify
from Project.User.Models import User
from Project import db
from Project.User.serializers import user_Schema, log_Schema
from Project.User.UserUtils import register_check_field_void, login_check_field_void

userBlueprint = Blueprint('User',__name__)

@userBlueprint.route('/register_user', methods=['POST'])
def createUser():
    if request.method == 'POST':
        userObject = user_Schema.load(request.get_json())
        if register_check_field_void(userObject) != 1:
            if User.query.filter_by(email = userObject.email).first() == None:   #si un usuario con ese correo no existe
                if userObject.password == userObject.confirmPassword:   #si las contraseñas coinciden
                    db.session.add(userObject)
                    db.session.commit()
                    return userObject.name+" se registrado con éxito", 201
                return jsonify("password do not match"), 400
            return "ya existe el usuario con ese correo", 409
        return "hay campos vacíos",400
    return 405



@userBlueprint.route('/login_user', methods=['POST'])
def logUser():
    if request.method == 'POST':
        log_User_Object = log_Schema.load(request.get_json())
        if login_check_field_void(log_User_Object) == 0:
            user_query = User.query.filter_by(email=log_User_Object.email).first()
            if user_query != None:   # si existe el registro
                if user_query.password == log_User_Object.password:  #si la contraseña coincide
                    users = User.query.all()
                    return jsonify(user_Schema.dump(users, many=True)) , 200
                return "contraseña incorrecta" , 400
            return "no existe el usuario", 400
        return "hay campos vacíos", 400
    return 405
