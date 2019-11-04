from .models import EncuestaDiaria, EncuestaInicial, EncuestaFinal
from .serializers import EncuestaDiariaSerializer, EncuestaInicialSerializer, EncuestaFinalSerializer
from rest_framework import generics

#EncuestaDiaria
class EncuestaDiariaList(generics.ListCreateAPIView):
    queryset = EncuestaDiaria.objects.all()
    serializer_class = EncuestaDiariaSerializer

class EncuestaDiariaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EncuestaDiaria.objects.all()
    serializer_class = EncuestaDiariaSerializer


#EncuestaInicial
class EncuestaInicialList(generics.ListCreateAPIView):
    queryset = EncuestaInicial.objects.all()
    serializer_class = EncuestaInicialSerializer

class EncuestaInicialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EncuestaInicial.objects.all()
    serializer_class = EncuestaInicialSerializer


#EncuestaFinal
class EncuestaFinalList(generics.ListCreateAPIView):
    queryset = EncuestaFinal.objects.all()
    serializer_class = EncuestaFinalSerializer

class EncuestaFinalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EncuestaFinal.objects.all()
    serializer_class = EncuestaFinalSerializer
