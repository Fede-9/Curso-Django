from django import forms
from .models import Favoritos


class FavoritoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()



class FavoritoModelForm(forms.ModelForm):
    class Meta:
        model = Favoritos
        fields = '__all__' #['nombre']
