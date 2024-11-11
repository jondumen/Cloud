from django.contrib import admin
from .models import Habitacion, Reserva, Cliente, Informe
from .forms import HabitacionForm, ReservaForm, ClienteForm, InformeForm

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    form = HabitacionForm

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    form = ReservaForm

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm

@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    form = InformeForm
