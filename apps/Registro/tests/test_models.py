from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Pack

class PackTestCase(TestCase):
    def setUp(self):
        Pack.objects.create(nombre="AAA", mensualidad=10000)
        Pack.objects.create(nombre="BBB", mensualidad=20000)

    def test_ingresar_packs(self):
        "Los packs se ingresan correctamente en la BD"
        pack_1 = Pack.objects.get(nombre="AAA")
        pack_2 = Pack.objects.get(nombre="BBB")
        self.assertEqual(pack_1.mensualidad, 10000)
        self.assertEqual(pack_2.mensualidad, 20000)     