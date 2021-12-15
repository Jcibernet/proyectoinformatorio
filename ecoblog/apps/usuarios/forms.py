from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from .models import Rol 


class registroform(UserCreationForm):
	class Meta: 
		#roles=Rol.objects.all()
		#print(type(roles[0]))
		#user=Usuario()
		#user.setrol(roles[0])
		#Usuario.setrol(roles[0])
		model=Usuario
		fields= ['username', 'email', 'password1', 'password2']