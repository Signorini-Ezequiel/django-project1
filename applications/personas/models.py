from django.db import models

#  Create your models here.
class Personas(models.Model): #  Modelo del tipo modelo
    nombres = models.CharField('Nombre y apellido', max_length=120) #  Descripción y largo de caracteres
    dni = models.CharField('Número de DNI', max_length=8)
    telefono = models.CharField('teléfono', max_length=100)
    correo_electronico = models.CharField('Correo electrónico', max_length=200)
    curso = models.CharField('Curso', max_length=10)

class ListAllPersonas(models.Model):
    nombres = models.CharField("Nombres", max_length=40)
    apellido = models.CharField("Apellido", max_length=40)
    # departamento =   ¿¿ Cómo se incluye ??