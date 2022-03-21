from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Rol 
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms


class registroform(UserCreationForm):
	
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'max-width: 300px;', 'placeholder': 'Ingrese su Nombre de Usuario'}))
	email= forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'style': 'max-width: 300px;', 'placeholder': 'ejemplo@gmail.com'}))
	password1= forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 300px;', 'placeholder': 'Ingrese su Contraseña'}))
	password2= forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 300px;', 'placeholder': 'Ingrese su Contraseña'}))
	
	class Meta: 
		#roles=Rol.objects.all()
		#print(type(roles[0]))
		#user=Usuario()
		#user.setrol(roles[0])
		#Usuario.setrol(roles[0])
		model=Usuario
		fields= ['username', 'email', 'password1', 'password2']

		

	def __init__(self, *args, **kwargs):
		super(registroform, self).__init__(*args, **kwargs)

		#self.fields['username'].widget.attrs['class']= 'form-control'
		#self.fields['password1'].widget.attrs['class']= 'form-control'
		#self.fields['password2'].widget.attrs['class']= 'form-control'





		
	