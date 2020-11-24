from django.urls import path
from . import views
from .views import SearchResultsView, BuscarPacksView

urlpatterns = [
    
    # listar los packs de la bd
    path('list_packs', views.PackList.as_view(), name="list_packs"),
    path('agregar_pack', views.agregar_pack, name="agregar_pack"),
    path('editar_pack/<int:carrera_id>', views.editar_pack, name="editar_pack"),
    path('borrar_pack/<int:carrera_id>', views.borrar_pack, name="borrar_pack"),
    path('pack_form', views.PackCreate.as_view(), name="pack_form"),
    path('buscar/', BuscarPacksView.as_view(), name='buscar_packs'),
    path('search/', SearchResultsView.as_view(), name= 'search_results'),

    # api
    path('packs/', views.pack_collection, name='pack_collection'),
    path('packs/<int:pk>/', views.pack_element, name='pack_element'),


]

