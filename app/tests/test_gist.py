from flask import Flask
import unittest
from app import sample_bp

app = Flask(__name__)
app.register_blueprint(sample_bp, url_prefix='')


class TestGist(unittest.TestCase):
    def test_http_200(self):
        client = app.test_client()
        res = client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_http_404(self):
        client = app.test_client()
        res = client.get('/not_found')
        self.assertEqual(res.status_code, 404)

    def test_get_gist_200(self):
        client = app.test_client()
        res = client.get('/abc')
        self.assertEqual(res.status_code, 200)

    def test_get_gist_data(self):
        client = app.test_client()
        res = client.get('/abc')
        self.assertEqual(res.json[0]['owner']['login'], 'abc')


if __name__ == "__main__":
    unittest.main()
