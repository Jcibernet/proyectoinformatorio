from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [

    path('', views.Login, name="login"),
    path('registrarse/', views.Register, name="register")
    
]