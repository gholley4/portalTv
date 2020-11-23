from django.test import TestCase
from apps.Registro.models import Pack
from apps.Registro.forms import PackForm

class PackFormCase(TestCase):

    def test_valid_form(self):
        pack = Pack.objects.create(nombre="ORO HD", mensualidad=20000 )
        data = {'nombre': pack.nombre, 'mensualidad': pack.mensualidad }
        form = PackForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        pack = Pack.objects.create(nombre='', mensualidad=200000)
        data = {'nombre': pack.nombre, 'mensualidad': pack.mensualidad, }
        form = PackForm(data=data)
        self.assertFalse(form.is_valid())
    