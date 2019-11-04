from django.contrib import admin
from django.urls import path, include

from django.config import settings
from django.config.urls.static import static

from rest_framework import routers
from mensajes import views as mensajesViews
from seguimiento import views as encuestaViews

urlpatterns = [
#Mensajes
  path('api/Mensajes/', mensajesViews.MensajeList.as_view()),
#Seguimiento
  path('api/EncuestaDiariaList/', encuestaViews.EncuestaDiariaList.as_view()),
  path('api/EncuestaInicialList/', encuestaViews.EncuestaInicialList.as_view()),
  path('api/EncuestaFinalList/', encuestaViews.EncuestaFinalList.as_view()),
 #Admin
  path('admin/', admin.site.urls),

 #Auth
 path('api/auth/',
  include('rest_auth.urls')),
 path('api/auth/registration/',
  include('rest_auth.registration.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
