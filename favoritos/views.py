from django.shortcuts import render
from .models import Favoritos
from .forms import FavoritoForm

# Create your views here.

def index_favoritos(request):
    return render(request, 'index.html')


def crear_favoritos(request):

    form = FavoritoForm()

    if request.method == 'POST':
        # nombre = request.POST['nombre']
        # url = request.POST['url']
        form = FavoritoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            url = form.cleaned_data['url']
            Favoritos.objects.create(nombre=nombre, url=url)
        else:
            print(form.errors)
        
        # favorito = Favoritos()
        # favorito.nombre = nombre
        # favorito.url = url
        # favorito.save()

    context = {
        'form':form
    }

    return render(request, 'favoritos/crear.html', context)