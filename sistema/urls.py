from django.urls import path
from sistema import views
from .views import login_view, logout_view, register_view


urlpatterns = [
    path('', views.main_view, name='index'),
    path('main/', views.index, name='main'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'), 
    path('exit/', views.exit, name = 'exit'),
]