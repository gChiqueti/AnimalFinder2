from django.test import TestCase
from .models import Dono
from django.test import Client
# Create your tests here.
class DonoTest(TestCase):
    def setUp(self):
        self.dono = Dono()
        self.dono.email='test@gmail.com'
        self.dono.telefone=14999998888
        self.dono.nome='Testador'
        self.dono.password='teste'
        self.dono.save()

    def test_dono_fields(self):
        record = Dono.objects.get(pk=self.dono.id)
        self.assertEqual(record, self.dono)
