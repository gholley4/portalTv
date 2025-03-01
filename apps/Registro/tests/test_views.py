from django.test import TestCase
from django.test import Client

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La pagina raiz se carga correctamente"""
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

class ViewTest(TestCase):
    def test_requerimientos_url(self):
        c = Client()
        resp = c.get('http://localhost:8000/login/')
        self.assertEqual(resp.status_code, 200)
