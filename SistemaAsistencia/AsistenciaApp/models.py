from django.db import models
from django.contrib.auth.models import User

class Matematicas(models.Model):
    nombre = models.CharField(max_length=100, default="Matemáticas")
    horas_teoricas = models.IntegerField()
    horas_practicas = models.IntegerField()
    horas_totales = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.horas_totales = self.horas_teoricas + self.horas_practicas
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.horas_totales} horas"

class Lenguaje(models.Model):
    nombre = models.CharField(max_length=100, default="Lenguaje")
    horas_lectura = models.IntegerField()
    horas_escritura = models.IntegerField()
    horas_totales = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.horas_totales = self.horas_lectura + self.horas_escritura
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.horas_totales} horas"

class Ciencias(models.Model):
    nombre = models.CharField(max_length=100, default="Ciencias")
    horas_laboratorio = models.IntegerField()
    horas_teoria = models.IntegerField()
    horas_totales = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.horas_totales = self.horas_laboratorio + self.horas_teoria
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.horas_totales} horas"
