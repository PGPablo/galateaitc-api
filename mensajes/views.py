from .models import Mensajes
from .serializers import MensajesSerializer
from rest_framework import generics
import time

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.core.mail import EmailMessage

import random


class EnviarCorreo():
    correos = ["14030605@itcelaya.edu.mx", "14030598@itcelaya.edu.mx"]
    mensajes = ["Superate una y otra vez.",
     "Estudiar es lo mejor del mundo. ",
     "Eres el mejor estudiante que existe.",
     "Tu puedes dar mucho más.",
     "El esfuerzo vale la pena.",
     "Tu vas a llegar muy lejos.",
     "Eres excepcional.",
     "Eres muy bueno en lo que haces, pero puedes mejorar aún más.",
     "Yo confío en ti.",
     "Alguien como tu tiene un futuro brillante.",
     "Los retos que tienes enfrente para alguien como tu no son nada.",
     "Eres muy inteligente, aprovechalo.",
     "Relájate, vas a lograrlo.",
     "Tus fracasos son los cimientos de tus éxitos, sigue adelante.",
     "Sigue adelante.",]
    #
    #
    # while True:
    #     numeroDeMensaje = random.randrange(15)
    #     for correo in correos:
    #         print("hola")
    #         # email = EmailMessage(mensajes[numeroDeMensaje], mensajes[numeroDeMensaje], to=[correo])
    #         # email.send()
    #     time.sleep(30.0)


class MensajeList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Mensajes.objects.all()
    serializer_class = MensajesSerializer

class MensajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensajes.objects.all()
    serializer_class = MensajesSerializer
