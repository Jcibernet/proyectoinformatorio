from django.shortcuts import render

# Create your views here.
def Login(request):

    return render(request, 'auth/login.html')

def Register(request):

    return render(request, 'auth/register.html')