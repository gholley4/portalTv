from django.urls import path
from . import views

urlpatterns = [
    
    # listar los packs de la bd
    path('listarPacks', views.listar_packs, name="listar_packs"),
    path('agregar_pack', views.agregar_pack, name="agregar_pack"),
    path('editar_pack/<int:carrera_id>', views.editar_pack, name="editar_pack"),
    path('borrar_pack/<int:carrera_id>', views.borrar_pack, name="borrar_pack"),

]

