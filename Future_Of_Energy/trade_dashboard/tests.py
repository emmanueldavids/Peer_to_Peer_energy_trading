import unittest
from django.test import TestCase, Client

""" All unit Test Case for the trade Dashboard application """


class checkPath(unittest.TestCase):
    """This unit test case validates all the define paths in the app"""

    def setUp(self):
        # setup for the client
        self.client = Client()

    
    def test_all_path(self):
        # issuing a GET request
        urls = [
        '/',
        '/dashboard/trade',
        '/dashboard/alert',
        '/dashboard/sell',
        '/dashboard/feeds', 
        '/dashboard/wallet', 
        '/dashboard/transactions'
        ]

        for url in urls:
            response = self.client.get(url)

        # check the response status code is 200
        self.assertEqual(response.status_code, 200)
    

   