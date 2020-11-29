"""Importaciones"""
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import generics
from .forms import RegistroForm
from .serializers import UsuarioSerializer

# Create your views here.

class RegistroUsuario(CreateView):
    """Clase para registrar un usuario nuevo en la base de datos"""
    model = User
    template_name = "Usuario/registrar_usuario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('list_user')

class UserList(ListView): # pylint: disable=too-many-ancestors
    """Clase para listar los usuarios guardados en la base de datos"""
    model = User
    template_name = 'Usuario/list_user.html'

class API_objects(generics.ListCreateAPIView): 
    """Clase para crear una apiview nueva"""
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    """Clase Para poder ver los contenidos de la api"""
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer    