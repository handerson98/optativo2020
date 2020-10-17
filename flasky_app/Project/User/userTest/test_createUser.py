import Project.User.userTest.utils as utils
from Project.User.serializers import user_Schema
from Project.User.Models import User
from Project.User.userTest.configTest import configTest

class TestCreate(configTest):

    def test_register_user(self):
        data = utils.allUserData()
        response = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response,201)
        userCount = User.query.count()
        self.assertEquals(1,userCount)



    def test_register_user_no_data(self):
        data = {}
        response = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response,400)


    def test_register_user_add_keys(self):
        data = utils.add_keys_to_data()
        response = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response,400)
        self.assertEquals(response.get_json(),{'lastname': ['Unknown field.']})


    def test_register_user_diff_password(self):
        data = utils.diff_password()
        response = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response,400) #status
        self.assertEquals(response.get_json() , 'password do not match') #string coherente


    def test_register_user_void_fields(self):
        data = utils.void_fields()
        response = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response,400)


    def test_register_user_already_exist(self):

        ### insert user
        data = utils.allUserData()
        response1 = self.client.post(
            '/register_user',
            json=data
        )
        self.assertStatus(response1,201)
        preCountUsers = User.query.count()

        ### insert user again
        response2 = self.client.post(
            '/register_user',
            json=data
        )
        proCountUser = User.query.count() ### para comprobar que no se haya ingresado
        #el correo debe ser único
        self.assertEquals(preCountUsers,proCountUser)  ##comprueba que no se haya ingresado el dato
        self.assertStatus(response2,409)




    #ideal
    #ningún dato
    #que le ingrese otras keys
    #contraseñas diferentes
    #campos vacíos
    #existencia de ese usuario

    #*** primero comprobar si existen las keys
