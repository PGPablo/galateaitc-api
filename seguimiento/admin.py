from django.contrib import admin

from seguimiento.models import EncuestaDiaria, EncuestaInicial, EncuestaFinal

admin.site.register(EncuestaDiaria)
admin.site.register(EncuestaInicial)
admin.site.register(EncuestaFinal)
