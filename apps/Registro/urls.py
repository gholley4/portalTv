from django.urls import path
from . import views

urlpatterns = [
    
    # listar los packs de la bd
    path('listarPacks', views.listar_packs, name="listar_packs"),

]

