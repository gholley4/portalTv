from django.urls import path
from . import views

urlpatterns = [
    
    # listar los packs de la bd
    path('list_packs', views.PackList.as_view(), name="list_packs"),
    path('agregar_pack', views.agregar_pack, name="agregar_pack"),
    path('editar_pack/<int:carrera_id>', views.editar_pack, name="editar_pack"),
    path('borrar_pack/<int:carrera_id>', views.borrar_pack, name="borrar_pack"),
    path('add_pack', views.PackCreate.as_view(), name="add_pack"),

]

