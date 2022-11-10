from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse

#Unit test of creating a user
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'Bill')
        self.assertEqual(user.email, 'Bill@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

#Unit test of the Registration page

class RegisterPageTests(TestCase):
    # see https://docs.djangoproject.com/en/4.1/topics/testing/tools/
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

#Unit test of the Login page
class LoginPageTests(TestCase):
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
 
#Unit test of the account URL
class LoginPageTests(TestCase):
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)

#Unit test of the Player URL
class LoginPageTests(TestCase):
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('/player/')
        self.assertEqual(response.status_code, 200)


#Unit test of the empty string URL
class LoginPageTests(TestCase):
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

#Unit test of the edit URL
class LoginPageTests(TestCase):
    def setup(self):
        self.client  = Client()

    def test_register_template(self):
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 200)
