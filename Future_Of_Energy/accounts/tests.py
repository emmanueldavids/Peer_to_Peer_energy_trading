from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from .views import signin, register
from django.test import TestCase, Client
from dotenv import load_dotenv
import os
import unittest


""" All unit Test Cases for user Authentication """

# load the environment variables
load_dotenv()

class checkPath(unittest.TestCase):
    """This unit test case validates all the define paths in the app"""

    def setUp(self):
        # setup for the client
        self.client = Client()

    
    def test_account_path(self):
        # issuing a GET request
        urls = [
        '/',
        '/accounts/register'
        ]

        for url in urls:
            response = self.client.get(url)

        # check the response status code is 200
        self.assertEqual(response.status_code, 200)
    


# class Validate_Account(TestCase):
#     """This test case is to validate the user signin and register authentication methods """

#     def setUp(self):
#         # create a new request factory instance
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username=os.environ.get('TESTUSR'),
#             email=os.environ.get('TESTEMAIL'),
#             password=os.environ.get('TESTPWD')
#         )

#     def test_user_creation(self):
#         # create an instance of a GET request
#         get_url = self.factory.get('/account/register')

#         #simulate a login user
#         get_url.user = self.user

#         # Test the register method in views
#         response = register(get_url)

#         self.assertEqual(response.status_code, 200)