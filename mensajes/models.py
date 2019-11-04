from django.db import models

class Mensajes(models.Model):
  Mensaje = models.CharField(max_length=500)
