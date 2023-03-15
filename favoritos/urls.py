from django.urls import path


from .views import *

app_name = 'favoritos'

urlpatterns = [
    path('', index_favoritos), #127.0.0.1:8000
    path('crear', crear_favoritos),
    path('borrar/<int:pk>', borrar_favoritos),
]