from .models import EncuestaDiaria, EncuestaInicial, EncuestaFinal
from rest_framework import serializers

class EncuestaDiariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = EncuestaDiaria
    fields = '__all__'

class EncuestaInicialSerializer(serializers.ModelSerializer):
  class Meta:
    model = EncuestaInicial
    fields = '__all__'

class EncuestaFinalSerializer(serializers.ModelSerializer):
  class Meta:
    model = EncuestaFinal
    fields = '__all__'
