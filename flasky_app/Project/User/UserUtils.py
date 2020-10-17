def register_check_field_void(data):
    if data.name == "" or data.surname == "" or data.email == "" or data.rut == "" or data.age == "" or data.city == "" or data.password == "" or data.confirmPassword == "":
        return 1
    else:
        return 0

def login_check_field_void(data):
    if data.email == "" or data.password == "":
        return 1
    return 0
