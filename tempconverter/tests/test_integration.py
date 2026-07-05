import unittest
import requests

BASE_URL = "http://localhost:5000"

class TestAppIntegration(unittest.TestCase):

    def test_homepage_loads(self):
        r = requests.get(BASE_URL, timeout=5)
        self.assertEqual(r.status_code, 200)

    def test_homepage_contains_student(self):
        r = requests.get(BASE_URL, timeout=5)
        self.assertIn("Zvonimir", r.text)

    def test_homepage_contains_college(self):
        r = requests.get(BASE_URL, timeout=5)
        self.assertIn("Algebra", r.text)

    def test_html_title(self):
        r = requests.get(BASE_URL, timeout=5)
        self.assertIn("<title>Celsius to Fahrenheit Converter</title>", r.text)