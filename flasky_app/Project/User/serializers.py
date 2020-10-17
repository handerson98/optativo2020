from Project.User.Models import User
from Project import marsh

class UserSchema(marsh.SQLAlchemyAutoSchema):
    class Meta():
        model = User
        load_instance = True
        load_only = ("id","password","confirmPassword","rut") # no dump

user_Schema = UserSchema()


class LogSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        #load_only = hay que asegurar que solo entren datos

#partial permite solo algunos campos
#unknown permitir campos que no existen en el modelo
#only permitir solo cargar los seleccionados cuando se crea el schema

log_Schema = LogSchema(partial=True, unknown=False, only=("email","password"))
