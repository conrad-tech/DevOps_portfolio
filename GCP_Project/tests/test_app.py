# test_app.py

import unittest
import app
import tempfile
import os

class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    # def test_home_redirects_to_login(self):
    #   response = self.app.get('/')
    #   self.assertEqual(response.status_code, 302)
    #   self.assertEqual(response.headers['Location'], '/login')

    # def test_login_with_valid_credentials(self):
    #   response = self.app.post('/login/', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
    #   self.assertIn(b'Welcome, testuser!', response.data)

    def test_login_with_invalid_credentials(self):
        response = self.app.post('/login/', data={'username': 'testuser', 'password': 'wrongpassword'}, follow_redirects=True)
        self.assertIn(b'Incorrect username/password', response.data)

    # def test_registration_with_valid_data(self):
    #   response = self.app.post('/register', data={'fullname': 'Test User', 'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'}, follow_redirects=True)
    #   self.assertIn(b'You have successfully registered!', response.data)

    def test_registration_with_existing_username(self):
        response = self.app.post('/register', data={'fullname': 'Test User', 'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'}, follow_redirects=True)
        response = self.app.post('/register', data={'fullname': 'Test User 2', 'username': 'testuser', 'password': 'testpassword2', 'email': 'test2@example.com'}, follow_redirects=True)
        self.assertIn(b'Account already exists!', response.data)

if __name__ == '__main__':
    unittest.main()
