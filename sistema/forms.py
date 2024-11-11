from django import forms
from .models import Habitacion, Reserva, Cliente, Informe
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
