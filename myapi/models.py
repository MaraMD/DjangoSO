from django.db import models


class Carrera(models.Model):        
    nombre_carrera = models.CharField(max_length=60)
    erase = models.BooleanField(default = False)


class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    edad = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60)
    direccion = models.TextField(max_length=1000)
    carrera = models.ForeignKey(Carrera, related_name='alumnos', on_delete=models.CASCADE)#null=false
    erase = models.BooleanField(default = False)
    


