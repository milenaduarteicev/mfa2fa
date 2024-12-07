import unittest
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post('/login', data={'username': 'usuario1', 'password': 'senha_errada'})
        self.assertIn('Usuário ou senha inválidos', response.data.decode())

if __name__ == '__main__':
    unittest.main()
import unittest
from app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.post('/login', data={'username': 'usuario1', 'password': 'senha_errada'})
        self.assertIn('Usuário ou senha inválidos', response.data.decode())

if __name__ == '__main__':
    unittest.main()
