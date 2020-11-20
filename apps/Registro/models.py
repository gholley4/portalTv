from django.db import models

# Create your models here.
class Pack(models.Model):
    nombre = models.CharField(max_length=20)
    mensualidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):        
    pack = models.ForeignKey(Pack, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
    