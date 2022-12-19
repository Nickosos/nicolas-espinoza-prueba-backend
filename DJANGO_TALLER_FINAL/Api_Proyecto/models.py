from unittest.util import _MAX_LENGTH
from django.db import models
from .opciones import lista


# modelo institucion
class Institucion(models.Model):
    institucion = models.CharField(max_length=50)
    def __str__ (self):
        return self.institucion
#modelo inscitos
class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechainscripción = models.DateField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE )
    horainscripcion= models.TimeField()
    estados = models.CharField(max_length=100, choices=lista)
    observacion = models.CharField(max_length=100, blank=True)
    


    


    