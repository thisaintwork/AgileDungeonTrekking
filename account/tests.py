from django.contrib.auth import get_user_model
from django.test import TestCase,Client
from django.urls import reverse
import re


class CreatUserTests(TestCase):
    """ Unit testing Custom User model """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='Mary Had a Little Lamb Whose Fleece was White as snow',
            email='mary had a little lamb@email.com',
            password='testpass123'
        )
        self.superuser = User.objects.create_superuser(
            username='adt_admin',
            email='admin@email.com',
            password='testpass123'
        )


    def test_create_user(self):
        """ Test creating a user is successful """
        self.assertEqual(self.user.username, 'Bill')
        self.assertEqual(self.user.email, 'Bill@email.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        self.assertEqual(self.user2.username, 'Mary Had a Little Lamb Whose Fleece was White as snow')
        self.assertEqual(self.user2.email, 'mary had a little lamb@email.com')
        self.assertTrue(self.user2.is_active)
        self.assertFalse(self.user2.is_staff)
        self.assertFalse(self.user2.is_superuser)

    def test_create_superuser(self):
        """ Test creating a super user is successful """
        self.assertEqual(self.superuser.username, 'adt_admin')
        self.assertEqual(self.superuser.email, 'admin@email.com')
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)


class UsernameValidationTests(TestCase):
    """ Unit testing Username validation """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='Mary Had a Little Lamb Whose Fleece was White as snow',
            email='mary had a little lamb@email.com',
            password='testpass123'
        )

    def test_username_validation(self):
        """ Test username follows rules """
        self.assertTrue(len(self.user.username) <= 30)
        self.assertTrue(len(self.user.username) > 0)


class EmailValidationTests(TestCase):
    """ Unit testing Username validation """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='Mary Had a Little Lamb Whose Fleece was White as snow',
            email='mary had a little lamb@email.com',
            password='testpass123'
        )

    def test_user_email_validation(self):
        """ Test user follows rules """
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        self.assertTrue(len(self.user.email) <= 30)
        self.assertTrue(len(self.user.email) > 0)
        self.assertTrue(re.fullmatch(regex, self.user.email))

        self.assertFalse(len(self.user2.email) <= 30)
        self.assertTrue(len(self.user2.email) > 0)
        self.assertFalse(re.fullmatch(regex, self.user2.email))


class PasswordValidationTests(TestCase):
    """ Unit testing password validation """
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )

    def test_password_validation(self):
        """ Test username follows rules """
        self.assertTrue(len(self.user.password) > 0)


class RegisterPageTests(TestCase):
    """ Unit test of the Registration page """
    def setUp(self):
        self.client  = Client()

    def test_register_template(self):
        """ Testing register page is accessible """
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)


class LoginPageTests(TestCase):
    """ Unit test of the Login page """
    def setUp(self):
        self.client  = Client()

    def test_login_template(self):
        """ Testing login page is accessible """
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


class ResetPasswordPageTests(TestCase):
    """ Unit test of the Reset Password page """

    def setUp(self):
        self.client = Client()

    def test_register_template(self):
        """ Testing reset password page is accessible """
        response = self.client.get('/password_reset/')
        self.assertEqual(response.status_code, 200)


class DashboardPageTests(TestCase):
    """ Unit test of the Dashboard  page """

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )

    def test_dashboard_template(self):
        """ Testing dashboard page is accessible """
        self.client.login(username='Bill', password='testpass123')
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class AdminPageTests(TestCase):
    """ Unit test of the Admin page """

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_superuser(
            username='adt_admin',
            email='admin@email.com',
            password='adt_admin'
        )
    def test_admin_template(self):
        """ Testing admin page is accessible """
        self.client.login(username='adt_admin', password='adt_admin')
        #url = reverse('admin/')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)


class InvalidLoginPageTests(TestCase):
    """ Unit test of the Login page """

    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Bill',
            email='Bill@email.com',
            password='testpass123'
        )

    def test_invalid_username(self):
        """ Testing invalid username entered """
        self.client.login(username='BillyBob', password='testpass123')
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


    def test_invalid_password(self):
        """ Testing invalid password entered """
        self.client.login(username='Billy', password='badpass123')
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


# Unit test of the edit URL
class EditPageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_register_template(self):
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 200)