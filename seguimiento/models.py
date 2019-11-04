from django.db import models

ACPTACION = [
  ('MB', 'Muy bien'),
  ('B', 'Bien'),
  ('R', 'Regular'),
  ('M', 'Mal'),
  ('MM', 'Muy mal'),
]

class EncuestaDiaria(models.Model):
    Usuario = models.CharField(max_length=150)
    pregunta_1 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_2 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_3 = models.CharField(max_length=10, choices=ACPTACION)

class EncuestaInicial(models.Model):
    Usuario = models.CharField(max_length=150)
    pregunta_1 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_2 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_3 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_4 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_5 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_6 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_7 = models.BooleanField(default=False)
    pregunta_8 = models.BooleanField(default=False)
    pregunta_9 = models.BooleanField(default=False)

class EncuestaFinal(models.Model):
    Usuario = models.CharField(max_length=150)
    pregunta_1 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_2 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_3 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_4 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_5 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_6 = models.CharField(max_length=10, choices=ACPTACION)
    pregunta_7 = models.BooleanField(default=False)
    pregunta_8 = models.BooleanField(default=False)
    pregunta_9 = models.BooleanField(default=False)
    pregunta_10 = models.BooleanField(default=False)
    pregunta_11 = models.BooleanField(default=False)
