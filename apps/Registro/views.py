from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Pack
from .forms import PackForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import PackSerializer
from rest_framework import status

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

class PackCreate(CreateView):
    model = Pack
    form_class = PackForm
    template_name = 'Registro/pack_form.html'
    success_url = reverse_lazy("listar_packs")    

class PackList(ListView):
    model = Pack
    template_name = 'Registro/list_packs.html'

class PackUpdate(ListView):
    model = Pack
    template_name = 'Registro/pack_form.html'
    success_url = reverse_lazy('list_packs')

class PackDelete(ListView):
    model = Pack
    template_name = 'Registro/pack_delete.html'
    success_url = reverse_lazy('list_packs')

class BuscarPacksView(ListView):
    model = Pack
    template_name = 'Registro/buscar_packs.html'

class SearchResultsView(ListView):
    model = Pack
    template_name = 'Registro/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Pack.objects.filter(
            Q(nombre__icontains=query))
        return object_list    

@api_view(['GET'])
def pack_collection(request):
    if request.method == 'GET':
        packs = Pack.objects.all()
        serializer = PackSerializer(packs, many=True)
        return Response(serializer.data) 

@api_view(['GET', 'PUT', 'DELETE'])
def pack_element(request, pk):
    pack = get_object_or_404(Pack, id=pk)

    if request.method == 'GET':
        serializer = PackSerializer(pack)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        pack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        pack_new = JSONParser().parse(request)
        serializer = PackSerializer(pack, data=pack_new)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                                 

@api_view(['GET', 'POST'])
def pack_collection(request):
    if request.method == 'GET':
        packs = Pack.objects.all()
        serializer = PackSerializer(packs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #Si el proceso de deserealizacion funciona, devolvemos una respuesta con un codigo 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #Si falla el proceso de deserealizacion, devolvemos una respuesta con un codigo 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            