from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Habitacion, Reserva, Cliente
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)    
            if user.is_staff:
                return redirect('main')  # Redirigir a la página de staff
            else:
                return redirect('index')  # Redirigir a la página de usuario regular
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'sistema/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def exit(request):
    logout (request)
    return redirect('index')

def register_view(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login (request, user)

            return redirect('index')

    return render(request, 'sistema/register.html', data)

def index(request):
    return render(request, 'sistema/index.html', )


def main_view(request):

    bebida_1 = {
        "titulo": "Americano",
        "descripcion": "Suavidad y carácter en cada sorbo.",
    }

    bebida_2 = {
        "titulo": "Capuccino",
        "descripcion": "La perfección del equilibrio.",
    }

    bebida_3 = {
        "titulo": "Espresso",
        "descripcion": "La esencia pura del café.",
    }

    bebida_4 = {
        "titulo": "Frappe",
        "descripcion": "Simple y divertido.",
    }

    bebida_5 = {
        "titulo": "Tisana",
        "descripcion": "Un abrazo de calma en cada infusión.",
    }

    bebida_6 = {
        "titulo": "Matcha",
        "descripcion": "El equilibrio entre suavidad y vitalidad.",
    }

    alimento_1 = {
        "titulo": "Pan Frances",
        "descripcion": "Pan brioche bañado en huevo, vainilla y canela con un toque frutal.",
    }

    alimento_2 = {
        "titulo": "Bagel Mañanero",
        "descripcion": "Bagel con huevo, tocino y jamón.",
    }

    alimento_3 = {
        "titulo": "Avocado Toast",
        "descripcion": "Aguacate y huevo en una cama de pan tostado.",
    }

    alimento_4 = {
        "titulo": "Rol de Canela",
        "descripcion": "Nuestros deliciosos roles especiales de la casa.",
    }

    alimento_5 = {
        "titulo": "Crossaint con Huevito",
        "descripcion": "Crossanit con huevo, jamón y queso.",
    }

    alimento_6 = {
        "titulo": "Galleta de chispas",
        "descripcion": "La original y favorita de todos.",
    }

    return render(request, 'sistema/main.html', {
        'bebida_1': bebida_1,
        'bebida_2': bebida_2,
        'bebida_3': bebida_3,
        'bebida_4': bebida_4,
        'bebida_5': bebida_5,
        'bebida_6': bebida_6,
        'alimento_1': alimento_1,
        'alimento_2': alimento_2,
        'alimento_3': alimento_3,
        'alimento_4': alimento_4,
        'alimento_5': alimento_5,
        'alimento_6': alimento_6,
    })
