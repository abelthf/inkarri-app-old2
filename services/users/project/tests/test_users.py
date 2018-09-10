import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests para el servicio Users."""

    def test_users(self):
        """Nos aseguramos que la ruta localhost:5001/users/ping esta funcionando correctamente."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!!!', data['mensaje'])
        self.assertIn('satisfactorio', data['estado'])


if __name__ == '__main__':
    unittest.main()