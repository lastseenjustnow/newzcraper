from unittest import TestCase

from server import create_app


class TestFlask(TestCase):
    def test_home_page(self):
        app = create_app()

        with app.test_client() as app_test:
            response = app_test.get('/')

        self.assertTrue(200, response.status_code)
