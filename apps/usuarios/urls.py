from django.conf.urls import url

from apps.usuarios.views import RegistroUsuario

from django.urls import path

app_name='usuarios'

urlpatterns = [
	path('registrar', RegistroUsuario.as_view(),name="registrar")
]