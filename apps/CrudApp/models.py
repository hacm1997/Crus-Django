from django.db import models

# Modelo Servicio.
class Servicio(models.Model):
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    hora_atencion = models.CharField(null=True, blank=False, max_length=20)
    hora_final_atencion = models.CharField(null=True, blank=False, max_length=20)
    empresa = models.CharField(null=True, blank=False, max_length=50)
    ciudad = models.CharField(null=True, blank=False, max_length=50)
    asunto = models.CharField(null=True, blank=False, max_length=70)
    respuesta = models.CharField(null=True, blank=False, max_length=70)
    fecha_solicitud = models.DateField(auto_now=False, auto_now_add=False)