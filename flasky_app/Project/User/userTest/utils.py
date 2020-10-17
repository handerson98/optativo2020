
def allUserData():
    data={
        "name":"test_name",
        "surname":"test_surname",
        "email":"test@",
        "rut":"123124343-7",
        "age":22,
        "city":"test_city",
        "password":"test_password",
        "confirmPassword":"test_password"
        }
    return data


def add_keys_to_data():
    data={
        "name":"test_name",
        "surname":"test_surname",
        "email":"test@",
        "lastname":"test_lastname", ###
        "rut":"123232-l",
        "age":22,
        "city":"test_city",
        "password":"test_password",
        "confirmPassword":"test_password"
        }
    return data

def diff_password():
    data={
        "name":"test_name",
        "surname":"test_surname",
        "email":"test@",
        "rut":"43243241-8",
        "age":22,
        "city":"test_city",
        "password":"test_password",
        "confirmPassword":"test_diff_password"
        }
    return data


def void_fields():
    data={
        "name":"",
        "surname":"test_surname",
        "email":"",
        "rut":"",
        "age":0,
        "city":"test_city",
        "password":"",
        "confirmPassword":""
        }
    return data

def alreary_exist_Data():
    data={
        "name":"test_name",
        "surname":"test_surname",
        "email":"equal_email@",
        "rut":"12318983-7",
        "age":22,
        "city":"test_city",
        "password":"test_password",
        "confirmPassword":"test_password"
        }
    return data

def login_user_void_field():
    data = {
        "email": "",
        "password": ""
    }
    return data

def login_user_exist_user():
    data = {
        "email":"test@",
        "password":"test_password"
    }
    return data

def login_user_fail_password():
    data = {
        "email": "test@",
        "password": "fail_password"
    }
    return data
