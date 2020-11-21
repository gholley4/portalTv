from django.shortcuts import render
from .models import Pack
from .forms import PackForm

# Create your views here.

def listar_packs(request):
    packs = Pack.objects.all()
    return render(request, "Registro/listar_packs.html" , {'packs' : packs})

def agregar_pack(request):
    if request.method == "POST":
        form = PackForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect ("/agregar_pack")
    else:
        form = PackForm()
        return render(request, "Registro/agregar_pack.html", {'form': form})

def borrar_pack(request, pack_id):
    instancia = Pack.objects.get(id=pack_id)
    instancia.delete()

    return redirect ('listar_packs')

def editar_pack(request, pack_id):
    instancia = Pack.objects.get(id=pack_id)

    form = PackForm(instance=instancia)

    if request.method == "POST":
        form= PackForm(request.POST, instance=instancia)

        if form.is_valid():
            instancia=form.save(commit=False)
            instancia.save()
    return render(request, "Registro/editar_pack.html", {'form': form})