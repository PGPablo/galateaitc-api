from .models import Mensajes
from rest_framework import serializers

class MensajesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mensajes
    fields = '__all__'
