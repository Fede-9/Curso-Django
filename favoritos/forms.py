from django import forms


class FavoritoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()


class FavoritoModelForm():
    pass
