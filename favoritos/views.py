from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Favoritos
from .forms import FavoritoModelForm

# Create your views here.

def index_favoritos(request):
    favoritos_lista = Favoritos.objects.all()

    context = {
        'favoritos_lista':favoritos_lista
    }

    return render(request, 'favoritos/lista.html', context)


def crear_favoritos(request):

    form = FavoritoModelForm()

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST)
        if form.is_valid():
           form.save()
        else:
            print(form.errors)
        

    context = {
        'form':form
    }

    return render(request, 'favoritos/crear.html', context)


def borrar_favoritos(request, pk):
    Favoritos.objects.get(pk=pk).delete()
    return redirect('favoritos:index')
    # return redirect(reverse('favoritos:borrar', kwargs={'pk':pk}))


def detalle_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)
    return render(request, 'favoritos/detalle.html', context={'object':favorito})


def actualizar_favoritos(request, pk):
    favorito = Favoritos.objects.get(pk=pk)

    form = FavoritoModelForm(instance=favorito)

    if request.method == 'POST':
        form = FavoritoModelForm(request.POST, instance=favorito)
        
        if form.is_valid():
           form.save()
        else:
            print(form.errors)
        

    context = {
        'form':form
    }

    return render(request, 'favoritos/crear.html', context)
