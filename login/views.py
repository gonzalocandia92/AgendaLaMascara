from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request, 'login/home.html')

@login_required
def products(request):
    return render(request, 'login/products.html')

def exit(request):
    logout(request)
    return redirect('index')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            # Recupera datos del formulario para luego loguearlo, luego lo envía al inicio
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        
    return render(request, 'registration/register.html', data)