from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

# Create your tests here.

class BackendTestCase(TestCase):
    """ Test api """

    def setUp(self):
        pass

    def test_get_password(self):

        resquest = APIClient()
        response = resquest.get('/test/v1/getpassword', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_show_keys(self):

        resquest = APIClient()
        response = resquest.get('/test/v1/showkeys', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
