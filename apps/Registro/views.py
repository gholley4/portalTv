from django.shortcuts import render
from .models import Pack

# Create your views here.

def listar_packs(request):
    packs = Pack.objects.all()
    return render(request, "Registro/listar_packs.html" , {'packs' : packs})
