import unittest
from app import login, app



class TestLogin(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # This test case pass.
    def test_login_success(self):
        username = 'admin'
        password = 'secret'
        response = self.app.post('/', data=dict(username=username, password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the dashboard!', response.data)

    def test_login_incorrect_input(self):
        username = '123'
        password = '456'
        response = self.app.post('/', data=dict(username=username, password=username), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)

    def test_login_incorrect_username(self):
        username = 'adminn'
        password = 'secret'
        response = self.app.post('/', data=dict(username=username, password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)

    def test_login_incorrect_password(self):
        username = 'admin'
        password = 'secrete'
        response = self.app.post('/', data=dict(username=username, password=password), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials', response.data)


if __name__ == 'main':
    unittest.main()
