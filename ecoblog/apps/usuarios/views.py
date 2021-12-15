#from django.shortcuts import render

from django.contrib.auth.models import User
from .forms import registroform
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegistroUsuario(CreateView):
	model = User
	template_name = "auth/register.html"
	form_class = registroform
	success_url = reverse_lazy('inicio')
