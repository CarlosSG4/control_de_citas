from django.db import models
from django.utils import timezone


class perfil(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    apellidos = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    curp = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    celular = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    consultorio = models.CharField(max_length=200)
    medico = models.CharField(max_length=200)
    turno = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title