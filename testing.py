import unittest
from flask import url_for
from app import login, app

class TestLogin(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_login_empty_input(self):
        username = ''
        password = ''
        response = self.app.post('/', data=dict(username=username, password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)

    def test_login_empty_username(client):
        username = 'admin'
        password = ''
        response = client.post('/', data=dict(username=username, password=password), follow_redirects=True)
        assert response.status_code == 200
        assert b'Invalid credentials' in response.data

    def test_login_non_existent_username(client):
        username = ''
        password = 'secret'
        response = client.post('/', data=dict(username=username, password=password) follow_redirects=True)
        assert response.status_code == 200
        assert b'Invalid credentials' in response.data

    def test_login_correct_password(client):
        username = 'admin'
        password = 'secret'
        response = client.post('/', data=dict(username=username, password=password) follow_redirects=True)
        assert response.status_code == 200
        assert b'Welcome to the Dashboard!' in response.data

if __name__ == '__main__':
    unittest.main()
