from flask import Blueprint,request
import requests


renameBlueprints = Blueprint('rename',__name__)

@renameBlueprints.route('/',methods=['GET'])
def renameStatus():
    if request.method == 'GET':
        requestToFlaskyApp = requests.post(
            'http://flaskyapp:5000/login_user',
            json={ "email": "test@", "password":"test_password"}           ### DEBE EXISTIR ESTE USUARIO PARA QUE RESPONDA BIEN
        )
        if requestToFlaskyApp.status_code == 200:
            return "desde other_app: \n" + requestToFlaskyApp.text, 200
        return requestToFlaskyApp.text ,requestToFlaskyApp.status_code
    return 405
