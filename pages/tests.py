from django.test import TestCase

# Create your tests here.
from django.db import reset_queries
from django.http import response
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model, login
from  accounts.models import CustomUser
# Create your tests here.
class test_custom_user(TestCase):
    def setUp(self):
        self.account=get_user_model().objects.create_user(
            username='usernameTest',
            email='email@gmail.com',
            password='usernameTest123456789'
        )
    def test_signup(self):
        url=reverse('signup')
        response=self.client.post(url,{
            'email':'usernameTest',
            'password':'usernameTest123456789'
        },follow=True)
        self.assertEqual(response.status_code,405)
    def test_login(self):
        url = reverse('login')
        actual_status_code = self.client.get(url).status_code
        self.assertEqual(actual_status_code, 200)