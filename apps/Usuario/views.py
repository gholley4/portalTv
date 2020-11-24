from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm
from rest_framework import generics
from .serializers import UsuarioSerializer

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/registrar_usuario.html"
    form_class = RegistroForm
    success_url = reverse_lazy('list_user')

class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'

class API_objects(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer    