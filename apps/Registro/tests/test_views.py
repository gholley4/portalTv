from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La pagina raiz se carga correctamente"""
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 404)