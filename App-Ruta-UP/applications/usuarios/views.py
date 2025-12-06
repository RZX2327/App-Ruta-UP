from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import RegistroForm  
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})



