from django.db import models
from django.contrib.auth.models import User

class AplicacionesMóvilesParaIot(models.Model):
    nombre_asignatura = models.CharField(max_length=100, default="Aplicaciones Móviles Para Iot")
    horas_asistidas = models.IntegerField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

    def __str__(self):
        return f"{self.nombre_asignatura} - {self.alumno.username} - {self.horas_asistidas} horas - {self.fecha_clase}"

class IngenieríaDeSoftware(models.Model):
    nombre_asignatura = models.CharField(max_length=100, default="Ingeniería De Software")
    horas_asistidas = models.IntegerField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

    def __str__(self):
        return f"{self.nombre_asignatura} - {self.alumno.username} - {self.horas_asistidas} horas - {self.fecha_clase}"

class ProgramaciónBackEnd(models.Model):
    nombre_asignatura = models.CharField(max_length=100, default="Programación Back End")
    horas_asistidas = models.IntegerField()
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_clase = models.DateField()

    def __str__(self):
        return f"{self.nombre_asignatura} - {self.alumno.username} - {self.horas_asistidas} horas - {self.fecha_clase}"
