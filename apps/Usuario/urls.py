from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Usuario import views

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registrar_usuario" ),
    path('listar', UserList.as_view(), name="list_user"),
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
