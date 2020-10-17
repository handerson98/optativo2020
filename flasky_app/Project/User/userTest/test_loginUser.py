from Project.User.userTest.configTest import configTest
import Project.User.userTest.utils as utils
from Project.User.Models import User

class TestLogin(configTest):

    def test_login_user_void_field(self):
        data = utils.login_user_void_field()

        response = self.client.post(
            '/login_user',
            json=data
        )
        self.assertIn('email',data)
        self.assertIn('password',data)
        self.assertStatus(response, 400)


    def test_login_user_exist(self):
        dataLogin = utils.login_user_exist_user()
        dataRegister = utils.allUserData()

        #primero registrar un usuario
        response = self.client.post(
            '/register_user',
            json=dataRegister
        )
        self.assertStatus(response,201)
        self.assertEquals(User.query.count(),1)

        #ahora logear con ese
        response2 = self.client.post(
            '/login_user',
            json=dataLogin
        )

        self.assertEquals(dataLogin['email'],dataRegister['email'])
        self.assertEquals(dataLogin['password'],dataRegister['password'])
        self.assertStatus(response2,200)


    def test_login_user_no_exist(self):
        dataLogin = utils.login_user_exist_user()
        response = self.client.post(
            '/login_user',
            json=dataLogin
        )
        self.assertStatus(response,400)

    def test_login_user_fail_password(self):
        dataLogin = utils.login_user_fail_password()
        dataRegister = utils.allUserData()

        #primero registrar un usuario
        response = self.client.post(
            '/register_user',
            json=dataRegister
        )
        self.assertStatus(response,201)
        userCount = User.query.count()
        self.assertEquals(1,userCount)

        #ahora logear con ese
        response2 = self.client.post(
            '/login_user',
            json=dataLogin
        )
        userRegiter = User.query.filter_by(email=dataRegister['email']).first()

        self.assertNotEquals(userRegiter.password,dataLogin['password'])
        self.assertStatus(response2,400)



# que los campos ingresados no sean vacíos
#si es que existe la cuenta registrada
#
